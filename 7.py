from itertools import count


def fact():
    n = 1
    for i in count(1):
        n *= i
        yield n


'''Если нужен факториал нуля'''
# print ("(0, 1)")

for el in enumerate(fact()):
    if el[0] < 16:
        print (el)
    else:
        break
