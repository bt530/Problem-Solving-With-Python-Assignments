import tkinter
import math

global canvas
global bounds
global codeBox




def run():
    global codeBox

    clear()
    print(codeBox.get("1.0", "end-1c"))
    exec(codeBox.get("1.0", "end-1c"))
    pass

def zOut():
    global bounds
    bounds = [i*1.1 for i in bounds]

    run()

def zIn():
    global bounds
    bounds = [i/1.1 for i in bounds]

    run()

bounds = [-4,3,4,-3]

window = tkinter.Tk()
window.geometry("1000x700")


codeBox = tkinter.Text(width = 200,height = 20)
codeBox.place(x=0,y=600)

runButton = tkinter.Button(width = 28, command = run,text="Run")
runButton.place(x=0,y=570)

zoomInButton = tkinter.Button(width = 28, command = zIn,text="Zoom In")
zoomInButton.place(x=0,y=510)

zoomOutButton = tkinter.Button(width = 28, command = zOut,text="Zoom Out")
zoomOutButton.place(x=0,y=540)


def clear():
    global canvas
    try:
        canvas.destroy()
    except:
        pass
    canvas = tkinter.Canvas(width=800,height=600,bg='black')
    canvas.place(x=200,y=0)




def add(value):
    global canvas
    global bounds

    try:
        value = int(value)
    except:
        return

    if value <= 0:
        return
    #stuck - how do we map a value to its 2d position in the spiral
    #aha - odd squares will always be at the bottom right corner of a square
    #centered on 1 (and even squares will be at the top left one above the diagonal

    root = math.sqrt(value)

    floor = math.floor(root)
    ceil = math.ceil(root)

    if ceil - root < 0.5:
        closestSquare = ceil
    else:
        closestSquare = floor


    if closestSquare % 2 == 1:#case closest to an odd square in bottom right
        x = (closestSquare - 1)/2
        y = -x
        if root > closestSquare:
            x += 1
            y += value - closestSquare ** 2 - 1
        else:
            x -= closestSquare ** 2 - value

    if closestSquare % 2 == 0:#case closest to an even square in top left
        x = -(closestSquare)/2 + 1
        y = -x + 1
        if root > closestSquare:
            x -= 1
            y -= value - closestSquare ** 2 - 1
        else:
            x += closestSquare ** 2 - value


    if x+0.5 >= bounds[0] and x-0.5 <= bounds[2] and y - 0.5 <= bounds[1] and y+0.5 >= bounds[3]:
        localTop = 600 - (y+0.5 - bounds[3])/(bounds[1]-bounds[3])*600
        localBottom = 600 - (y-0.5 - bounds[3])/(bounds[1]-bounds[3])*600

        localLeft = (x-0.5 - bounds[0])/(bounds[2]-bounds[0])*800
        localRight = (x+0.5 - bounds[0])/(bounds[2]-bounds[0])*800

        if abs(localTop - localBottom) <= 1:
            localTop = localBottom + 2

        if abs(localLeft - localRight) <= 1:
            localLeft = localRight - 2


        canvas.create_rectangle(localLeft,localTop,localRight,localBottom,fill="white",outline="white")
        
        

clear()


window.mainloop()
