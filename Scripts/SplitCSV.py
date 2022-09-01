import csv

# Se divide el archivo en segmentos, cada uno de 350 000 lineas
csvfile = open('Data.csv', 'r', encoding="utf8").readlines()
filename = 1
for i in range(len(csvfile)):
    if i % 350000 == 0:
        open(str(filename) + '.csv', 'w+', encoding="utf8").writelines(csvfile[i:i+1000])
        filename += 1