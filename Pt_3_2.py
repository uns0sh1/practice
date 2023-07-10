import functools
value = int(input("Введите число: "))
length = 0
n, m = 0, 1
while m < value:
    length += 1
    n, m = m, m + n

fib = functools.reduce(lambda y, _: y + [y[-1] + y[-2]], range(length - 1), [0, 1])
print(fib)
