import numpy as np
import copy

# 0  1  2
# 3  4  5
# 6  7  8


def det(M):
    return M[0] * M[4] * M[8] - M[0] * M[5] * M[7] - M[3] * M[1] * M[8] + M[3] * M[2] * M[7] + M[6] * M[1] * M[5] - M[6] * M[2] * M[4]


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
    currentTarget = copy.deepcopy(validMatrices[pointer])

    turn = (currentTarget.count(1) + currentTarget.count(0)) % 2

    if turn == 1:
        for i in range(9):
            if currentTarget[i] == 1:
                currentTarget[i] = None
                validMatrices.append(currentTarget)
                print(currentTarget)
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
                    print(currentTarget)
                    currentTarget = copy.deepcopy(validMatrices[pointer])

    pointer += 1
    if any([all([None == i[m] for m in range(9)]) for i in validMatrices]):
        break

    if pointer >= len(validMatrices):
        break


                
    

 
