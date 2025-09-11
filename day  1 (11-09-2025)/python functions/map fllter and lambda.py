a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)
c = map(lambda x: x * 2, b)
print(list(c))
