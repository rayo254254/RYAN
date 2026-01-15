with open('books.txt') as file:

    line = file.readline()
    linecounter = 1
    
    while line:
        linecounter += 1        
        author = file.readline()
        print(str(linecounter) + ".", line.rstrip(), '->', author.rstrip())
        line = file.readline()
        