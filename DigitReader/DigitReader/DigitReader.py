import sys
import os
import numpy as np
#from sklearn.svm import SVC
from sklearn.lda import LDA
from sklearn.decomposition import PCA
from sklearn.externals import joblib
#from sklearn.multiclass import OneVsRestClassifier
from PIL import Image

# class to handle reading in images as input
class ImageReader:
    def __init__(self):
        self.image = None

    def readImgFromFile(self, fname):
        """
        Reads the image from a file and resizes it to the classifier's required size (27x27)
        """
        self.image = Image.open(fname)
        self.image = self.image.resize((28,28))

    def readImgFromBuffer(self, buf, size):
        self.image = Image.frombuffer("RGBA", size, buf)

    def getPxData(self):
        """
        Returns the image data as an unrolled matrix of averaged pixel values.
        """
        if self.image is not None:
            imageSize = self.image.size
            print(imageSize)
            print(self.image.getdata()[0])
            imgDataRaw = self.image.getdata()
            try:
                imgData = map(lambda px: (255.0 - sum(px[:3])/3.0), imgDataRaw)
            except:
                imgData = imgData = map(lambda px: (255.0 - px), imgDataRaw)
            imgData = np.array(imgData, np.uint8)
            
            return imgData

        else:
            raise ValueError("Image hasn't been read in yet.")

# Class to train and predict with the SVM image classifier.
class DigitReader:
    def __init__(self, debug = False):
        self.svm_classifier = LDA()
        self.dim_reducer = PCA(n_components=10)
        self.trainDataMatrix = None
        self.train_y = None
        self.trained = False

        # debug mode restricts trains/tests to 100 data points
        self.debug = debug

    def getTrainingDataFromImages(self, fnames, labels):
        """
        Given image file names and labels, reads in training data set.
        """
        trainData = []
        for fname in fnames:
            imgReader = ImageReader()
            imgReader.readImgFromFile(fname)
            trainData.append(imgReader.getPxData())
        self.trainDataMatrix = np.array(trainData)
        self.train_y = labels

    def getTrainingDataFromCsv(self, fname):
        print("Reading in training data from csv file " + fname)
        trainingData = np.loadtxt(fname, delimiter=",", skiprows=1, ndmin = 2)

        if self.debug:
            trainingData = trainingData[:30000, :]
        
        # set the feature matrix and the corresponding labels:
        self.train_y = trainingData[:, 0]
        print(self.train_y[0:5])
        self.trainDataMatrix = trainingData[:, 1:]
        print(self.trainDataMatrix[0:5, 120:135])

    def reduceDimPCA(self, data):
        """
        Reduce dimensionality of data matrix (hardcoded to 10 components right now).
        """
        return self.dim_reducer.fit_transform(data)

    def reduceDimTrainingData(self):
        print("Reducing dimension of training data.")
        self.trainDataMatrix = self.reduceDimPCA(self.trainDataMatrix)

    def trainSVM(self, saveto=""):
        print("Training svm model.")
        self.svm_classifier.fit(self.trainDataMatrix, self.train_y)

        # dump the svm to the given file for later load
        if saveto:
            joblib.dump(self.svm_classifier, saveto)

        self.trained = True

    def loadTrainedModel(self, fname):
        try:
            self.svm_classifier = joblib.load(fname)
            return True
        except:
            return False

    def predictDigit(self, input_data, reduce_dim=False, model_location="../classifier/digit_svm.skm"):
        """
        Return the predicted classes for given pixel input_data (rows of unrolled 27x27 matrices).
        Reads model from given location if classifier not already trained.
        """
        if not self.trained:
            print("Loading model.")
            if not self.loadTrainedModel(model_location):
                raise Exception("Model file at " + model_location + " does not exist.")

        if reduce_dim:
          input_data = self.reduceDimPCA(input_data)

        if self.debug:
           input_data = input_data[30000:, :]

        output_classes = self.svm_classifier.predict(input_data)
        return output_classes   

    def predictDigitsFromCsv(self, fname, skiprows=1, reduce_dim=False, model_location="../classifier/digit_svm.skm"):
        pixel_data = np.loadtxt(fname, delimiter=",", skiprows=skiprows, ndmin = 2)
        pixel_data = pixel_data[:, 1:]
        return self.predictDigit(pixel_data, reduce_dim, model_location)

    def predictDigitFromImgFiles(self, fnames, reduce_dim=False, model_location="../classifier/digit_svm.skm"):
        image_pixels = []
        for fname in fnames:
            imgReader = ImageReader()
            imgReader.readImgFromFile(fname)
            #image_pixels.append()
            print(self.predictDigit(imgReader.getPxData(), reduce_dim, model_location))





# running the code from the command line:
if __name__ == '__main__':
    # -r flag retrains the model
    retrain = "-r" in sys.argv

    # -i + file indicates input
    try:
        input_file_idx = sys.argv.index("-i") + 1
        if input_file_idx >= len(sys.argv):
            raise Exception("No input file provided")
        else:
            input_file = sys.argv[input_file_idx]
    except:
        input_file = None

    # -debug turns on debug mode
    debug_flag = "-debug" in sys.argv

    #reduce dim?
    PCA_flag = "-pca" in sys.argv

    digReader = DigitReader(debug = debug_flag)

    # run the model training with dimensionality reduction if model doesnt exist or retrain needed:
    if retrain:
        sys.stdout.write("Training the classifier and dumping result to classifier folder.\n")
        digReader.getTrainingDataFromCsv("../data/train.csv")

        if PCA_flag:
            print("creating reduced dim classifier.")
            digReader.reduceDimTrainingData()
            digReader.trainSVM("../classifier/reducedDim/digit_svm.skm")
        else:
            digReader.trainSVM("../classifier/ldaSmall/digit_svm.skm")

            #pixel_data = np.loadtxt("../data/train.csv", delimiter=",", skiprows=1, ndmin = 2)
            #pixel_data_y = pixel_data[:, 0]
            #pixel_data = pixel_data[:, 1:]
            
            #predictions = digReader.predictDigit(pixel_data[30000:, :])
            #print(pixel_data_y)
            #print(predictions)
            #correct = np.equal(predictions, pixel_data_y[30000:])
            #print(sum(correct))
            

    # predict on the input file if it was given and dump to output.txt:
    if input_file is not None:
        print("Running predictions on the input file.")
        if input_file.endswith(".csv"):
            digits = digReader.predictDigitsFromCsv(input_file,  model_location="../classifier/train1000/digit_svm.skm")
            
        else:
            digits = digReader.predictDigitFromImgFiles([input_file],  model_location="../classifier/ldaSmall/digit_svm.skm")

        #np.savetxt("../output/output.txt", digits, fmt='%d')