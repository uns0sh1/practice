num = int(input("Введите число: "))
res = 0
newNum = num
while newNum > 0:
    digit = newNum % 10
    res += digit**3
    newNum //= 10
if res == num:
    print("Число", num, "является числом Армстронга")
else:
    print("Число", num, "не является числом Армстронга")
