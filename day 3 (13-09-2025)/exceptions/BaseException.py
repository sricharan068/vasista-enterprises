try:
    raise BaseException("This is a BaseException")
except BaseException as e:
    print(e)
