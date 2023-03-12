# Python Script: Exponential Series
import math
x, tol = eval(input('Enter x and tolerance (Use Comma):\n'))
sum, term = 0.0, 1.0
n = 1
while abs(term) > tol:
    sum += term
    term = term*x/n
    n += 1
print('Calculated Value =',sum,"\nActual value =",math.exp(x) )
