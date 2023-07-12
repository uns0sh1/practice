import csv

start = int(input("Введите начальный год: "))
end = int(input("Введите конечный год: "))
if start > end:
    start, end = end, start
    print("Предупреждение! Начальный год должен быть меньше конечного. Значения были поменяны местами")
filename = "favourite_books.csv"

with open(filename, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    flag = False
    for row in reader:
        year = int(row["Year of release"])
        if start <= year <= end:
            flag = True
            print(row)
    if not flag:
        print("Не было найдено книг, выпущенных в указанный промежуток времени")
