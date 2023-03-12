import numpy as np 
x, h = np.linspace(0, 1, 101, retstep = True) 
m = x.tolist()
y = x**2
I = y[0] + y[-1]
def f(x):
    return x**2
    
for i in range(1,101):
    o = i*h
    if i%3==0:
        I = I + 2*y[3:-1:3]
    else:
        I = I + 3*f(o)
I = I*3*h/8
# I = y[3]
# print(h)
# print(x)
print("Integral = ", I)

# print(y[1:-1:2])all()
