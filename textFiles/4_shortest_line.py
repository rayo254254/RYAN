with open('irish_song.txt') as file:
    line = file.readline()
    shortest = line.rstrip()

    while line:

        if len(line.rstrip()) < len(shortest):
            shortest = line.rstrip()
        line = file.readline()

print('The shortest line has', len(shortest), 'characters')
print(shortest)