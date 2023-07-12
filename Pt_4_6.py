array = input("Введите строку английскими буквами: ")
rot = 13
res_array = ""

for i in range(len(array)):
    if array[i].isupper():
        letter = ord(array[i]) - 64
        if letter + rot <= 26:
            res_array += chr(letter + rot + 64)
        else:
            res_array += chr(letter + rot - 26 + 64)
    elif array[i].islower():
        letter = ord(array[i]) - 96
        if letter + rot <= 26:
            res_array += chr(letter + rot + 96)
        else:
            res_array += chr(letter + rot - 26 + 96)
    else:
        res_array += array[i]
print("Зашифрованная строка:", res_array)
