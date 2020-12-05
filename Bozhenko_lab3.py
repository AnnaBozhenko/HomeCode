do_not_exit = True
print("Лабораторна робота №3")
print('Tема: "Рядки"')
print("Виконала: Боженко А. О.")
print("Студент групи КМ-01")
while do_not_exit:
        first_w = input("Увведіть перше слово:")
        sec_w = input("Увведіть друге слово:")
        length_sec = len(sec_w)
        if (first_w[0] == "a" or first_w[0] =="A") and (sec_w[length_sec-1] =="z"):
            print("Порядок слів змінений:", sec_w, first_w)
        else:
            print("Без змін")
        a = "y"
        quest = input("Бажаєте протовжити роботу програми - натисніть 'х', бажаєте завершити - натисніть 'у'")
        if quest == a:
            do_not_exit = False
    