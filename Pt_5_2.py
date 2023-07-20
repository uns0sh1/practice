import csv

filename = "favourite_books.csv"
amount = int(input("Сколько записей вы хотите добавить в список?\n"))
for i in range(amount):
    print("Запись №" + str(i + 1))
    book = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = input("Введите год выпуска книги: ")
    row = [book, author, year]
    with open(filename, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row)
    print("Запись добавлена!")

name = input("Введите автора для поиска его книг в списке: ")
with open(filename, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    flag = False
    for row in reader:
        if name in row["Author"]:
            flag = True
            print(row)
    if not flag:
        print("Не было найдено ни одной книги указанного вами автора")
