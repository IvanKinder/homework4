from itertools import count
from itertools import cycle


def cic_func(list):
    i = 0
    for el in cycle(list):
        print (el)
        i += 1
        if i > 100:
            if input("Для завершения программы введите Q или ENTER для продолжения! ").lower() == 'q':
                break
            elif input("Если желаете продолжить итерироваться введите Y, если нет введите что угодно.").lower() == 'y':
                i = 0
                continue
            else:
                if input(
                        "Если желаете просто итерироваться введите Y, если нет, введите что угодно.").lower() == 'y':
                    cic_func(input("Введите список, элементы которого будем повторять: "))


def iter_func():
    i = 0
    for el in count(int(input("С какого числа начнём итерироваться?\n"))):
        print (el)
        i += 1
        if i > 100:
            if input("Для завершения программы введите Q или ENTER для продолжения! ").lower() == 'q':
                break
            elif input("Если желаете продолжить итерироваться введите Y, если нет, введите что угодно.").lower() == 'y':
                i = 0
                continue
            else:
                if input(
                        "Если желаете итерироваться по списку введите Y, если нет, введите что угодно.").lower() == 'y':
                    cic_func(input("Введите список, элементы которого будем повторять: "))


try:
    iter_func()
except:
    print ("Необходимо вводить целые числа!!!")
