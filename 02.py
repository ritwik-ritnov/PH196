import numpy as np 
x, h = np.linspace(0, 1, 101, retstep = True) 
y = x**2 
I = h/3*(y[0] + y[-1] + 4*sum(y[1:-1:2])+2*sum(y[2:-2:2])) 
print("Integral = ", I)
print(type(x))