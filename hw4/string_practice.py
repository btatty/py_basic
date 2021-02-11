string = 'Lorem, Ipsum, is, sImPlY, duMMy, TEXT, of, The, printing, INDUSTRY.'

string = string.replace(', ', ' ')
print(string)
print(string.rfind('s'))
print(string.count('i') + string.count('I'))
index_s = string.find('sImPlY duMMy TEXT')
index_f = string.rfind('sImPlY duMMy TEXT')
print(string[index_s:index_s + index_f + 2])
print(string[0:len(string) // 2] * 3 + string[len(string) // 2:])
