print("...Area and Perimeter of Rectangle...")
l=int(input("enter the length of the rectangle : "))
b=int(input("enter the breadth of the rectangle : "))
area=lambda l,b : l*b
print("Area of the given rectangle is : ",area(l,b))
perimeter=lambda l,b : 2*(l+b)
print("Perimeter of the given rectangle is : ",perimeter(l,b))
print("...Area and Perimeter of Square...")
a=int(input("enter the length of the square : "))
area=lambda a : a*a
print("Area of the given square is : ",area(a))
perimeter=lambda a : 4*a
print("Perimeter of the given square is : ",perimeter(a))
