# 1.

with open("file_practice.txt", "w") as f:
    print("Starting practice with files", file=f)

# 2.

with open("file_practice.txt") as f:
    print(f.read(5).upper())
    f.seek(0)
    print(f.read())

# 3.

with open("text.txt") as f:
    text = f.read()
    if text.count("i") > text.count("e"):
        text = text.replace("i", "e")
    else:
        text = text.replace("e", "i")

with open("file_practice.txt", "a") as f:
    f.write(text)

# 4.

with open("file_practice.txt", "a+") as f:
    f.seek(0)
    text = f.read()
    if len(text) % 2 == 0:
        f.write("the end")
    else:
        f.write("bye")

    f.seek(0)
    print(f.read())

# 5.

with open("file_practice.txt", "r+") as f:
    text = f.read()
    f.seek(0)
    center = len(text) // 2
    text = text[:center] + "*some inserted text*" + text[center:]
    f.write(text)





