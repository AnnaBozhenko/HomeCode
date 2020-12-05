n = int(input("Enter a positive int number: "))
if n < 0:
    raise Exception("Sorry, no negative numbers.")

@pascal()
def binomk(n):
    # Count the factorial of input number.
    n_fact = 1
    for number in range(n + 1):
        if number == 0:
            n_fact = number * n_fact + 1
        else:
            n_fact = number * n_fact
    i = 0
    c = 1
    # The l is a list where koefitients will be added.
    l = list()
    while i <= n:
        # Count the factorial of the current i.
        i_fact = 1
        for number in range(i + 1):
            if number == 0:
                i_fact = number * i_fact + 1
            else:
                i_fact = number * i_fact
        # Count the factorial of difference of n and i.
        subtr_ni = n - i
        subtr_ni_fact = 1
        for number in range(subtr_ni + 1):
            if number == 0:
                subtr_ni_fact = number * subtr_ni_fact + 1
            else:
                subtr_ni_fact = number * subtr_ni_fact
        # Count the koefitient formed with folowing formula.
        c = (n_fact)/((subtr_ni_fact) * i_fact)
        l = l + [int(c)]
        i += 1
    l = str(l)

    return l

def pascal(n):
    def wrapper(*args, **kwargs):
        i = 0
        while i <= n:
            yield binomk(*args, **kwargs)
            i += 1 
    return wrapper

pascal(3)