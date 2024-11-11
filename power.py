def power(base,exponent):
    if exponent==0:
        return 1
    if exponent==1:
        return base
    else:
        return base*power(base,exponent-1)
base=int(input("enter the base"))
exponent=int(input("enter the exponent"))
result=power(base,exponent)
print(f"the power of {base} and {exponent} is {result}\n")    