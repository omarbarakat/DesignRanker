from CNNClassifier import *
from Utils.DataLoader import *
import numpy as np
import sys
import resource

def memory_limit():
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (get_memory() * 1024 / 2, hard))

def get_memory():
    with open('/proc/meminfo', 'r') as mem:
        free_memory = 0
        for i in mem:
            sline = i.split()
            if str(sline[0]) in ('MemFree:', 'Buffers:', 'Cached:'):
                free_memory += int(sline[1])
    return free_memory


def main():
    rootDir='/media/omar/Data/Miscellaneous/web analysis/'
    trainDir='images/train/'
    testDir='images/test/'
    propFileName='prop.pkl'
    
    trainLoader=DataLoader(rootDir+trainDir, rootDir+propFileName)
    testLoader=DataLoader(rootDir+testDir, rootDir+propFileName)
#    (trainData, trainlbl)=trainLoader.getImgVecLbl()
#    (testData, testlbl)=testLoader.getImgVecLbl()
#    cnn.runModel(trainData, trainlbl, testData, testlbl)
    trainGen = trainLoader.getGenerator()
    testGen  = testLoader.getGenerator()
    
    prop = Properties.readFromFile(rootDir+'prop.pkl')
    cnn=CNNClassifier((3, prop.finalHeight, prop.finalWidth))
    cnn.runModel_gen(trainGen, testGen)

if __name__=="__main__":
    memory_limit()
    main()
