num = int(input("Введите число: "))
res = 0
while num < 0:
    res += num
    num = int(input("Введите число: "))
print("Получившийся результат:", res)
