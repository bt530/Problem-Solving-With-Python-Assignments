
import random
n=6
glasses = [0 for _ in range(n)]

while True:
    dist = [random.random() for _ in range(n)]
    dist = sorted(dist)
    dist.append(1)
    dist = [(dist[i+1]-dist[i])/2 for i in range(n)]

    glasses = [glasses[i] + dist[i] for i in range(n)]


    print(glasses)

    if any([i>1 for i in glasses]):
        print("A wins")
        break

    sums = [glasses[i-1]+glasses[i] for i in range(n )]
    maxVal = 0
    maxPos = 0
    for i,v in enumerate(sums):
        if v > maxVal:
            maxVal = v
            maxPos = i

    glasses[maxPos] = 0
    glasses[maxPos-1] = 0


    print(glasses)

