import sys
import os
import numpy as np
import datetime 

from sklearn.lda import LDA
from sklearn.externals import joblib
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier
from PIL import Image

import matplotlib.pyplot as plt
from matplotlib import colors

PROB_flag = False
# class to handle reading in images as input
class ImageReader:
    def __init__(self):
        self.image = None

    def readImgFromFile(self, fname):
        """
        Reads the image from a file and resizes it to the classifier's required size (28x28)
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
            imgDataRaw = self.image.getdata()
            try:
                imgData = map(lambda px: (255.0 - sum(px[:3])/3.0), imgDataRaw)
            except:
                imgData = map(lambda px: (255.0 - px), imgDataRaw)
            imgData = np.array(imgData, np.uint8)
            return imgData

        else:
            raise ValueError("Image hasn't been read in yet.")

# Class to train and predict with the SVM image classifier.
class DigitReader:
    def __init__(self, classifier=None, debug = False):
        np.random.seed(10)
        if classifier == "LDA": 
            self.classifier = LDA()
        else: 
            self.classifier = DecisionTreeClassifier(random_state=0)
        self.dim_reducer = PCA()
        self.trainDataMatrix = None
        self.labels = None
        self.trained = False

        # debug mode restricts trains/tests to 100 data points
        self.debug = debug
        self.debug_training_len = 10000
        self.debug_len = 100

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
        self.labels = labels

    def getTrainingDataFromCsv(self, fname):
        print("Reading in training data from csv file " + fname)
        trainingData = np.loadtxt(fname, delimiter=",", skiprows=1, ndmin = 2)

        if self.debug:
            trainingData = trainingData[:self.debug_training_len, :]
        
        # set the feature matrix and the corresponding labels:
        self.labels = trainingData[:, 0]
        self.trainDataMatrix = trainingData[:, 1:]

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
        self.classifier.fit(self.trainDataMatrix, self.labels)

        # dump the svm to the given file for later load
        if saveto:
            joblib.dump(self.classifier, saveto)

        self.trained = True

    def loadTrainedModel(self, fname):
        try:
            self.classifier = joblib.load(fname)
            return True
        except:
            return False

    def gen_plot(self): 
        features = self.classifier.feature_importances_
        features = [features[i*28:i*28+28] for i in range(28)]
        for i in range(28): 
            for j in range(28): 
                features[i][j] = float(features[i][j])

        cmap2 = colors.LinearSegmentedColormap.from_list('cmap', ['white', 'black'], 256)
        img2 = plt.imshow(features,interpolation='nearest', cmap = cmap2, origin='lower')
        plt.colorbar(img2,cmap=cmap2)

    def predictDigit(self, input_data, reduce_dim=False, model_location="../classifier/tree/digit_svm.skm"):
        """
        Return the predicted classes for given pixel input_data (rows of unrolled 27x27 matrices).
        Reads model from given location if classifier not already trained.
        """
        global PROB_flag
        if not self.trained:
            print("Loading model from\t" + model_location)
            if not self.loadTrainedModel(model_location):
                raise Exception("Model file at " + model_location + " does not exist.")

        if reduce_dim:
            input_data = self.reduceDimPCA(input_data)

        if self.debug:
            print("Debugging with first " + str(min(self.debug_len, len(input_data))) + " rows")
            input_data = input_data[:(self.debug_len), :]
            
        if PROB_flag: 
            probs = self.classifier.predict_proba(input_data)
            print "Probabilities", probs, [float(x) for x in probs[0]]

        output_classes = self.classifier.predict(input_data)
        return output_classes

    def predictDigitsFromCsv(self, fname, skiprows=1, reduce_dim=False, model_location="../classifier/tree/digit_svm.skm"):
        pixel_data = np.loadtxt(fname, delimiter=",", skiprows=skiprows, ndmin = 2)
        return self.predictDigit(pixel_data, reduce_dim, model_location)

    def predictDigitFromImgFiles(self, fnames, reduce_dim=False, model_location="../classifier/tree/digit_svm.skm"):
        image_pixels = []
        results = []
        arrs = []
        for fname in fnames:
            imgReader = ImageReader()
            imgReader.readImgFromFile(fname)
            print("Reading from\t\t" + fname)
            input_data = imgReader.getPxData()
            input_data = input_data.reshape(1, -1)
            prediction = self.predictDigit(input_data, reduce_dim, model_location)
            print ("\tPrediction: " + str(prediction))
            results.append(prediction)
        return results

class ClassifierExplainer: 
    def __init__(self, reader): 
        self.reader = reader
        self.classifier = reader.classifier 

    def explain(self):
        if isinstance(self.classifier, DecisionTreeClassifier): 
            self.explain_decision_tree()
        else: 
            self.explain_lda()

    def explain_decision_tree(self): 
        print("Generating decision tree file")
        left      = self.classifier.tree_.children_left
        right     = self.classifier.tree_.children_right
        threshold = self.classifier.tree_.threshold
        features  = [feature_names[i] for i in self.classifier.tree_.feature]
        value = self.classifier.tree_.value
        decision_str = ""
        gen_decision_tree(left, right, threshold, features, value, decision_str)
        np.savetxt("../output/decision-tree.txt", decision_str)

    def explain_lda(self):
        pass

    def gen_decision_tree(self, left, right, threshold, features, node, decision_str):
        if (threshold[node] != -2):
                decision_str += "if ( " + features[node] + " <= " + str(threshold[node]) + " ) {" + "\n"
                if left[node] != -1:
                        gen_decision_tree (left, right, threshold, features,left[node])
                decision_str += "} else {" + "\n"
                if right[node] != -1:
                        gen_decision_tree (left, right, threshold, features,right[node])
                decision_str += "}" + "\n"
        else:
                decision_str += "return " + str(value[node]) + "\n"

# running the code from the command line:
if __name__ == '__main__':
    global PROG_flag
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

    # PCA 
    PCA_flag = "-pca" in sys.argv 
    LDA_flag = "-lda" in sys.argv
    PROB_flag = "-prob" in sys.argv
   
    if LDA_flag:
        print("Using LDA model")
        model_location = "../classifier/ldaSmall/digit_svm.skm"
    else: 
        print("Using default Tree Classifier model.")
        model_location = "../classifier/tree/digit_svm.skm"

    digReader = DigitReader(classifier = LDA_flag, debug = debug_flag)

    # run the model training with dimensionality reduction if model doesnt exist or retrain needed:
    if retrain:
        sys.stdout.write("Training the classifier and dumping result to classifier folder " + model_location + "\n")
        digReader.getTrainingDataFromCsv("../data/train.csv")

        digReader.trainSVM(model_location)
            

    # predict on the input file if it was given and dump to output.txt:
    if input_file is not None:
        print("Running predictions on the input file.")
        if input_file.endswith(".csv"):
            digits = digReader.predictDigitsFromCsv(input_file, reduce_dim = PCA_flag, model_location=model_location)
            
        else:
            digits = digReader.predictDigitFromImgFiles([input_file], reduce_dim = PCA_flag, model_location=model_location)

        withids = np.transpose(np.array([[i for i in range(1, len(digits) + 1)], digits]))
        name = "../output/output-" + str(datetime.datetime.now()) + ".csv"
        np.savetxt(name, withids, header='ImageId,Label', delimiter=',', fmt=['%d', '%d'], comments='')

    # generate precise or nonprecise explanations
    explainer = ClassifierExplainer(digReader)
    if "-explain-all" in sys.argv: 
        explainer.explain()