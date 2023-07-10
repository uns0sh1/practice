import random

counterW = 0
counterL = 0
while counterL < 3:
    option = int(input("Введите 0, если хотите выбрать орла, или 1, если хотите выбрать решку: "))
    if option != 0 and option != 1:
        break
    value = random.randint(0, 1)
    if value == option:
        counterW += 1
        print("Вы угадали! На данный момент у вас " + str(counterW) + " побед и " + str(counterL) + " поражений")
    else:
        counterL += 1
        print("Вы не угадали! На данный момент у вас " + str(counterW) + " побед и " + str(counterL) + " поражений")
print("Конец игры! Спасибо за участие!")
