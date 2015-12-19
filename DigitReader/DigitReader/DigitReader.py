import sys
import os
import numpy as np
import datetime 
import subprocess

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
    def getPxDataArray(self): 
        data = self.getPxData()
        features = [data[i*28:i*28+28] for i in range(28)]
        for i in range(28): 
            for j in range(28): 
                features[i][j] = float(features[i][j])
        return features 

# Class to train and predict with the model image classifier.
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

    def trainModel(self, saveto=""):
        print("Training digit recognition model.")
        self.classifier.fit(self.trainDataMatrix, self.labels)

        # dump the model to the given file for later load
        if saveto:
            joblib.dump(self.classifier, saveto)

        self.trained = True

    def loadTrainedModel(self, fname):
        try:
            self.classifier = joblib.load(fname)
            return True
        except:
            print("couldnt load the model.")
            return False

    def predictDigit(self, input_data, reduce_dim=False, model_location="../classifier/tree/digit_model.skm"):
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

    def predictDigitsFromCsv(self, fname, skiprows=1, reduce_dim=False, model_location="../classifier/tree/digit_model.skm"):
        pixel_data = np.loadtxt(fname, delimiter=",", skiprows=skiprows, ndmin = 2)
        return self.predictDigit(pixel_data, reduce_dim, model_location)

    def predictDigitFromImgFiles(self, fnames, reduce_dim=False, model_location="../classifier/tree/digit_model.skm"):
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

