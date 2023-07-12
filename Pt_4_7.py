from itertools import permutations
from random import randint

length = int(input("Введите длину списка: "))
array = [randint(0, 10) for x in range(length)]
print("Изначальный список:", array)
res = set(permutations(array))
print("Все возможные перестановки данного списка:")
for i in res:
    print(i)
