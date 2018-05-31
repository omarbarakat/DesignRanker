#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 22:36:07 2017

@author: omar
"""
from Utils.DirIterator import *
from Utils.Properties import *
import re
import numpy as np

class DataLoader:
    
    def __init__(self, dirName, propertiesFileName):
        self.dirName=dirName
        self.loadPropFromFile(propertiesFileName)
    
    def getGenerator(self):
        imgGen=ImageDataGenerator()
        generator = imgGen.flow_from_directory(
            self.dirName,  # this is the target directory
            target_size=(3, self.properties.finalWidth, self.properties.finalHeight),  # all images will be resized to 150x150
            class_mode='binary')  # since we use binary_crossentropy loss, we need binary labels
        return generator

    def getDims(self):
        widths=[]
        heights=[]
        iter=DirIterator(self.dirName)
        i=0
        while(iter.hasNext()):
            i+=1
            img=iter.readNextFile()
            w=len(img[0][0])
            h=len(img[0][0][0])
            widths.append(w)
            heights.append(h)
        return (widths, heights)
    
    def loadPropFromFile(self, file):
        self.properties=Properties.readFromFile(file)
    
    def getImgVecLbl(self):
        iter=DirIterator(self.dirName)
        numOfFiles=min(10, iter.getNumFiles())
        
        features=np.zeros((numOfFiles, 3, self.properties.finalWidth, self.properties.finalHeight))
        labels=np.zeros((numOfFiles, 1))
        
        i=0
        while(iter.hasNext() and i<numOfFiles):
            fnum=re.sub("\.jpg$", '', iter.nameNextFile())
            fnum=int(fnum) if re.match( r'^[0-9]+$', fnum) else -1
            if fnum==-1:
                iter.skipFile()
                continue
            
            lbl =int(1) if fnum<10001 else int(0)     # 1 if in the top 10000
            
            img=np.array(iter.readNextFile())
            features[i, :, :, :] = img
            labels[i] = lbl
            i+=1
        
        return (features, labels)
        
        
        