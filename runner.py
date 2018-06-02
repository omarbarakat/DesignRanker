from CNNClassifier import CNNClassifier
from Utils.DataLoader import DataLoader
import resource
from Utils.Constants import Constants
from Utils.Properties import Properties

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
    const=Constants()

    trainLoader=DataLoader(const.rootDir+const.trainDir, const.rootDir+const.propFileName)
    testLoader=DataLoader(const.rootDir+const.testDir, const.rootDir+const.propFileName)
#    (trainData, trainlbl)=trainLoader.getImgVecLbl()
#    (testData, testlbl)=testLoader.getImgVecLbl()
#    cnn.runModel(trainData, trainlbl, testData, testlbl)
    trainGen = trainLoader.getGenerator()
    testGen  = testLoader.getGenerator()
    
    prop = Properties.readFromFile(const.rootDir+'prop.pkl')
    cnn=CNNClassifier((3, prop.finalHeight, prop.finalWidth))
    cnn.runModel_gen(trainGen, testGen)

if __name__=="__main__":
    memory_limit()
    main()
