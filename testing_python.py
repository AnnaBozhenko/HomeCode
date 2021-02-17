def n(q, p = 1):
    if p == q:
        return k(q)
    print(p)
    return n(q, p + 1)

def k(q):
    if q == 0:
        return q
    print(q)
    return k(q - 1)

num = 12377321

def ispolidrom(n):
    n = str(n)
    start = 0
    end = len(n) - 1
    while start <= len(n)//2:
        if n[start] == n[end]:
            start += 1
            end -= 1
            continue
        else:
            return False
    return True


def amount_polid(n):
    amount = 0
    while n != 0:
        if ispolidrom(n) == True:
            amount += 1
        n -= 1
    return amount

def equal_n():
    n = int(input('Enter: '))
    amount = 0
    while n != 0:
        current = n
        n = int(input('Enter: '))
        if n == current:
            amount += 1
    print(amount) 

def monoton():
    pass

while True:
    monoton()
    wish = input('Wish to continue (y/n)?')
    if wish == 'n':
        break

