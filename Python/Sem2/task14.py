# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# Пример:

# 10 -> 1 2 4 8


n = int(input("Введите число n : "))
count = 1
while count <= n:
    print(str(count) + ' ')
    count = count * 2