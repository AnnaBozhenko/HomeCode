# Permutation programme
    
def fact(n):
    '''
    n - integer positive number or zero;
    Returns the factorial of n.
    '''
    if n ==  0 or n == 1:
        return 1
    return fact(n - 1) * n


def make_list(data):
    '''
    data: any object

    If data is not list the function returns a 
    list with data, if data is a list the data is returned.
    '''
    if type(data) != list:
        return [data]
    return data


def bigger_less(n, bank):
    '''
    n - integer number;
    bank - list of sorted integer numbers;

    The function searches bigger number from n in bank if n is not maximum,
    otherwise (if n is maximum) it returns the minimum number from bank.
    '''
    if n == max(bank):
        return min(bank)
    else:
        for digit in bank:
            if digit > n:
                return digit


def same(data):
    '''
    data: a list with numbers.

    The function returns True if at least a number in 
    data-list is not unique, otherwise - False.
    '''
    for digit in data:
        ecxept_digit = data + []
        ecxept_digit.remove(digit)
        if digit in ecxept_digit:
            return True
    return False


def function(comby):
    '''
    comby - list;
    
    The function returns the list with int numbers 
    combination that is different from comby list.
    '''
    pattern = comby + []
    ind = 0
    base = sorted(comby) # a data to take and put into pattern
    while pattern == comby or same(pattern):
        char_change = bigger_less(comby[ind], base)
        pattern[ind] = char_change
        ind += 1
    return pattern


def permut(n):
    ''' 
    n - int number bigger than 1;

    Returns the list with unique combinations 
    of sequence: [1, 2, ... n - 1, n]
    '''
    combyns = [list(range(1, n + 1))] # a basic combynation - [1, 2, ... n - 1, n]
    for i in range(fact(n) - 1):
        pattern = combyns[-1]
        boundary = -2 # a first index of the second part
        while pattern in combyns:
            part_1 = make_list(pattern[0: boundary])
            part_2 = function(pattern[boundary:])
            pattern = part_1 + part_2
            boundary -= 1
        combyns.append(pattern)
    return combyns
