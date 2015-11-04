﻿import sys
import os
import numpy as np
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.externals import joblib
from sklearn.multiclass import OneVsRestClassifier
from PIL import Image

class ImageReader:
    def __init__(self):
        self.image = None

    def readImgFromFile(self, fname):
        self.image = Image.open(fname)
        self.image = self.image.resize((27,27))

    def readImgFromBuffer(self, buf, size):
        self.image = Image.frombuffer("RGBA", size, buf)

    def getPxData(self):
        if self.image is not None:
            imageSize = self.image.size

            imgData = map(lambda px: sum(px[:3])/3, self.image.getdata())
            imgData = np.array(imgData, np.uint8)
            
            return imgData

        else:
            raise ValueError("Image hasn't been read in yet.")

class DigitReader:
    def __init__(self, debug = False):
        self.svm_classifier = OneVsRestClassifier(SVC(kernel="linear"))
        self.dim_reducer = PCA(n_components=10)
        self.trainData = []
        self.trainDataMatrix = None
        self.train_y = None
        self.trained = False
        self.debug = debug

    def getTrainingDataFromImages(self, fnames, labels):
        for fname in fnames:
            imgReader = ImageReader()
            imgReader.readImgFromFile(fname)
            self.trainData.append(imgReader.getPxData())
        self.trainDataMatrix = np.array(self.trainData)
        self.train_y = labels

    def getTrainingDataFromCsv(self, fname):
        print("Reading in training data from csv file " + fname)
        trainingData = np.loadtxt(fname, delimiter=",", skiprows=1, ndmin = 2)

        if self.debug:
            trainingData = trainingData[1:100, :]
 
        self.train_y = trainingData[:, 0]
        print(self.train_y)
        self.trainDataMatrix = trainingData[:, 1:]

    def reduceDimPCA(self, data):
        return self.dim_reducer.fit_transform(data)

    def reduceDimTrainingData(self):
        print("Reducing dimension of training data.")
        self.trainDataMatrix = self.reduceDimPCA(self.trainDataMatrix)

    def trainSVM(self, saveto=""):
        print("Training svm model.")
        self.svm_classifier.fit(self.trainDataMatrix, self.train_y)
        if saveto:
            joblib.dump(self.svm_classifier, saveto)

        self.trained = True

    def loadTrainedModel(self, fname):
        try:
            self.svm_classifier = joblib.load(fname)
            return True
        except:
            return False

    def predictDigit(self, input_data, model_location="../classifier/digit_svm.skm"):
        if not self.trained:
            print("Loading model.")
            if not self.loadTrainedModel(model_location):
                raise Exception("Model file at " + model_location + " does not exist.")

        input_data = self.reduceDimPCA(input_data)
        if self.debug:
            input_data = input_data[1:100, :]

        output_classes = self.svm_classifier.predict(input_data)
        return output_classes

    def predictDigitsFromCsv(self, fname, skiprows=1, model_location="../classifier/digit_svm.skm"):
        pixel_data = np.loadtxt(fname, delimiter=",", skiprows=skiprows, ndmin = 2)
        return self.predictDigit(pixel_data, model_location)

    def predictDigitFromImgFiles(self, fnames, model_location="../classifier/digit_svm.skm"):
        image_pixels = []
        for fname in fnames:
            imgReader = ImageReader()
            imgReader.readImgFromFile(fname)
            image_pixels.append(imgReader.getPxData())

        return self.predictDigit(np.array(image_pixels), model_location)






if __name__ == '__main__':    
    retrain = "-r" in sys.argv
    try:
        input_file_idx = sys.argv.index("-i") + 1
        if input_file_idx >= len(sys.argv):
            raise Exception("No input file provided")
        else:
            input_file = sys.argv[input_file_idx]
    except:
        input_file = None

    digReader = DigitReader(debug = True)

    if not os.path.isfile("../classifier/digit_svm.skm") or retrain:
        sys.stdout.write("Training the classifier and dumping result to classifier folder.\n")
        digReader.getTrainingDataFromCsv("../data/train.csv")
        digReader.reduceDimTrainingData()
        digReader.trainSVM("../classifier/digit_svm.skm")

    if input_file is not None:
        print("Running predictions on the input file.")
        if input_file.endswith(".csv"):
            digits = digReader.predictDigitsFromCsv(input_file)
        else:
            digits = digReader.predictDigitFromImgFiles([input_file])

        np.savetxt("../output/output.txt", digits, fmt='%d')