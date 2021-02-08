string = 'Lorem, Ipsum, is, sImPlY, duMMy, TEXT, of, The, printing, INDUSTRY.'
uppers = 0
lowers = 0
if string.istitle():
    string = string[:] + 'done. '
else:
    string = string.replace(string[0:5], 'draft: ')

print(string)

if len(string) > 20:
    string = string.substring(0, 20)
else:
    string = string.ljust(20, '@')

print(string)

for char in string:
    if char.islower():
        lowers += 1
    elif char.isupper():
        uppers += 1
if lowers > uppers:
    string = string.lower()
elif lowers < uppers:
    string = string.upper()
elif lowers == uppers:
    string = string.swapcase()

print(lowers, uppers)
print(string)
