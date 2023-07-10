dict_1 = {i: i for i in range(1, 11)}
dict_res = {x: y**3 for (x, y) in dict_1.items() if x % 2 == 0}
print(dict_res)
