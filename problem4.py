global counter
global target

target = 25

counter = 0

def step(position,move,steps):
    global counter
    global target
    position += move
    steps += 1
    if position == target:
        counter += 2**((target-1)-steps)

    if position < target:
        step(position,1,steps)
        step(position,2,steps)

step(1,1,0)
step(1,2,0)
print("succesful outcomes: " + str(counter))

print("probability of success: "+ str(counter/(2**(target-1))))
    
    
