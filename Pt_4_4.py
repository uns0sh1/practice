from itertools import combinations
from random import randint

length = int(input("Введите длину списка чисел: "))
numlist = [randint(1, 10) for x in range(length)]
print("Список чисел:", numlist)

num = int(input("Введите число: "))
comb = []
res = []

if length > 0:
    for i in range(0, length + 1):
        comb += list(combinations(numlist, i))
    for value in comb:
        if sum(value) == num:
            res.append(value)
resfinal = list(set(res))
print("Уникальные комбинации чисел, сумма которых равна " + str(num) + ": " + str(resfinal))
