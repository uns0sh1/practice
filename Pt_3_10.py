array = input("Введите строку: ")
array = array.replace(" ", "")
dict1 = {i: array[i] for i in range(len(array))}
dict_res = {x: array.count(x) for x in dict1.values()}
print(dict_res)
