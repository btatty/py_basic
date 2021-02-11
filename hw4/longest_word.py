string = input('Введите строку: ')
count = 1
max_word = ''
word = ''
len_word = 0
if string == ' ':
    count == 0
    print('Пустая строка')
for char in string:
    if char.isalpha():
        word += char
    else:
        count += 1
        if len(word) > len_word:
            len_word = len(word)
            max_word = word
        word = ''

print('Количество слов: ', count)
print('Самое длинное слово в строке: ', max_word, len(max_word))

# isalpha method correct without split
