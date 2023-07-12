import itertools

value = int(input("Введите число: "))
print(max([num for i in itertools.permutations(str(value)) if (num := int(''.join(i))) >= value]))
