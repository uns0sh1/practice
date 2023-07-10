import math
value = int(input("Введите число: "))
if math.ceil(math.sqrt(value)) == math.sqrt(value):
    print("Первое натуральное число, квадрат которого больше введенного значения:", math.ceil(math.sqrt(value)) + 1)
else:
    print("Первое натуральное число, квадрат которого больше введенного значения:", math.ceil(math.sqrt(value)))
