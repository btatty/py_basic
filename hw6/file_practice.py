# 1.

file = open('file_practice.txt', 'w')
file.write('Starting practice with files' + '\n')
file.close()

# 2.

file = open('file_practice.txt', 'r')
print(file.read(5).upper())
file.seek(0)
print(file.read())
file.close()

# 3.

file = open('text.txt', 'r+')
print(file.read())
file.seek(0)
print(file.read().replace('e', 'i'))
file.close()

# 4.

file = open('file_practice.txt', 'r+')
if len(file.read()) % 2 == 0:
    print(file.write('the end.'))
else:
    print(file.write('bye!'))
file.close()

# 5.

file = open('file_practice.txt', 'r+')
file.insert(len(file) / 2, file)
file.seek(0)
print(file.read())
file.close()





