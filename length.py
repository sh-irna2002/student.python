list1=[]
n=int(input("enter the number of element:"))
for i in range(0,n):
    element=input("enter the element")
    list1.appendS(element)
print(list1)
max=len(list1)
temp=list1[0]
for i in list1:
    if len(i)>max:
        max=len(i)
        temp=i
print("the word",temp,"with longest length is",max)            