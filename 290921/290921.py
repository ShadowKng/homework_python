def y(n):
    q = 2
    array = list()
    while q <= n:
        array.append(q)
        q += 2
    return array

def x(n):
    q = 1
    array = list()
    while q <= n:
        array.append(q)
        q += 1
    return array
print(y(50))
print(x(50))