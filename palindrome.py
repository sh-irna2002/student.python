def is_palindrome(n):
    n_rev = n[::-1]
    return n == n_rev

n = input("Enter a string: ")
if is_palindrome(n):
    print("Palindrome")
else:
    print("Not a palindrome")