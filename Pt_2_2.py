shows = ["Импровизация", "Кухня", "След", "Касл"]
print("Список передач: ")
for i in shows:
    print(i)
newShow = input("Введите название новой передачи: ")
position = int(input("Введите позицию передачи (от 1 до 4): "))
shows.insert(position - 1, newShow)
print("Измененный список передач: ")
for i in shows:
    print(i)
