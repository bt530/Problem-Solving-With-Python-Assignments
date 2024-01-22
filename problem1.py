count = 0
pairs = [(i,j) for i in range(10) for j in range(10)]
totalLength = 0

while len(pairs) != 0:
    currentStart = pairs[0] #picks the first pair of digits that hasn't been used in a bracelet yet
    bracelet = [currentStart[0],currentStart[1]] #initialises new bracelet
    del pairs[0]
    first = currentStart[1]
    second = (currentStart[0] + currentStart[1]) % 10
    while (first,second) != currentStart: #loops through bracelet until we have arrived back at start
        bracelet.append(second)
        pairs.remove((first,second))
        _f = second
        second = (first + second) % 10
        first = _f
    count += 1
    print(bracelet[:-1]) #ignores last term because that's where it starts to wrap around
    print("The above bracelet has length: "+ str(len(bracelet[:-1])))
    totalLength += len(bracelet[:-1])

print("There are: " + str(count) + " bracelets formed")
print("The total lengths of the bracelets is: " +  str(totalLength))
input()
    
