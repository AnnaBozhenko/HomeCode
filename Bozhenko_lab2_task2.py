do_not_exit = True
print("Лабораторна робота №2")
print('Tема: "Програмування циклічних алгоритмів"')
print("Виконала: Боженко А. О.")
print("Студент групи КМ-01")
while do_not_exit:
    try:
        n =  int(input("Уведіть натуральне число:"))
        while n < 0:
            print("Ви ввели від'ємне число. Спробуйте ще раз")
            n =  int(input("Уведіть натуральне число:"))
        amount = 0
        mnozh = 10
        if n%2 == 0:
            amount = 1
        while n>10 :
            n = n//mnozh
            mnozh *=10
            if n%2==0:
                amount +=1
        print("Кількість парних цифр в числі :", amount, sep=" ")
        a = "y"
        quest = input("Бажаєте продовжити - натисніть будь - яку літеру. Бажаєте завершити - натисніть 'y'.")
        if quest == a:
            do_not_exit = False
    except ValueError:
        print("Ви ввели хибний формат")
        a = "y"
        quest = input("Бажаєте продовжити - натисніть будь - яку літеру. Бажаєте завершити - натисніть 'y'.")
        if quest == a:
            do_not_exit = False

