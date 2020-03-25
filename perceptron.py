
from array import *

def multiply_vector(v: list, m: float) -> list:
    res = []
    for value in v:
        res.append(float(value)*m)
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


def delta_rule(w: list, d: int, y: int, alfa: float, x: list, t: float) -> list:
    
    w.append(t)
    x.append(-1)

    w_prim = add_vectors(w, (multiply_vector(x,((d-y)*alfa))))

    return w_prim



def training(trainSet: list, classifiers: list, numOfAtt: int, alfa: float) -> list:
    weights = [1]*numOfAtt
    t = 0.75

    for row in trainSet:
        data = row.split(';')[:-1]
        classifier = str(row.split(';')[-1]).strip()

        net = calculate_net(weights, data)
        # print(net)
        res = 0
        if net>=t:
           res = 1

        if classifiers[res] != classifier:
            d=1 
            if(res==1): d=0

            # print(f"B4: {weights} t={t} p={data} alfa={alfa} d={d} y={res}")
            weights = delta_rule(weights, d, res, alfa, data, t)

            t = float(weights[-1])
            weights = weights[:-1]
            

            # print(f"DELTA RULE APPLIED {weights} t={t}")
            net = calculate_net(weights, data)
            
            res = 0
            if net>=t:
                res = 1

            # if classifiers[res] == classifier:
            #     print(f"NOW {classifier} == {classifiers[res]}")
            # else:
            #     print(f"{classifier} STILL IS NOT {classifiers[res]}")

    weights.append(t)
    return weights


def testing(testSet: list, w: list, classifiers: list) -> list: 
    accuracy = [[0,0],[0,0]]
    # accuracy[0] - grupa 
    # accuracy[0][0] - poprawnie zaklasyfikowane z grupy
    # accuracy[0][1] - wszystkie klasyfikowane z grupy

    t = float(w[-1])
    weights = w[:-1]

    for row in testSet:
        data = row.split(';')[:-1]
        classifier = str(row.split(';')[-1]).strip()

        net = calculate_net(weights, data)
    
        res = 0
        if net>=t:
           res = 1

                
        if res == 0:
            if classifiers[0] == classifier:
                accuracy[0][0]+=1
                accuracy[0][1]+=1
            else:
                accuracy[1][1]+=1
        else:
            if classifiers[1] == classifier:
                accuracy[1][0]+=1
                accuracy[1][1]+=1
            else:
                accuracy[0][1]+=1

        print(f"{classifiers[res]} ?= {classifier}")
        print(f"Accuracy:")
        print(f"{classifiers[0]}: ")
        print(f"poprawnie: {accuracy[0][0]} \nwszystkie: {accuracy[0][1]}")
        print(f"{classifiers[1]}: ")
        print(f"poprawnie: {accuracy[1][0]} \nwszystkie: {accuracy[1][1]}")

    return accuracy


    


testSetPath = 'test-set.csv'
trainSetPath = 'train-set.csv'
a = 2

with open(testSetPath) as f:
    testSet = f.readlines()
    
with open(trainSetPath) as  f:
    trainSet = f.readlines()

numOfAtt = len(trainSet[0].split(';'))-1

classifiers = ['Iris-setosa','Iris-versicolor']

w_prim = training(trainSet, classifiers, numOfAtt, a)

accuracy = testing(testSet, w_prim, classifiers)

print(f"Accuracy:")
print(f"{classifiers[0]}: ")
print(f"poprawnie: {accuracy[0][0]} \nwszystkie: {accuracy[0][1]}")
print(f"{classifiers[1]}: ")
print(f"poprawnie: {accuracy[1][0]} \nwszystkie: {accuracy[1][1]}")