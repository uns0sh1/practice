def isprime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


a = int(input("Введите левую границу списка: "))
b = int(input("Введите правую границу списка: "))
if a > b:
    a, b = b, a
print([x for x in range(a, b + 1) if isprime(x)])
