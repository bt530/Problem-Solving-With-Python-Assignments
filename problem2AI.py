import tkinter
import numpy as np
import copy
import pickle
import time
# 0  1  2
# 3  4  5
# 6  7  8


def det(M):
    return M[0] * M[4] * M[8] - M[0] * M[5] * M[7] - M[3] * M[1] * M[8] + M[3] * M[2] * M[7] + M[6] * M[1] * M[5] - M[6] * M[2] * M[4]

try:
    with open("3x3Logic","rb") as f:
        validMatrices = pickle.load(f)
except:

    validMatrices = []
    count = 0
    matrix = [-1,0,0,0,0,0,0,0,0]
    while count < 2**9:
        matrix[0] += 1
        
        
        for i in range(len(matrix)):
            if matrix[i] == 2:
                matrix[i+1] += 1
                matrix[i] = 0
        if matrix.count(1) == 5 and matrix.count(0) ==4:
            validMatrices.append(copy.deepcopy(matrix))
        #print(matrix)
        count += 1

    length = len(validMatrices)
    for j in range(length):
        i = length - j - 1
        if det(validMatrices[i]) != 0:
               del validMatrices[i]
        
    print(validMatrices)


    pointer = 0
    while True:
        print(str(pointer) + "/" + "3456")
        currentTarget = copy.deepcopy(validMatrices[pointer])

        turn = (currentTarget.count(1) + currentTarget.count(0)) % 2

        if turn == 1:
            for i in range(9):
                if currentTarget[i] == 1:
                    currentTarget[i] = None
                    validMatrices.append(currentTarget)
                    #print(currentTarget)
                    currentTarget = copy.deepcopy(validMatrices[pointer])
        if turn == 0:
            
            for i in range(9):
                if currentTarget[i] == 0:
                    valid = True
                    for j in range(9):
                        currentTarget = copy.deepcopy(validMatrices[pointer])
                        if currentTarget[j] == 1:
                            currentTarget[j] = None
                            currentTarget[i] = 1
                            v = False
                            for k in range(9):
                                if currentTarget[k] == None:
                                    currentTarget[k] = 0
                                    
                                    if any([all([currentTarget[m] == i[m] for m in range(9)]) for i in validMatrices]):
                                        v = True
             
                                        
                                        break
                                    currentTarget[k] = None
                            if not v:
                                valid = False
                                break
                    if valid:
                        currentTarget = copy.deepcopy(validMatrices[pointer])
                        currentTarget[i] = None

                        if not any([all([currentTarget[m] == i[m] for m in range(9)]) for i in validMatrices]):
                            validMatrices.append(currentTarget)
                        #print(currentTarget)
                        currentTarget = copy.deepcopy(validMatrices[pointer])

        pointer += 1
        if any([all([None == i[m] for m in range(9)]) for i in validMatrices]):
            break

        if pointer >= len(validMatrices):
            break

    with open("3x3Logic","wb") as f:
        pickle.dump(validMatrices,f)

def threeByThree0FirstAlgo(game):
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

def threeByThree1FirstAlgo(game):
    for i in range(9):
        if game[i] == None:
            test = copy.deepcopy(game)
            test[i] = 0
            if any([all([test[m] == j[m] for m in range(9)]) for j in validMatrices]):
                return i


def twoByTwoAlgo(game):
    if game[0] == 0 and game[1] == None:
        return 1
    if game[0] == 0 and game[2] == None:
        return 2
    if game[3] == 0 and game[1] == None:
        return 1
    if game[3] == 0 and game[2] == None:
        return 2
    if game[0] == None:
        return 0
    if game[3] == None:
        return 3

def nByNAlgo(game):
    temp = copy.deepcopy(game)
    size = int(np.sqrt(len(game)))
    game = [[game[i+size*j] for i in range(size)] for j in range(size)]

    for i in range(size):
        if game[0][i] == 1 and game[1][i] == None:
            return size + i
        if game[1][i] == 1 and game[0][i] == None:
            return i
        if game[2][i] == 1 and game[3][i] == None:
            return 3*size + i
        if game[3][i] == 1 and game[2][i] == None:
            return 2*size + i
    for i in range(1,len(temp)+1):
        if temp[-i] == None:
            return len(temp)-i
    


print(threeByThree1FirstAlgo([1,None,None,None,None,None,None,None,None]))
global currentAction
currentAction = None

def click(x):
    global currentAction
    currentAction = x
    print(currentAction)
    pass
                
    
while True:
    size = int(input("size: "))
    starts = input("Who starts (1 or 0): ")
    if starts == "0":
        turn = 0
    if starts == "1":
        turn = 1


    game = [None for _ in range(size**2)]
    elements = []

    window = tkinter.Tk()
    for j in range(size):
        for i in range(size):
            elements.append(tkinter.Button(width=10,height=5,command = lambda a=i,b=j:click(size*b+a)))
            elements[-1].grid(column=i,row=j)
    
    while None in game:
        if currentAction is not None and turn == 1 and game[currentAction] is None:
            print(currentAction)
            game[currentAction] = 1
            elements[currentAction].config(text = "1")
            currentAction = None
            turn = 0

        if turn == 0 and None in game:
            if size == 3 and starts == "0":
                x = threeByThree0FirstAlgo(game)
                game[x] = 0
                elements[x].config(text = "0")
                turn = 1
            if size == 3 and starts == "1":
                x = threeByThree1FirstAlgo(game)
                game[x] = 0
                elements[x].config(text = "0")
                turn = 1
            if size == 2:
                x = twoByTwoAlgo(game)
                game[x] = 0
                elements[x].config(text = "0")
                turn = 1
            if size >= 4:
                x = nByNAlgo(game)
                game[x] = 0
                elements[x].config(text = "0")
                turn = 1
                
        window.update()

    time.sleep(5)
    window.destroy()
    
 
