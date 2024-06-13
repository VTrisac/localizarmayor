numeros = [10, 5, 45, 89, 22, 3, 78, 12, 43, 67]
mayor = 0
for numero in numeros:
    if numero > mayor:
        mayor = numero
print("el número mayor de la lista es " + str(mayor))