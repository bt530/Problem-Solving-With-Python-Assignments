import copy
empty = [None,None,None,None,None,None,None,None,None]



def testAlgo(game):
    #greedy algo for n=3
    terms = [[0,4,8],[0,5,7],[1,3,8],[2,3,7],[1,5,6],[2,4,6]]
    ones = [0,0,0,0,0,0]
    zero = [0,0,0,0,0,0]


    for i,v in enumerate(game):
        for j,w in enumerate(terms):
            if i in w and v == 1:
                ones[j] += 1
            if i in w and v == 0:
                zero[j] = 1
    targetTerm = None
    for i,v in enumerate(zero):
        if v == 0:
            targetTerm = i
            targetOnes = 0

        

    if targetTerm is None:
        for i,v in enumerate(game):
            if v == None:
                return i


        
    for i,v in enumerate(ones):
        w = zero[i]
        if v > targetOnes and w == 0:
            targetTerm = i
            targetOnes = v

    targetTerms = []

    for i,v in enumerate(ones):
        w = zero[i]
        if v == targetOnes and w == 0:
            targetTerms.append(i)

    print(ones)
    print(zero)
    for t in targetTerms:
        for v in terms[t]:
            for j,w in enumerate(terms):
                if j != t and v in w and game[v] == None and zero[j] == 0:
                    return v
    
    for v in terms[targetTerm]:
        if game[v] == None:
            return v

    print("The algo fails to make all terms 0")






finished = False
trials = [empty]

for i in range(9):#delete this loop for only case where player 0 starts
    newTrial = copy.deepcopy(empty)
    newTrial[i] = 1
    trials.append(newTrial)

trialOrders = copy.deepcopy(trials)
while any([None in i for i in trials]):
    
    deleteList = []
    for i,v in enumerate(trials):
        if None in v:
            print(v)
            print(trialOrders[i])
            algoResult = testAlgo(v)
            
            trials[i][algoResult] = 0
            trialOrders[i][algoResult] = 9 - sum([1*(k == None) for k in trials[i]])
            print(trials[i])
            if None in trials[i]:
                for j in range(9):
                    if trials[i][j] == None:
                        newTrial = copy.deepcopy(trials[i])
                        newTrial[j] = 1
                        trials.append(newTrial)

                        newTrialOrder = copy.deepcopy(trialOrders[i])
                        newTrialOrder[j] = 9 - sum([1*(k == None) for k in newTrial])
                        trialOrders.append(newTrialOrder)
                deleteList.append(i)

    deleteList.reverse()
    for i in deleteList:
        del trials[i]


    


        
        
        
