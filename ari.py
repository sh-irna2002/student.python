a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
print("choose any operation:")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
print("5. exponentation")
print("6. floor division")            
op=(int(input("enter the op number:")))
if op == 1:
    print("sum of two number:",a+b)
elif op == 2:
    print("difference of two number:",a-b)
elif op == 3:
    print("product of two number:",a*b)
elif op == 4:
    print("quatient of two number:",a/b)
elif op == 5:
    print("exponent of two number:",a**b)
elif op == 6:
    print("floor division of two number:",a//b)
else:
    print("invalid option")