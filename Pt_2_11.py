a = int(input("Введите число А: "))
b = int(input("Введите число В: "))
res = 0
for i in range(a, b + 1):
    res += i
print(f'Сумма чисел между {a} и {b} равна {res}')
