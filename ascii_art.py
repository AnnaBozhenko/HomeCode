def floor(a):
    return int(a) + 1


def column(row, col):
    for r in range(row):
        for c in range(col):
            if c % 2 == 0:
                print(r'/|/ ', end = '')
            else:
                print(r'\|\ ', end = '')
        print()

# column(5, 5)

def rhombs(row, col):
    print('.', '--' * col, '.', sep = '') 

    for r in range(row):
        print(r'|', end = '')
        for c in range(col):
            
            if c % 2 == 0:
                print(r'\\', end = '')
            else:
                print(r'//', end = '')
        print(r'|')           

    print('.', '--' * col, '.', sep = '') 

# rhombs(5, 5)

from w3d import word_number
word_number('ascii_art.py')