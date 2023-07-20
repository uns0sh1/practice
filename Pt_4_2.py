def palindrome(n):
    if n == n[::-1] and len(n) != 1:
        return True
    return False


array = input("Введите строку: ")
res = set()

for i in range(len(array)):
    for j in range(i + 1, len(array) + 1):
        if palindrome(array[i:j]):
            res.add(array[i:j])

if len(res) == 0:
    print("Не найдено ни одного палинидрома")
else:
    print("Найденные палиндромы:", res)
