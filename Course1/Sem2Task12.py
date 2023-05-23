import math
s = int(input('The sum of two numbers: '))
n = int(input('The multiplication of two numbers: '))
x = (s - (math.sqrt(s**2-4*n)))/2
y = s - x
print (y,x)