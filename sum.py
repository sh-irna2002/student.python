def sum_of_first_n(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    return sum

num = int(input("Enter a number: "))
result = sum_of_first_n(num)
print("Sum of the first", num, "numbers is", result)