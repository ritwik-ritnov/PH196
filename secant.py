# Root finding: Secant Method
def f(x): 
    return x**3 - 2*x - 5
x0, x1, tol = eval(input('x0, x1, tol \n'))
while abs(f(x1)) >= tol:
    x2 = x1-f(x1)*(x1-x0)/(f(x1)-f(x0))
# Swapping x-coordinates
    x0, x1 = x1, x2
    print ("x1 =",x1, "f(x1) =",f(x1))
print ('Root = ', x1)