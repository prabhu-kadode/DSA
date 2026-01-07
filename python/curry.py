def outer(a):
    total=a
    def inner(b=None):
        nonlocal total
        if b is None:
            return total
        total+=b

        return inner
    return inner
print(outer(10)(20)())