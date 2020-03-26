from random import randint

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
    weights = [randint(-5,5) for x in range(0,numOfAtt)]
    t = randint(-5,5)

    for row in trainSet:
        data = row.split(';')[:-1]
        classifier = str(row.split(';')[-1]).strip()

        net = calculate_net(weights, data)
        res = 0
        if net>=t:
           res = 1

        if classifiers[res] != classifier:
            d=1 
            if(res==1): d=0

            weights = delta_rule(weights, d, res, alfa, data, t)

            t = float(weights[-1])
            weights = weights[:-1]
            

        
            net = calculate_net(weights, data)
            
            res = 0
            if net>=t:
                res = 1

    weights.append(t)
    #zwraca wektor razem z wartością t na ostatnim miejscu
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

    return accuracy

def classify(x: list, w: list, t: float) -> str:
    net = calculate_net(w, x)
    
    res = 0
    if net>=t:
        res = 1

    return res

    


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

t = float(w_prim[-1])
weights = w_prim[:-1]

accuracy = testing(testSet, w_prim, classifiers)

print(f"Accuracy:")
print(f"{classifiers[0]}: ")
print(f"poprawnie: {accuracy[0][0]} \nwszystkie: {accuracy[0][1]}")
print(f"{classifiers[1]}: ")
print(f"poprawnie: {accuracy[1][0]} \nwszystkie: {accuracy[1][1]}")


while True:
    v = input("Your vector (separate with ';')[or exit]: ")
    if v.lower() == 'exit': break

    data = v.split(';')

    print(f'Answere: {classifiers[classify(data, weights, t)]}')


