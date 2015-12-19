DigitReader comes pre-equipped with trained classifiers using the LDA and Decision Tree models. 

# Directory structure

The main script is located at /DigitReader/DigitReader.py. Training and test data are in /data, outputs from the predictor are in /output, and classifier data is in /classifier.

# How to use - typical use case 

1. REQUIREMENTS: 
You must have an environment with the following python packages installed to run the code:
    - numpy
    - scipy
    - sklearn
    - matplotlib
    - PIL
    If running the code on the zoo, these can be accessed by using a virtual environment with the packages installed (since new packages cant be installed on the zoo). A virtual environment with the packages installed has been provided at `/home/accts/isg2/cs458/.myenv`.
    To activate it, run `source /home/accts/isg2/cs458/.myenv/bin/activate` from anywhere in the zoo.

2. To retrain the model, run the script with the -r flag. This is highly recommended if you are running the program for the first time somewhere other than the zoo, because the models are often not compatible across operating systems. For example, run the following before running predictions (or if predictions arent working with some error):
    - `python DigitReader.py -r`

3. PREDICT ON INPUT:
To get a prediction on the image file stored at your/image/file.jpg: 
    - `python DigitReader.py -i your/image/file.jpg` 
    - Note that the code currently only works on JPEG files. Please convert image files to .jpg before using (this can be done with the builtin `convert` command line utility on most linux machines).

Or you can use sample test file we provide. This csv has test images converted into the format for the classifier (a num_samples * 784 data array). 
    - `python DigitReader.py -i ../data/test.csv` 

This is a simple image file that we provide the model is correct on:
    - `python DigitReader.py -i ../data/0.jpg`

4. OUTPUT:
For an image file, the system will print out the predicted digit.
If the -save flag is used, output files are saved under the /output folder, timestamped with the date and time when you ran the program. Each output file is a .csv, with the first column containing image ids (the ids are just increasing integers in the order of images passed in) and the second containing the predicted digit. 

# Overview of Command Line Options

- `-i` passes input. It should be followed by a path to a .jpg file or a .csv file that the model should be run on.
- `-r` retrains the model. The model will be trained on the training data in /data/train.csv and the model will be saved in a location dependent on which type of model is trained (lda or tree).
- `-lda` trains the lda model or uses it on the input. The default is to use a decision tree classifier.
- `-debug` will cause the model to be trained on a small subset of the training data during a retrain.
- `-save` will save the results of prediction to an output file.
- `-prob` will make the model print the probabilities for each prediction along with the prediction.
- `-explain-all` If the input file is an image, this will show a plot that visualizes how the decision tree classifier came to its decision. The red pixels are pixels that were over some threshold, and the blue pixels are pixels that were below some threshold (after the image was resized to 28x28). At each of these pixels, the classifier moved closer to classifying the image under the produced label. See writeup for more details on what this explanation means given the underlying model.
