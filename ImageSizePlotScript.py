# -*- coding: utf-8 -*-
from Utils.DataLoader import DataLoader
import matplotlib.pyplot as plt
from Utils.Constants import Constants

def main():
    const=Constants()
    
    loader=DataLoader(const.rootDir+const.trainDir, const.rootDir+const.propFileName)
    (widths, heights) = loader.getDims()    # height=2000, width 15000
    
    plt.hist(widths, normed=True, bins=50)
    plt.ylabel('Probability')
    plt.figure()
    plt.hist(heights, normed=True, bins=50)
    plt.ylabel('Probability')

if __name__=="__main__":
    main()
