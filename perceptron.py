


testSetPath = 'test-set.csv'
trainSetPath = 'train-set.csv'

with open(testSetPath) as f:
    testSet = f.readlines()
    
with open(trainSetPath) as  f:
    trainSet = f.readlines()

atributes = len(trainSet[0].split(';'))-1

print(atributes)

#calculate Net
