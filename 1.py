from sys import argv

script_name, work_hours, rub_hour, gift = argv
try:
    print (f"Заработная плата сотрудника: {float(work_hours) * float(rub_hour) + float(gift)}")
except:
    print ("Вводите числа!!!")