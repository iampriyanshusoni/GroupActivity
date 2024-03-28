import math
def triangle_area(a,b,c):
    s=(a+b+c)/2
    ar=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return ar
a=float(input("Enter first side:"))
b=float(input("Enter second side:"))
c=float(input("Enter third side:"))
area=triangle_area(a,b,c)
print("Area of traingle is: ",area)