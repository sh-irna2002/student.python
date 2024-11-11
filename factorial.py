def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = factorial(n - 1)
        return n * result

n = int(input("Enter a number: "))
if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    fact = factorial(n)
    print(fact)
    