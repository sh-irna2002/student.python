a=int(input("enter the lower case"))
b=int(input("enter the upper case"))
for i in range(a,b+1):
    if i>1:
        for j in range(2,i-1):
            if i % j == 0:
                break
            else:
                print(i)