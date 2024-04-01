import tkinter
import math
import time

global canvas
global glasses
global glassesEntry

global mouseValue
mouseValue = "up"

global mouseX
mouseX = 0

global mouseY
mouseY = 0

def leftDown(event):
    global mouseValue
    mouseValue = "down"

def leftUp(event):
    global mouseValue
    mouseValue = "up"

def mouseMotion(event):
    global mouseX
    global mouseY
    mouseX = window.winfo_pointerx() - window.winfo_x()
    mouseY = window.winfo_pointery() - window.winfo_y()
    #print(mouseX,mouseY)

glasses = []


class Glass():
    def __init__(self,pos):
        self.x = pos*50 + 30
        self.y = 300
        self.value = 0
        self.height = 100

    def update(self):
        canvas.create_rectangle(self.x-20,self.y+self.height,self.x+20,self.y-self.height)
        canvas.create_rectangle(self.x-20,self.y+self.height - self.value*self.height*2,self.x+20,self.y+self.height,fill='blue')


    def checkHitBox(self,x,y):
        return (abs(x - self.x) < 20 and abs(y-self.y) < self.height)

        
def fillGlasses():
    global glasses
    global mouseValue
    global mouseX
    global mouseY
    mouseValue = "up"
    remaining = 0.5
    lastTime = time.time()
    while remaining > 0:
        newTime = time.time()
        dt = newTime - lastTime
        lastTime = newTime
        changed = False
        for i in glasses:
            if i.checkHitBox(mouseX - 210,mouseY) and mouseValue == "down":
                #print(mouseX,mouseY)
                remaining -= 0.5*dt
                i.value += 0.5*dt
                changed = True
    
        if changed:
            clear()
            for i in glasses:
                i.update()
            canvas.create_text(300, 50, text="LIQUID LEFT TO BE DISTRIBUTED: "+str(remaining), fill="black", font=('Helvetica 15 bold'))

        window.update()
    clear()
    for i in glasses:
        i.update()
    canvas.create_text(300, 50, text="Next Turn ", fill="black", font=('Helvetica 15 bold'))
    window.update()

def emptyGlasses():
    global glasses
    global mouseValue
    global mouseX
    global mouseY
    remaining = 2
    lastTime = time.time()


    waitingOnMouseReset = True
    while remaining > 0:
        if mouseValue == "up":
            waitingOnMouseReset = False
        newTime = time.time()
        dt = newTime - lastTime
        lastTime = newTime
        changed = False
        for i in glasses:
            if i.checkHitBox(mouseX - 210,mouseY) and mouseValue == "down" and not waitingOnMouseReset:
                #print(mouseX,mouseY)
                remaining -= 1
                i.value = 0
                changed = True
                waitingOnMouseReset = True
    
        if changed:
            clear()
            for i in glasses:
                i.update()
            canvas.create_text(300, 50, text="GLASSES LEFT TO BE EMPTIED: "+str(remaining), fill="black", font=('Helvetica 15 bold'))

        window.update()
    clear()
    for i in glasses:
        i.update()
    canvas.create_text(300, 50, text="Next Turn ", fill="black", font=('Helvetica 15 bold'))
    window.update()

        

        

def freePlay():
    global glasses
    global glassesEntry

    glasses = []

    
    for i in range(int(glassesEntry.get())):
        glasses.append(Glass(i))
    clear()
    for i in glasses:
        i.update()

    winCondition = False
    while not winCondition:
        fillGlasses()
        for i in glasses:
            if i.value > 1:
                winCondition = True
        if winCondition:
            break
        else:
            emptyGlasses()
        
    pass


