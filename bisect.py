# Root finding: Bisection Method
def f(x): 
    return x**3 - 2*x - 5
a, b, tol = eval(input('Lower limit, upper limit, tol \n'))
while f(a)*f(b) > 0:
    print ('No root in this interval')
    break
while abs(b-a) >= tol:
    xm = 0.5*(a + b)
    if f(xm) == 0:
        print("Root = ", xm)
        break
    if f(a)*f(xm) < 0:
        b = xm # Left half
    else:
        a = xm # Right half
print ('Root = ', (a + b)*0.5)