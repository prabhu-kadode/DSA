def fact(n):
    if n<0:
        return ValueError("o Is not allowed")
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(-1))