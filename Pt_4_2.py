def palindrome(n):
    if n == n[::-1]:
        return True
    return False


array = input("Введите строку: ")
res = set()

for i in range(len(array)):
    for j in range(i+1, len(array)+1):
        if palindrome(array[i:j]):
            res.add(array[i:j])

print("Найденные палиндромы:", res)
