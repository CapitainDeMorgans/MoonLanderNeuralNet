import time
import tkinter as tk

timestep = .02
w=1000
h=750
v = 0
a = -1.6*timestep
x = 500
at = 3*timestep

def keyPress(event):
    global at
    at = 3*timestep
#     print('pressed')
    
def keyRelease(event):
    global at
    at = 0
    print('unpressed')
    
root = tk.Tk()

canvas = tk.Canvas(root, width=w, height=h)

canvas.bind_all('<KeyRelease>', keyRelease)
canvas.bind_all('<Key>', keyPress)

canvas.pack()
def ball(x,y,r):
    canvas.create_polygon(x-r/2,y,x+r/2,y,x,y-r,fill='blue')
while True:
    canvas.delete("all")
    ball(w/2,h-x,50)
    thrust = False
    time.sleep(timestep)
    x+=v
    v+=a
    v+=at
    if x <0:
        break
    print("%.2f" % x,"%.2f" % v,at)
    
    canvas.update()
if abs(v)<1:
    print('yo not dead',v)
else:
    print('yo dead',v)

root.mainloop()