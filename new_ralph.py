# Python Script: Root finding by Newton-Raphson Method

# Function
def f(x): 
    return x**3 - 2*x - 5

x, tol = eval(input('initial point, tolerance \n'))

while abs(f(x)) >= tol:
    dx = 0.01
    fpx = (f(x+dx)-f(x-dx))/(2*dx)  # Derivative
    x = x - f(x)/fpx
    print(x)

print ('Root = ', x)