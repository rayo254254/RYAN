letters = []
text = input('Enter a text: ')

for i in range(len(text)):
    if text[i] != ' ': # and not text[i] in letters:
        letters.append(text[i])

letters.sort() # sort List of letters

print(letters)
print()

print(*letters)
print()

for character in letters:
    print(character, '\t', end='')
