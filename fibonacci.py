def isfib(n):
    f0 = 0
    f1 = 1
    f = 0
    while True:
        if f == n:
            print(f'{n} is in fibonacci row')
            break
        if f > n:
            print(f'{n} is a stranger among fibs.')
            break
        f = f0 + f1
        f0 = f1
        f1 = f


def isfib1(n, f0 = 0, f1 = 1, f = 0):
    if f == n:
        return print(f'{n} is in fibonacci row')
    if f > n:
        return print(f'{n} is a stranger among fibs.')
    f = f0 + f1
    f0 = f1
    f1 = f
    return isfib1(n, f0, f1, f)

# isfib(13)

def findfib(n):
    f0 = 0
    f1 = 1
    f = 0
    for i in range(n):
        f = f0 + f1
        f0 = f1
        f1 = f 
    print(f1)

findfib(5)

    



