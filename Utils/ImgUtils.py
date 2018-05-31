#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 21:37:29 2017

@author: omar
"""
import numpy as np

class ImgUtils:
    
    def __init__(self):
        self.iterator=DirIterator("")
    
    def shapeImage(image, width, height):
        newImg=np.zeros(image.shape[0], width, height)
        xShift=max(0, floor((image.shape[1]-width)/2))
        yShift=max(0, floor((image.shape[2]-height)/2))
        xNewShift=max(0, floor((width-image.shape[1])/2))
        yNewShift=max(0, floor((height-image.shape[2])/2))
        
        newImg[xNewShift:xNewShift+width][yNewShift:yNewShift+height]=\
            image[xShift:xShift+width][yShift:yShift+height]
        return newImg
        
        
    def exportImage(origFPath, distFPath, width, height):
        img = self.iterator.readFile(origFPath)
        self.shapeImage(img, width, height)
        