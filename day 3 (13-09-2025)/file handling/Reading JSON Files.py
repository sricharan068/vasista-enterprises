import json
with open("sample1.json", "r") as jsonfile:
    data = json.load(jsonfile)
    print(data)
