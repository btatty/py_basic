phone = input('Enter phone number: ')
out = ''
i = phone.rfind('0')
if i != -1:
    phone = phone[(i - 1):]
for char in phone:
    if char.isdigit():
        out += char

print('38' + out)
