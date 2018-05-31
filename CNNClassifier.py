#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 22:33:13 2017

@author: omar
"""

import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Convolution2D
from keras.layers.convolutional import Convolution3D
from keras.layers.convolutional import MaxPooling3D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils
from keras import backend as K

K.set_image_dim_ordering('th')

class CNNClassifier:
    def __init__(self, imageShape):
        # fix random seed for reproducibility
        seed = 7
        np.random.seed(seed)
        self.imageShape=imageShape
        self.model = self.baseline_model_2D()
    
    def runModel_gen(self, trainGen, validationGen):
        self.model.fit_generator(trainGen, validation_data=validationGen,
                                 samples_per_epoch=trainGen.nb_samples,
                                 nb_epoch=2,
                                 nb_val_samples=validationGen.nb_samples)
    
    def runModel(self, X_train, y_train, X_test, y_test):
        # normalize data
        #        maxi = max(np.max(X_train[:]), np.max(X_test[:]))
        #        X_train /= float(maxi)
        #        X_test /= float(maxi)
        
        self.model.fit(X_train, y_train, validation_split=0.05, nb_epoch=3, batch_size=20, verbose=2)
        # Final evaluation of the model
        scores = self.model.evaluate(X_test, y_test, verbose=0)
        print("Baseline Error: %.2f%%" % (100-scores[1]*100))


    def baseline_model_2D(self):
        # create model
        model = Sequential()
        model.add(Convolution2D(32, 20, 10, border_mode='full', input_shape=self.imageShape, activation='relu'))
#        model.add(MaxPooling2D(pool_size=(2, 2)))
#        model.add(Dropout(0.2))
        model.add(Flatten())
#        model.add(Dense(8, activation='relu'))
        model.add(Dense(1, activation='softmax'))       # the final decision: in top 10,000 or not
        # Compile model
        model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
        return model

