"""
Требуется вывести все целые степени двойки (т.е. числа
вида 2k), не превосходящие числа N.
10 -> 1 2 4 8
"""

n = int(input('Введите число N: '))
degree = 1
print(f'{n} ->', end=" ")
while degree < n:
    print(degree, end=" ")
    degree *= 2
