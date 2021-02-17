def identical(obj_1, obj_2):
    if len(obj_1) == len(obj_2):
        for i in obj_1:
            if i in obj_2:
                obj_2.remove(i)
            else:
                return False
    else: 
        return False
    return True
        


def mix(l):
    from random import choice
    if type(l) == list:
        new_l = list()
        while len(l) != 0:
            cosa = choice(l)
            new_l.append(cosa)
            l.remove(cosa)
        return new_l


def prefix(multystr, prefix):
    bank = multystr.split('\n')
    bank = [prefix + ' ' + el for el in bank if bank.index(el) != len(bank) - 1]
    return '\n'.join(bank)


sample_text = '''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''


def del_indent(string):
    bank = ''
    white = 'w'
    for ind in range(len(string)):
        if string[ind] == '\n' and string[ind + 1] == ' ':
            bank = bank + '\n'
            white = 1
    
        if white != 'w' and ind + 1 < len(string):
            if string[ind + 1] == ' ':
                white += 1
                continue
            elif string[ind + 1] != ' ':
                white = 'w'
                continue
        bank = bank + string[ind]
    return bank

# permutations start

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

# print(permut(4))

# permutations end

def vise_versa(bank):
    '''
    bank: list with numbers;

    The function returns the changed bank-list. The amount of list should be even, so
    the pair of neigbour elements could change its places.
    '''
    if len(bank) % 2 == 0:
        new_bank = list()
        for ind in range(len(bank)):
            if bank[ind] % 2 == 0:
                new_bank.append(bank[ind + 1])
            else:
                new_bank.append(bank[ind - 1])
        return new_bank

# print(vise_versa([0,1,2,3,4,5, 9]))

def seq(n, el1 = 20, el2 = 21):
    bank = [el1, el2]
    ind = 0
    while ind <= n - 2:
        el = bank[ind + 1]/(bank[ind] + bank[ind]*bank[ind + 1])
        bank.append(el)
        ind += 1
    return (bank[-1], len(bank) - 1)

# print(seq(2021))

def add_dicts(*dicts):
    '''dicts: a tuple with dictionaries.

    Returns the concatenation of dictionaries''' 
    for ind in range(len(dicts)):
        if ind < len(dicts) - 1:
            next_dict = dicts[ind + 1]
            for key, value in next_dict.items():
                dicts[0][key] = value
        else:
            return dicts[0]

a = {1: 'a', 2: 'b'}
b = {3: 'c', 4: 'd'}
c = {5: 'r', 6: 'w'}
# print(add_dicts(a, b, c))

def numb_square(start, end):
    '''start: a number to start from;
    end: a number to end.

    Returns a dictionary with keys as range of numbers 
    from start to end and values as keys in square.
    '''
    return {key: key**2 for key in range(start, end + 1)}

# print(numb_square(1, 10))

def sum_items(dictionary):
    '''
    dictionary: a dictinary with numbers as keys and values.

    Returns False if dictinary has non-number type items.
    Returns the sum of all items in dictionary.
    '''
    # Checking if dictionary's items are numbers 
    for key, value in dictionary.items():
        if type(key) and type(value) not in (int, float):
            return False

    sum_items = 0
    for key, value in dictionary.items():
        sum_items += key + value
    return sum_items

# print(sum_items({1: 'j', 3: 4}))

import functools

def mult_items(dictionary):
    '''
    dictionary: a dictinary with numbers as keys and values.
   
    Returns False if dictinary has non-number type items.
    Returns the multiplicatin of all items in dictionary.
    '''
    items_bank = []
    # Checking if dictionary's items are numbers 
    for key, value in dictionary.items():
        if type(key) and type(value) not in (int, float):
            return False
        else:
            items_bank.append(key)
            items_bank.append(value)

    return functools.reduce(lambda a, b: a * b, items_bank)

# print(mult_items({1: 2, 3: -4}))

def remove_key(diction, key_remove):
    '''
    diction: a dictionary;
    key_remove: a key from dictionary
    
    Returns False if key_remove is not found in diction as a key.
    Returns a dictionary without a key (key_remove)
    '''
    if key_remove not in diction.keys():
        return False
    return {key: value for key, value in diction.items() if key != key_remove}


# print(remove_key({1: 2, 3: -4}, 0))

def map_dicts(list_1, list_2):
    '''
    list_1, list_2 : lists.

    Returns False if amount of elements in list_1 and list_2 is different.
    Returns a dictinary, created from lists, where keys are taken 
    from lists_1 and values from list_2.
    '''
    if len(list_1) != len(list_2):
        return False
    return {list_1[ind]: list_2[ind] for ind in range(len(list_1))}

# print(map_dicts([1, 2, 3], ['a', 'b', 'c']))

def word_number(name = 'w3d.py', word = 'def'):
    '''
    name: a string which is the name of file to read;
    word: a string which is a seeked word in a file.

    Prints out the amount of found seeked word. 
    '''
    with open(name) as text:
        w = 0
        for i in text:
            if word in i:
                w += 1
        # this function is not counted inside this file
        if __name__ == '__main__' and w != 0:
            w -= 1
        print(w)

def set_indent(text, line = 1, spaces = 3):
    '''
    text: a string; line, spaces: int numbers.

    Returns modified text with added indentation to the text's line.
    Indentation: amount of (spaces) whitspaces.
    '''
    text = text.split('\n', line)
    text[line - 1] = ' '* spaces + text[line - 1]
    return '\n'.join(text)


text = '''The weather is great
don't you think so?
I'm fond of your cakes.
Don't you mind I'll wrap
and bring some to my aunt?'''
# print(set_indent(text, 3, 4))

def list_of_dicts(n):
    '''
    n: int number of empty dictionaries to create;

    Returns th list with n empty dictionaries.
    '''
    return [dict() for i in range(n)]

# print(list_of_dicts(5))

def space_between(*elements):
    '''
    elements: a tuple of elements;

    Returns a list with elements from 
    given tuple, sepersted with spacecs.
    '''
    data = list()
    for el in elements:
        data += [el, ' ']
    return data[:-1]        
# print(space_between(1, 2, 3 , 5))



