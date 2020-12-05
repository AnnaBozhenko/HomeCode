do_not_exit = True 
print("Лабораторна робота №2")
print('Tема: "Програмування циклічних алгоритмів"')
print("Виконала: Боженко А. О.")
print("Студент групи КМ-01")
while do_not_exit: # While do_not_exit is true the cycle acts
    try: # Start of the block, which counts sum of expressions
        n = int(input("Уведіть значення n:"))
        x = float(input("Уведіть значення x:"))
        sumof = 0 # The primer sum is zero
        for i in range(1, n+1): # 
            extract = float(i**2-x**2) # Count the expression
            sumof += extract # Sum the previous expression and the next one
            if i == 1: # Literate thing: if there is only one expression use singular
                print("Сума", i, "виразу i^2-x^2=", sumof)
            else: # Literate thing: in other cases use plural
                print("Сума", i, "виразів i^2-x^2=", sumof) 
            # End of the block, which counts expressions
        exit = "y"
        quest = input("Якщо бажаєте продовжити - натисніть 'x'. Бажаєте вийти - натисніть 'y'") # to continue or exit
        if quest == "y":
            do_not_exit = False # necessary result is given, so stop the cycle
    except ValueError: # Returning the message in case of false format
        print("Ви ввели хибний формат")
        exit = "y"
        quest = input("Якщо бажаєте продовжити - натисніть 'x'. Бажаєте вийти - натисніть 'y'") # to continue or exit
        if quest == "y":
            do_not_exit = False
