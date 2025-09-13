my_list = [1, 2, 3]

try:
    element = my_list[5]
except IndexError as e:
    print(e)
