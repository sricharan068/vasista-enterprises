d = {"key1": "value1"}

try:
    val = d["key2"]
except KeyError as e:
    print(e)
