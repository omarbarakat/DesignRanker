#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 22:44:02 2017

@author: omar
"""
import os
import numpy as np
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

class DirIterator:
    def __init__(self, rootDir):
        self.rootDir = rootDir
        self.dataDirs = sorted(os.listdir(rootDir))
        self.curFile = 0
        
    # start iterating on files in the directory from the begining
    def rewind(self):
        self.curFile = 0
        
    def hasNext(self):
        return self.curFile < len(self.dataDirs)
    
    # returns the data in the format (joint, frame, x-y-z-c)
    def readNextFile(self):
        if not self.hasNext():
            return None
        dataFile = self.rootDir+self.dataDirs[self.curFile]
        self.curFile += 1
        return self.readFile(dataFile)
        
    def readFile(self, dataFile):
        try:
            image = Image.open(dataFile)
            x = np.fromstring(image.tobytes(), dtype=np.uint8)
            x = x.reshape((1, 3, image.size[1], image.size[0])) 
        except:
            print("couldn't open image"+dataFile)
            return [[[[[0]]]]]
        
        #x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, w, h)
        
        return x
        
    def nameNextFile(self):
        if not self.hasNext():
            return None
        return self.dataDirs[self.curFile]
        
    def skipFile(self):
        if self.hasNext():
            self.curFile += 1
    
    def getNumFiles(self):
        return len(self.dataDirs)

    def getNamesList(self):
        return self.dataDirs
        