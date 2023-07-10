a = int(input("Введите левую границу списка: "))
b = int(input("Введите правую границу списка: "))
if a > b:
    a, b = b, a
print([x**2 for x in range(a, b + 1)])
