def is_palindrome_num(n):
    original = n
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10

    return rev == original


print(is_palindrome_num(12321))  # True
print(is_palindrome_num(12345))  # False
