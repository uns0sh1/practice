dict_1 = {i: i for i in range(1, 11)}
dict_res = {x: y**2 for (x, y) in dict_1.items()}
print(dict_res)
