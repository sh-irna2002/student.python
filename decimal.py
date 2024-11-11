binary=input("enter a binary number:")
decimal=0
for char in binary:
    decimal=decimal * 2 + int(char)
print("decimal equivalent:",decimal)    