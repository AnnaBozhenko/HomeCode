# Permutation programmes

    
def fact(n):
    if n ==  0 or n == 1:
        return 1
    return fact(n - 1) * n


def g(number, pattern):
    combin_1 = [pattern]
    for i in range(number - 1):
        part = combin_1[i][1:] + [combin_1[i][0]]
        combin_1.append(part)
    combin_2 = [[pattern[i] for i in range(len(pattern) - 1, -1, -1)]]
    for i in range(number - 1):
        part = combin_2[i][1:] + [combin_2[i][0]]
        combin_2.append(part)
    return combin_1 + combin_2


def permutations(number):
    pattern = list(range(1, number + 1))
    pattern_list = [pattern]
    comb_list = list()
    num = -2
    while pattern[num] != pattern[0]:
        patt = pattern[num:]
        for part in g(num * -1, patt):
            first_part = pattern[:num]
            if first_part == int:
                pattern_list.append([first_part] + part)
            else:
                pattern_list.append(first_part + part)
        num -= 1

    for el in pattern_list:
        for comb in g(number, el):
            comb_list.append(comb)

    for i in range(len(comb_list)):
        comb_list[i] = tuple(comb_list[i])
    comb_list = set(comb_list)

    return comb_list
    
print(len(permutations(2))) 
print(len(permutations(3))) 
print(len(permutations(6))) 


