# -*- coding: utf-8 -*-
from Utils.DataLoader import *
import matplotlib.pyplot as plt

def main():
    rootDir='/media/omar/Data/Miscellaneous/web analysis/'
    trainDir='images/train/'
    testDir='images/test/'
    propFileName='prop.pkl'
    
    loader=DataLoader(rootDir+trainDir, rootDir+propFileName)
    (widths, heights) = loader.getDims()    # height=2000, width 15000
    
    plt.hist(widths, normed=True, bins=50)
    plt.ylabel('Probability')
    plt.figure()
    plt.hist(heights, normed=True, bins=50)
    plt.ylabel('Probability')

if __name__=="__main__":
    main()
