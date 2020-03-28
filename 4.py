from random import randint
my_list = [randint(0, 100) for i in range(30)]

print (f"Исходный список:\n{my_list}")
print (f"Новый список:\n{[i for i in my_list if my_list.count(i) == 1]}")