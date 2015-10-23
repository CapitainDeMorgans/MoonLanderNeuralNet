import time
import tkinter as tk
timestep = .05
root = tk()

v = 0 
a = -1.6*timestep
x = 500
at = 0

def keyPress(event):
    at = 3
while True:
    thrust = False
    time.sleep(timestep)
    x+=v
    v+=a
    if x <0:
        break
    print("%.2f" % x,"%.2f" % abs(v),thrust)
    
    if thrust:
        v+=at
    at = 0
print('yo dead',v)