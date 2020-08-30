#Importing libraries
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import keras
import numpy as np

#Loading the dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

for train in range(len(x_train)):
    for row in range(28):
        for x in range(28):
            if x_train[train][row][x] != 0:
                x_train[train][row][x] = 1

#Initializing the Convolutional neural network
model = tf.keras.Sequential()

#layer_01
model.add(tf.keras.layers.Conv2D(20, kernel_size=3, activation='relu', input_shape=[28, 28, 1]))
model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

#layer_02
model.add(tf.keras.layers.Conv2D(10, kernel_size=3, activation='relu'))
model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

#Flatten Layer
model.add(tf.keras.layers.Flatten())

#Fully Connected layer_01
model.add(tf.keras.layers.Dense(128, activation='relu'))

#Output layer
model.add(tf.keras.layers.Dense(units=10, activation='softmax'))

#Compliling the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

#Training the model
x_train_fit = np.expand_dims(x_train, axis=3)
x_test_fit = np.expand_dims(x_test, axis=3)
model.fit(x_train_fit, y_train, epochs=3, validation_data=(x_test_fit, y_test))

#Save Model
model.save('mnist_model.h5')