#Importing libraries
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import keras
import numpy as np

#Loading the dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#Data Preprocessing
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)
x_train = np.expand_dims(x_train, axis=3)
x_test = np.expand_dims(x_test, axis=3)
for train in range(len(x_train)):
    for row in range(28):
        for x in range(28):
            if x_train[train][row][x] != 0:
                x_train[train][row][x] = 1

#Loading the model                
model = tf.keras.models.load_model('mnist_model.h5')

#Making predictions over the test set
predictions = model.predict(x_test)

#Calculating the accuracy and results of our model.
count = 0
for x in range(len(predictions)):
    guess = np.argmax(predictions[x])
    actual = y_test[x]
    if guess != actual:
        count+=1
print("The total number of wrong guesses out of ", len(x_test), "  are: ", count, ".")
print("Accuracy of the model on a test set is: ",100 - (count/10000)*100, "%")