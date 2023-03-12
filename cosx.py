# Python Script: Cosine Series
import math
x, tol = eval(input('Angle in deg, tolerance: \n'))
# Converted to radian
x = x*math.pi/180
sum, term = 0.0, 1.0
n = 1
while abs(term) > tol:
    sum += term
    # term update
    term = term*(-x**2/(2*n*(2*n-1)))
    n += 1
print("Calculated Value =",sum,"\nActual Value =", math.cos(x))