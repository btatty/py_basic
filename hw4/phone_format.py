phone = input('Enter phone number: ')
out = ''
for char in phone:
    if char.isdigit():
        out += char

print(out)
