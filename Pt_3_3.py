value = int(input("Введите число: "))
res = lambda x: "Четное" if x % 2 == 0 else "Нечетное"
print(res(value))
