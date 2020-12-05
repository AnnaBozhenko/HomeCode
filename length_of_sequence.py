# This programme is for counting medium value of sequence values. To stop entering type '0'.

def medium(*sequence):
    sum_n = 0
    counter = 0
    for el in sequence:
        sum_n += el
        counter += 1
    return sum_n/counter

# Testing
# print(f'Medium value: {medium(1, 2, 3, 4)}')

# define if colors of chess board squares are same.

def chess_board(x1, y1, x2, y2):
    if (x1 + y1) % 2 == (x2 + y2) % 2:
        return print("Yes, same colors.")
    else:
        return print("No, colors are different.")

# Testing   
# chess_board(1, 2, 2, 3)

def log2(number):
    if number < 1:
        return "Input must be more than 0"
    k =  0
    log2 = 0
    while log2 < number:
        log2 = 2**k 
        k += 1
    return k
    
# Testing
print(log2(5))






