n = int(input("Enter a number:"))
ten = 10
digit = n
great_n = 0
while digit > 1 :
    digit = int((digit/ten - digit//ten)*10)
    ten *= 10
    if digit > great_n :
        great_n = digit
print("The greatest digit is :", great_n)
