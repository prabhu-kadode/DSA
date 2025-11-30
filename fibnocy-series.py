n = 10




        
def fib1(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b

def fib2(n):
    a = 0
    b = 1
    count = 2

    if n == 0:
        return 0
    if n == 1:
        return 1

    print(a, b)

    while count < n:
        c = a + b
        print(c)
        a = b
        b = c
        count += 1

# fib(5)




print(fib2(5))
