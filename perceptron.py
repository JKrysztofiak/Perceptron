
def multiply_vector(v: list, m: int) -> list:
    res = []
    for value in v:
        ret.append(float(value)*m)
    return res

def add_vectors(v1: list,v2: list) -> list:
    res = []
    for i in range(0,len(v1)):
        res.append(float(v1[i])+float(v2[i]))

    return res


def calculate_net(w: list, p: list) -> float:
    res = 0
    for i in range(0,len(w)):
        res += float(p[i])*float(w[i])

    return res

def training_delta(trainSet: list, classifiers: list, numOfAtt: int, alfa: float) -> list:
    weights = [0]*attributes
    t = 0

    for row in trainSet:
        data = row.split(';')[:-1]
        classifier = row.split(';')[-1]

        net = calculate_net(weights, data)

        res = 0
        if net>=t:
           res = 1

        print(res)

    


testSetPath = 'test-set.csv'
trainSetPath = 'train-set.csv'
a = 1

with open(testSetPath) as f:
    testSet = f.readlines()
    
with open(trainSetPath) as  f:
    trainSet = f.readlines()

numOfAtt = len(trainSet[0].split(';'))-1

classifiers = ['Iris-setosa','Iris-versicolor']

w_prim = training_delta(trainSet, classifiers, numOfAtt, a)


#calculate Net


#check if Net > t

#Delta 

#check if correct 