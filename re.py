a=input("enter a string:")
first_char=a[0]
modified_string=first_char + a[1:].replace (first_char,'$')
print("modified string",modified_string)