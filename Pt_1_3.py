array = [int(input("Введите число А: ")), int(input("Введите число B: ")), int(input("Введите число C: "))]
print("Наибольшее число - ", max(array), "\nЧисла в порядке убывания: ", sorted(array)[::-1])