def AIfillGlasses(turn):
    global glasses
    if turn == 0:
        for i in [0,2,4]:
            glasses[i].value += 1/6
    if turn == 1:
        remaining = 0.5
        for i in [0,2,4]:
            if glasses[i].value == 0:
                glasses[i].value += 5/18
                remaining -= 5/18
            else:
                glasses[i].value += 1/9
                remaining -= 1/9
        if remaining > 0:
            glasses[0].value += remaining
    if turn == 2:
        remaining = 0.5
        for i in [0,2,4]:
            if glasses[i].value != 0 and remaining > 0:
                glasses[i].value += 0.25
                remaining -= 0.25
    if turn == 3:
        for i in [0,2,4]:
            if glasses[i].value > 0.5:
                glasses[i].value += 0.5
                break
    clear()
    for i in glasses:
        i.update()
    canvas.create_text(300, 50, text="Your turn to empty glasses ", fill="black", font=('Helvetica 15 bold'))
    window.update()

def AIemptyGlasses(turn,n):
    global glasses
    if n <= 4:
        glasses[(2*turn)%n].value = 0
        glasses[(2*turn+1)%n].value = 0
    if n == 5:
        maximumNonAdj = 0
        maximumNonAdjPos = 0
        maximumValue = 0

        maximumPos = 0
        for i in range(n):
            if glasses[i].value + glasses[(i+2)%n].value > 0.5:
                if glasses[i].value + glasses[(i+1)%n].value > maximumNonAdj:
                    maximumNonAdj = glasses[i].value + glasses[(i+1)%n].value
                    maximumNonAdjPos = i
                if glasses[i].value + glasses[(i-1)%n].value > maximumNonAdj:
                    maximumNonAdj = glasses[i].value + glasses[(i-1)%n].value
                    maximumNonAdjPos = (i-1)%n
            if glasses[i].value + glasses[(i+1)%n].value > maximumValue:
                maximumValue = glasses[i].value + glasses[(i+1)%n].value
                maximumPos= i
        if maximumNonAdj > 0:
            glasses[maximumNonAdjPos].value = 0
            glasses[(maximumNonAdjPos+1)%n].value = 0

        else:
            glasses[maximumPos].value = 0
            glasses[(maximumPos+1)%n].value = 0

    clear()
    for i in glasses:
        i.update()
    canvas.create_text(300, 50, text="Your turn to fill glasses ", fill="black", font=('Helvetica 15 bold'))
    window.update()

    
        
def aiPlay():

    turn = 1

    global glasses
    global glassesEntry

    glasses = []
    
    n = int(glassesEntry.get())
    for i in range(n):
        glasses.append(Glass(i))
    clear()
    for i in glasses:
        i.update()
        
    winCondition = False
    while not winCondition:
        if n <= 5:
            
            fillGlasses()
            for i in glasses:
                if i.value > 1.0000001:
                    winCondition = False
            if winCondition:
                pass
            else:
                AIemptyGlasses(turn,n)
                turn += 1
        else:
            AIfillGlasses(turn)
            turn += 1
            for i in glasses:
                if i.value > 1.00000001:
                    winCondition = False
            if winCondition:
                pass
            else:
                emptyGlasses()
        
    pass

bounds = [-4,3,4,-3]

window = tkinter.Tk()
window.geometry("1000x600")

window.bind("<ButtonPress-1>", leftDown)

window.bind("<ButtonRelease-1>", leftUp)

window.bind("<Motion>", mouseMotion)


glassesButton = tkinter.Button(width = 28,text="Number of glasses:")
glassesButton.place(x=0,y=450)

glassesEntry = tkinter.Entry(width = 35)
glassesEntry.place(x=0,y=480)



freeplayButton = tkinter.Button(width = 28, command = freePlay,text="Free Play")
freeplayButton.place(x=0,y=510)

playAgainstComp = tkinter.Button(width = 28, command = aiPlay,text="Play against computer")
playAgainstComp.place(x=0,y=540)




def clear():
    global canvas
    try:
        canvas.destroy()
    except:
        pass
    canvas = tkinter.Canvas(width=800,height=600,bg='white')
    canvas.place(x=200,y=0)


        

clear()

while True:

    window.update()

