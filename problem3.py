import matplotlib.pyplot as plt

import random
found = []
for i in range(1000):
    if i%1000 == 0:
        print(i/100000)
    values = list(range(1,2025))
    while len(values) != 1:
        pos = random.randint(0,len(values)-1)
        val1 = values[pos]
        del values[pos]

        pos = random.randint(0,len(values)-1)
        val2 = values[pos]
        del values[pos]

        values.append(abs(val1 - val2))

    found.append(values[0])
    #print(values[0],end = ", ")



plt.hist(found)
plt.xlabel("final number")
plt.ylabel("freq")
plt.show()

print(max(found))
