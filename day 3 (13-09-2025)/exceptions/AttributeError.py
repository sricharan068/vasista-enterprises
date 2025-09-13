class MyClass:
    pass

obj = MyClass()

try:
    obj.some_attribute
except AttributeError as e:
    print(e)
