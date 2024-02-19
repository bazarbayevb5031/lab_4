def squares(n):
    for i in range(n+1):
        yield i * i
def even_n(n):
    return (x for x in range(0, n+1, 2))
def div_3_a4(n):
    return (x for x in range(n+1) if x % 3 == 0 and x % 4 == 0)
def squares(a, b):
    for i in range(a, b+1):
        yield i * i
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
