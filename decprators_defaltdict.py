def do_twice(func):
    def wrapper_do_twice(args):
        print("Start of executing...")
        func(args)
        print("End of executing.")
    return wrapper_do_twice

'''@do_twice
def say_hello(name):
    return print(f"Hello, {name}")

say_hello("Dereck")
print()

dict_1 = {}
print(f'The primer state: {dict_1}')
dict_1[1] = 'a'
print(f'The second state: {dict_1}')
print(f'Is not yet confirmed state: {dict_1.get(2,"b")}')
dict_1.setdefault(2, 'b')
print(f'Already confirmed 3rd state: {dict_1}')
# dict_1.redefault(2, 'c')
# print(f'The 4th state: {dict_1}')'''

letters_guessed = ajrdws
def get
