import csv

with open('3.csv', 'r', encoding="utf8") as inp, open('3.txt', 'w', encoding="utf8") as out:
    for line in inp:
        line = line.replace(';', ' ')
        out.write(line)