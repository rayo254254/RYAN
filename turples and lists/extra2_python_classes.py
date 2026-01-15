python_classes=[['1ITFA', 35]]  # a List of lists was given as start value

total = python_classes[0][1]    # total starts with the number 35 given for '1ITFA'

for asci in range(ord('B'), ord('B')+7):  # ASCII value from 'B' to 'H'
     number = int(input ('Number of students in 1ITF' + chr(asci) + ': '))
     python_classes.append(['1ITF' + chr(asci), number])
     total += number

print(*python_classes, sep="\n")
print(total, 'students follow the Python course.')
