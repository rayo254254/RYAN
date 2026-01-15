with open('textFiles/weather_2018 08.csv', encoding='UTF-8') as file:
    line=file.readline()
    highest=line
    while line:
        record=line.split(';')
        if record[1]>highest:
            highest=record[1]
        else:
            record[1]=highest
        line=file.readline()
print('tHE HIGHEST TEMPERATURE IN THIS PERIOD IS',record[highest].rstrip(),'DEGREES')











