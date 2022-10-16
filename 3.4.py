import math
p=float(input("Enter the value of p:"))
print(p)
r=float(input("Enter the value of r:"))
print(r)
n=float(input("Enter the value of n:"))
print(n)
t=float(input("Enter the value of t:"))
print(t)
cp= p*math.sqrt((1+(r/100*n)) ** (n*t))
print("The compound interest =",cp)

