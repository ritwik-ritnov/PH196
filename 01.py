import numpy as np 
x, h = np.linspace(0, 1, 101, retstep = True) 
y = x**2 
# I = 0.5 * h * (y[0] + y[-1] + 2*sum(y[1:-2])) 
# print("Integral =", I)
# print(x)
# print("h =",h)
print(y[-1])
print(x)
print(x[1:-1])