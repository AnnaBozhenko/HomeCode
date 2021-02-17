def gcd1(n1, n2):
    '''
    n1, n2: numbers;

    Returns the GCD of n1 and n2.
    '''
    if n1 > n2:
        N = n1
        n = n2
    else:
        N = n2
        n = n1
    calcul = True
    while calcul:
        rest = N % n
        if rest == 0:
            break 
        N = n
        n = rest
    return n

# print(gcd1(24, 24)) 

def greater(n1, n2):
    '''
    n1, n2 : numbers;

    Returns bigger number of n1 and n2 
    or n1 if n1 equals to n2.
    '''
    if n1 >= n2:
        return n1
    else:
        return n2


def less(n1, n2):
    '''
    n1, n2 : numbers;

    Returns less number of n1 and n2 
    or n1 if n1 equals to n2.
    '''
    if n1 <= n2:
        return n1
    else:
        return n2

def gcd2 (N, n):
    '''
    N - bigger number, n - less number;

    Returns the GCD with recursive approach.
    '''
    if N % n == 0:
        return n 
    else:
        return gcd2(n, N % n)
    
def wrapper(n1, n2):
    '''
    n1, n2: numbers;

    Filters arguments to place them to the gcd2
    function and gives the result of gcd2 function.

    '''
    N = greater(n1, n2)
    n = less(n1, n2)
    return gcd2(N, n)

# print(wrapper(12, 124))


def faster(func1, func2):
    import time
    start_func1 = time.perf_counter()
    func1(134, 62)
    end_func1 = time.perf_counter()
    period_func1 = end_func1 - start_func1

    start_func2 = time.perf_counter()
    func2(134, 62)
    end_func2 = time.perf_counter()
    period_func2 = end_func2 - start_func2

    if period_func1 < period_func2:
        print(f'{func1.__name__} : {period_func1}')
    else:
        print(f'{func2.__name__}: {period_func2}')

faster(gcd1, gcd2)

def exe_time(func):
    '''
    func: function without parameters;

    Returs the time of executing the func.
    '''
    import time
    start_func = time.perf_counter()
    func()
    end_func = time.perf_counter()
    return end_func - start_func



