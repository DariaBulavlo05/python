string = 'Follow your heart'

char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Словарь с количеством вхождений каждой буквы:")
print(char_count)