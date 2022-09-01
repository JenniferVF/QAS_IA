# variables
values = list("abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 \n")
alphanumeric = ""
newLines = []

# se abre el archivo
with open('Test3.txt', 'r', encoding="utf8") as f:
    lines = f.readlines()

# se eliminan los caracteres que no se encuentren en la lista "values"
for line in lines:
    for character in line:
        if character in values:
            alphanumeric += character
    newLines.append(alphanumeric)
    alphanumeric = ""

# escribir las lineas nuevas en el archivo de salida
with open('Listo3.txt', 'w', encoding="utf8") as f:
    f.writelines(newLines)