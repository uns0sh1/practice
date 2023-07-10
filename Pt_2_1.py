import random

colors = ["red", "blue", "green", "yellow", "purple"]
print("Доступные цвета в списке: ")
for i in range(len(colors)):
    print((i+1), colors[i])

optionProg = random.randint(1, len(colors))
optionUser = int(input("Введите номер цвета: "))
while optionProg != optionUser:
    if optionProg == 1:
        print("Повторите попытку! Загаданный цвет является первым цветом радуги")
    if optionProg == 2:
        print("Повторите попытку! Загаданный цвет зачастую ассоциируют с морем")
    if optionProg == 3:
        print("Повторите попытку! Загаданный цвет зачастую ассоциируют с природой")
    if optionProg == 4:
        print("Повторите попытку! Загаданный цвет зачастую ассоциируют с солнцем")
    if optionProg == 5:
        print("Повторите попытку! Загаданный цвет зачастую ассоциируют с фиалками")
    optionUser = int(input("Введите номер цвета: "))
print("Отлично!")
