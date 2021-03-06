#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 22:06:12 2017

@author: omar
"""

import pickle


class Properties:
    @staticmethod
    def readFromFile(file):
        with open(file, 'rb') as pickle_file:
            content=pickle.load(pickle_file)
        return content
    
    
    cropWidth=None
    cropHeight=None
    
    finalWidth=None
    finalHeight=None
    
    trainSetRatio=None
    
    def writeToFile(self, file):
        with open(file, 'wb') as output:
            pickle.dump(self, output)