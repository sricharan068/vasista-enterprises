def find_index(arr, x):
    return arr.index(x)


arr=tuple(map(int, input("Enter elements of tuple separated by space: ").split()))

# Take x input
x = int(input("Enter the value to find: "))
print(find_index(arr, x))
