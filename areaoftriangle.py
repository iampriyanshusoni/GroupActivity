import math
def triangle_area(a,b,c):
    s=(a+b+c)/2
    ar=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return ar

def calculate_rectangle_area(width, height): 
    if width > 0 and height > 0: 
        return width * height
    else:
        return 0



a=float(input("Enter first side:"))
b=float(input("Enter second side:"))
c=float(input("Enter third side:"))
area=triangle_area(a,b,c)
print("Area of traingle is: ",area)