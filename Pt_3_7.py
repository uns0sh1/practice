def check(n):
    if n in "аеёиоуыюяэaeyuio":
        return True
    return False


array = input("Введите строку: ")
array = array.replace(" ", "")
res = {array[i]: check(array[i]) for i in range(len(array))}
print(res)
