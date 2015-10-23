import time
import tkinter as tk
color = 'blue'
timestep = .005
w=1000
h=750
v = -1
a = -1.6*timestep
x = 500
at = 3*timestep
input = [0,0]
weights = [1,1]


# def keyPress(event):
#     global at
#     at = 3*timestep
#     global color
#     color = 'red'
# #     print('pressed')
#     
# def keyRelease(event):
#     global at
#     at = 0
#     print('unpressed')
#     global color
#     color = 'blue'
    
root = tk.Tk()

canvas = tk.Canvas(root, width=w, height=h)
# 
# canvas.bind_all('<KeyRelease>', keyRelease)
# canvas.bind_all('<Key>', keyPress)

canvas.pack()
def finalNeuron(input,weight,thresh)->bool:
    sum = 0
    for x in range(0,len(input)-1):
        sum += input[x]*weight[x]
    print(sum)
    return sum >= thresh
def ball(x,y,r):
    canvas.create_polygon(x-r/2,y,x+r/2,y,x,y-r,fill=color)
    
    
    
    
    
    
while True:
    canvas.delete("all")
    ball(w/2,h-x,50)
    
    time.sleep(timestep)
    x+=v
    v+=a
    v+=at
    input = [(h-x)/100,v]
    if finalNeuron(input,weights,4):
        color = 'red'
        at = 3*timestep
    else:
        color = 'blue'
        at = 0
    if x <0:
        break
    print("%.2f" % x,"%.2f" % v,)
    
    canvas.update()
if abs(v)<1:
    print('yo not dead',v)
else:
    print('yo dead',v)

root.mainloop()















