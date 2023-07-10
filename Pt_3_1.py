import functools
import random

length = int(input("Введите длину списка чисел: "))
numbers = [0] * length
print("Получившийся список чисел:")
for i in range(length):
    numbers[i] = random.randint(0, 1000)
    print(numbers[i], end=" ")
average = functools.reduce(lambda x, y: x+y, numbers)/len(numbers)
print("\nСреднее арифметическое списка чисел:", average)
