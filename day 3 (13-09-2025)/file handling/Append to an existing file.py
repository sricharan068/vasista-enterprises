with open("file.txt", "a", encoding="utf-8") as f:
    f.write("Appended line.\n")

with open("file.txt", "r", encoding="utf-8") as f:
    print(f.read())
