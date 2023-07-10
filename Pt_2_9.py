value = int(input("Введите число: "))
mas = [int(a) for a in str(value)]
print("Порядковый номер наибольшей цифры с начала числа:", mas.index(max(mas))+1)
mas.reverse()
print("Порядковый номер наибольшей цифры с конца числа:", mas.index(max(mas))+1)
