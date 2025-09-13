lines = ["Line A", "Line B", "Line C"]
text = "\n".join(lines) + "\n"
with open("file2.txt", "w", encoding="utf-8") as f:
    f.write(text)

with open("file2.txt", "r", encoding="utf-8") as f:
    print(f.read())
