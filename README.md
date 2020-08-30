# Digit-Recogniser

## Demo:
![Alt Text](https://github.com/Harsh19397/Digit-Recogniser/blob/master/demo.gif)

## Description: 
This is a simple project where I have implelemented the convolutional neural network in order to predict the digits. First I have used the dataset provided by the scikit learn library and trained the model on it, which is then saved as mnist_model.h5. Then this model is being used in the drawNumber.py file. Here you draw a number and the trained model predicts it.

## Pre requisities:

Install the dependencies by running the below commands in a python installed environment:
  1. pip install tensorflow
  2. pip install numpy
  3. pip install keras
  4. pip install tkinter
  5. pip install pygame
  6. pip install matplotlib

## How to use:

If you want to train the model yourself, first run the file creat_model.py file by going to the command prompt with python added to the environment variables and running the command "python create_model.py"

The model will be trained and a mnist_model.h5 file with a trained model will be generated. This we can use to test the file by running testing_model.py file.

## Have fun:

Now have fun by running drawNumber.py file. Enter the command "python drawNumber.py" in the command prompt and have fun watching the model predicting your digits.
