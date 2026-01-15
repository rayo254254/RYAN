names = []
distances = []
print('Enter your name and the distance to school.')
print('Type stop when you want to close the entry.')

name = input('Your name: ')  # priming read
while name != 'stop':
    distance = float(input('Distance to school: ')) # only ask distance if name is not 'stop'
    names.append(name)
    distances.append(distance)   # indices of both list are the same to keep track
    name = input('Your name: ')  # modifying read

#print lists and conclusions
if len(names) != 0:
    print('Overview')
    for i in range(len(names)):
        print(names[i], '\t', distances[i])
    max = max(distances)
    print(names[distances.index(max)], 'lives farthest, namely', max, 'km') # find student who lives the farest
    print('The average distance is', sum(distances)/len(distances))


