def str(string):
    if len(string) >= 3:
        if string[-3:] == "ing":
            new_string = string + "ly"
        else:
            new_string = string + "ing"
    else:
        return string
    return new_string

# print(str("intersting"))

def substitute(string):
    first = string[0]
    new_word = [first]
    for char in string[1:]:
        if char == first:
            new_word.extend("$")
        else:
            new_word.extend(char)
    new_word = "".join(new_word)
    return new_word

# print(substitute("infinity"))

def the_longest(list_words):
    max_length = 0
    for word in list_words:
        c = len(word)
        if c > max_length:
            max_length = c
    return max_length

# print(the_longest(["word", "sword", "heartbeatjkjt", "kingdom"]))

'''def list_numbers(string_with_numbers):
    list_numbers = string_with_numbers.split(" ")
    new_list = list()
    length = len(list_numbers)
    if length > 1:
        i = 0
        last = float(list_numbers[-1])
        current = float(list_numbers[i])
        first = float(list_numbers[0])
        prev = float(list_numbers[i - 1])
        following = float(list_numbers[i + 1])
        for i in range(length):
            if i == 0:
                new_list.extend(current + last)
            elif i == length - 1:
                new_list.extend(current + first)
            else:
                new_list.extend(prev + following)
            i += 1
        new_list = " ".join(new_list)
        return new_list
    else:
        return string_with_numbers'''

# print(list_numbers("1 2.5 34"))
   
def isempty(data):
    if data == []:
        return print("The list is empty")
    else:
        return print("The list is not empty")
# isempty([])

def copylist(data):
    new_l = data + []
    return new_l

'''old_list = [(2, 5), (2, 5), (4, 4)]
new_list = copylist(old_list)
new_list += [3]
print(old_list)
print(new_list)'''

def morethan(n, string):
    l = list()
    words = string.split(" ")
    for i in words:
        if len(i) > n:
            l.extend(i)
    return l

# print(morethan(2, "santa finds a so call to work"))

def same_arg(list1, list2):
    issame = False
    for i in list1:
        for j in list2:
            if i == j:
                issame = True
                return issame
    return issame

# print(same_arg((1, 3, 5, 8), ('d', 9, 4, 6)))
def remove045(list1):
    newlist = list1[1:4] + list1[6:]
    return newlist
# print(remove045(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))

def array():
    # 3x4x6
    list_xy = []
    list_xz = []
    list_yz = []
    global_list = []
    list_x = []
    list_y = []
    list_z = []
    x = 3
    y = 4
    z = 6
    xy = x*y
    xz = x*z
    yz = y*z
    i = 1
    while i <= z:
        j = 1
        while j <= xy:
            list_xy.extend("*")
            j += 1
        list_z.extend(list_xy)
        i += 1
    global_list.extend(list_z)
    i = 1
    while i <= y :
        j = 1
        while j <= xz:
            list_xz.extend("*")
            j += 1
        list_x.extend(list_xz)
        i += 1
    global_list.extend(list_x)
    i = 1
    while i <= x:
        j = 1
        while j <= yz:
            list_yz.extend("*")
            j += 1
        list_y.extend(list_yz)
        i += 1 
    global_list.extend(list_y)
    return global_list

# print(array())
       
