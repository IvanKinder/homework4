from functools import reduce


def multiple(pre, nex):
    return pre * nex


my_list = [i for i in range(100, 1001) if i % 2 == 0]

print (reduce(multiple, my_list))
