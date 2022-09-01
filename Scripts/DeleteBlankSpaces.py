import csv

# se toman las lineas del archivo
with open('3.txt', 'r', encoding="utf8") as f:
    lines = f.readlines()

# borrar espacios
lines = [line.rstrip() + '\n' for line in lines]

# escribir las lineas en el archivo
with open('Test3.txt', 'w', encoding="utf8") as f:
    f.writelines(lines)