# Class to help generate an explanatory visualization for the decision tree's decision on an image input.
class ClassifierExplainer: 
    def __init__(self, reader): 
        self.reader = reader
        self.classifier = reader.classifier 

    def explain(self, input_file):
        if isinstance(self.classifier, DecisionTreeClassifier): 
            self.explain_decision_tree(input_file)
        else: 
            print "Not a decision tree, explanation not supported"

    def explain_decision_tree(self, input_file): 
        print("Generating decision tree file")
        feature_names = [ (i, j) for i in range(28) for j in range(28)]
        #print len(feature_names)
        left      = self.classifier.tree_.children_left
        right     = self.classifier.tree_.children_right
        threshold = self.classifier.tree_.threshold
        #print len(self.classifier.tree_.feature)
        features  = [feature_names[i] for i in self.classifier.tree_.feature]
        value = self.classifier.tree_.value

        # generate a python file in decision-tree.py that, when run, will execute
        # the decision tree and keep track of the nodes traversed:
       
        f = open("decision-tree.py", "w") 
        f.write("import sys\n")
        f.write("import numpy as np\n")
        f.write("from DigitReader import ImageReader\n")
        f.write("img_reader = ImageReader()\n")
        f.write("features_file = sys.argv[1]\n")
        f.write("img_reader.readImgFromFile(features_file)\n")
        f.write("features = img_reader.getPxDataArray()\n")
        f.write("pixels_low = []\n")
        f.write("pixels_high = []\n")
        self.gen_decision_tree(left, right, threshold, features, value, 0, 0, f)
       
        # the file saves the path through the tree in 2 separate files:
        f.write("with open(\"path_low.txt\", \'w\') as f: \n\tf.write(\"\\n\".join([str(px[0]) + \" \" + str(px[1]) for px in pixels_low])) # save path to file\n")
        f.write("with open(\"path_high.txt\", \'w\') as f: \n\tf.write(\"\\n\".join([str(px[0]) + \" \" + str(px[1]) for px in pixels_high])) # save path to file\n")

        f.close()

        # call the program that was just constructed:
        subprocess.call(["python", "decision-tree.py", input_file])


    def gen_path_plot(self, path_high_loc="path_high.txt", path_low_loc="path_low.txt"): 
        # read in the pixels that were in the decision tree path and put them into a grid:
        feature_grid = np.zeros((28,28))
        for k, path_loc in enumerate([path_high_loc, path_low_loc]):
            with open(path_loc) as f: 
                path = f.readlines()
            for i, p in enumerate(path): 
                x, y = p.split(" ")
                path[i] = (int(x), int(y))
            
            for p in path: 
                x, y = p
                feature_grid[x, y]= float((k+1) * 3) # change value based on whether pixel was high or low

        # plot the visualization:
        cmap2 = colors.ListedColormap(["white", "red", "blue"])
        img2 = plt.imshow(feature_grid, interpolation='nearest', cmap = cmap2, origin='lower')
        plt.show()


    def gen_feature_plot(self): 
        features = self.classifier.feature_importances_
        features = [features[i*28:i*28+28] for i in range(28)]
        for i in range(28): 
            for j in range(28): 
                features[i][j] = float(features[i][j])

        cmap2 = colors.LinearSegmentedColormap.from_list('cmap', ['white', 'black'], 256)
        img2 = plt.imshow(features,interpolation='nearest', cmap = cmap2, origin='lower')
        plt.colorbar(img2,cmap=cmap2)
        plt.show()

    def parse_value(self, values):
        values = values.tolist()[0]
        values_pruned = [(i, values[i]) for i in range(len(values)) if values[i] != 0] 
        comment = ""
        if len(values_pruned) > 2: 
            for item in values_pruned: 
                comment += "# " + str(item[0]) + " also had " + str(item[1]) + " samples here \n"

        ans = str(values.index(max(values)))
        comment += "# approximately " + str(int(max(values)))
        comment += " were " + ans + " out of " 
        comment += str(int(sum(values))) + " samples at leaf node"
        return int(ans), " " + comment 

    #recursively defined function to output python if-else code based on the tree data structure from
    #the sklearn model:
    def gen_decision_tree(self, left, right, threshold, features, value, node, depth, f):
        i, j = features[node]
        if (threshold[node] != -2):
                f.write("\t" * depth + "if features[" + str(i) + "][" + str(j) + "] <= " + str(threshold[node]) + ":" + "\n")
                f.write("\t" * (depth + 1) + "pixels_low.append(" + str(features[node]) +")\n")
                if left[node] != -1:
                        self.gen_decision_tree (left, right, threshold, features, value, left[node], depth + 1, f)
                f.write("\t" * depth + "else:" + "\n")
                f.write("\t" * (depth + 1) + "pixels_high.append(" + str(features[node]) +")\n")
                if right[node] != -1:
                        self.gen_decision_tree (left, right, threshold, features, value, right[node], depth + 1, f)
        else:
                ans, explanation = self.parse_value(value[node])
                f.write("\t" * depth + "ans = " + str(ans))
                f.write("\t" * depth + str(explanation) + "\n")

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

    PCA_flag = "-pca" in sys.argv 
    LDA_flag = "-lda" in sys.argv
    PROB_flag = "-prob" in sys.argv
    SAVE_flag = "-save" in sys.argv
   
    if LDA_flag:
        print("Using LDA model")
        model_location = "../classifier/ldaSmall/digit_model.skm"
    else: 
        print("Using default Tree Classifier model.")
        model_location = "../classifier/tree/digit_model.skm"
    digReader = DigitReader(classifier = LDA_flag, debug = debug_flag)

    # run the model training with if retrain needed:
    if retrain:
        sys.stdout.write("Training the classifier and dumping result to classifier folder " + model_location + "\n")
        digReader.getTrainingDataFromCsv("../data/train.csv")
        digReader.trainModel(model_location)

    # predict on the input file if it was given and dump to output.txt:
    if input_file is not None:
        print("Running predictions on the input file.")
        if input_file.endswith(".csv"):
            digits = digReader.predictDigitsFromCsv(input_file, reduce_dim = PCA_flag, model_location=model_location)
            
        else:
            digits = digReader.predictDigitFromImgFiles([input_file], reduce_dim = PCA_flag, model_location=model_location)

        withids = np.transpose(np.array([[i for i in range(1, len(digits) + 1)], digits]))
        name = "../output/output-" + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M") + ".csv"
        
        #if -save, save to a csv named after the time the program was called
        if SAVE_flag:
            np.savetxt(name, withids, header='ImageId,Label', delimiter=',', fmt=['%d', '%d'], comments='')

        # generate the explanation if necessary and produce the plot:
        explainer = ClassifierExplainer(digReader)
        if "-explain-all" in sys.argv: 
            explainer.explain(input_file)
            explainer.gen_path_plot()