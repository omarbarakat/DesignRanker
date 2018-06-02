import random
from Utils.DirIterator import DirIterator
from math import floor, ceil
import os
import re
from PIL import Image, ImageChops
from Utils.Properties import Properties
import time

# does not move the file
def exportImage(F_IN, F_OUT, prop):
    size = (prop.cropWidth, prop.cropHeight)
    try:
        image = Image.open(F_IN)
    except:
        print("couldn't open image "+F_IN)
        return
    
    image_size = image.size
    
    finalSize = (prop.finalWidth, prop.finalHeight)
    cropped = image.crop( (0, 0, size[0], size[1]) )
    
    offset_x = max( floor((size[0] - image_size[0]) / 2), 0 )
    offset_y = max( floor((size[1] - image_size[1]) / 2), 0 )
    
    thumb = ImageChops.offset(cropped, offset_x, offset_y)
    thumb.thumbnail(finalSize, Image.ANTIALIAS)
    thumb.save(F_OUT)
    
    # spanin+portugal - greace - swizerland - italy - france - Denemark
   
   
   
def initProp():
    prop=Properties()
    prop.trainSetRatio=0.7
    prop.maxDatasetSize=-1          # all files in train+test (-1 for all)
    prop.cropHeight=1200
    prop.cropWidth=1200
    prop.finalHeight=600
    prop.finalWidth=600
    return prop


def main():
    prop=initProp()
    
    directories=['images/', 'wikis/', 'htmls/']
    extensions=['jpg', 'pkl', 'html']
    rootDir='/media/omar/Data/Miscellaneous/web analysis/'
    setDirs=['train/', 'test/']
    
    featuredDirInd = 0
    
    for d in directories:
        if not os.path.exists(rootDir+d+"train/"):
            os.makedirs(rootDir+d+"train/")
        if not os.path.exists(rootDir+d+"test/"):
            os.makedirs(rootDir+d+"test/")
    
    iter = DirIterator(rootDir+directories[featuredDirInd])
    fileNames = iter.getNamesList()
    random.shuffle(fileNames)
    dataSize = len(fileNames) if prop.maxDatasetSize==-1 else min(prop.maxDatasetSize, len(fileNames))
    
    numTrain=ceil(prop.trainSetRatio*dataSize)
    
    start = time.time()
    for j in range(dataSize):
        fileName=re.sub("\."+extensions[featuredDirInd]+"$", '', fileNames[j])
        
        if j<numTrain:  setDir=setDirs[0]
        else:           setDir=setDirs[1]
        
        for i in range(len(directories)):
            origFPath=rootDir+directories[i]+fileName+'.'+extensions[i]
            distFPath=rootDir+directories[i]+setDir+fileName+'.'+extensions[i]
            if i==featuredDirInd:   # processes the file, makes a copy, but doesn't move it
                exportImage(origFPath, distFPath, prop)
            else:                   # moves the file
                if os.path.isfile(origFPath):
                    os.rename(origFPath, distFPath)
                    
        if j%100==0:
            print("processed "+str(j)+" images")
            print(str((time.time()-start)/60.0)+" minutes have passed")
    
    prop.writeToFile(rootDir+'prop.pkl')
    
if __name__=="__main__":
    main()
    
    
    
    
    