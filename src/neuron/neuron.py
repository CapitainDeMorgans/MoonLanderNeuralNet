import time
import tkinter as tk

timestep = .02
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

canvas = tk.Canvas(root, width=100, height=100)

canvas.bind_all('<KeyRelease>', keyRelease)
canvas.bind_all('<Key>', keyPress)

canvas.pack()

while True:
    canvas.delete("all")
    thrust = False
    time.sleep(timestep)
    x+=v
    v+=a
    v+=at
    if x <0:
        break
    print("%.2f" % x,"%.2f" % abs(v),at)
    
    canvas.update()
print('yo dead',v)

root.mainloop()