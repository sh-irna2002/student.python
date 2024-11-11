num=int(input("enter the number of student:"))
name=[]
for i in range(0,num):
    nam=input("enetr student name")
    name.append(nam)
print("\nname in the list",name)
name.sort()
print("\nalphabetic order name list",name)
    