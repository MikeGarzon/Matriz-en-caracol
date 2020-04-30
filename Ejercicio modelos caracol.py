# CREACION DE UNA MATRIZ n*n EN CARACOL
# Maicol Andres Garzon Fonseca
# 20172020011

tamaño = int(input("Ingrese el tamalo de la matríz cuadrada:"))

# Creando vector
matriz = [None] * tamaño

# Creando Matriz
for i in range(0, tamaño):
    matriz[i] = [None] * tamaño

# Creando variables auxiliares
numero = 1
posicion = 0
tope = tamaño - 1

# Creando automatizacion en while, acaba cuando tome todos los datos (n*n)
while (numero <= tamaño * tamaño):
    for i in range(posicion, tope + 1):  # For para llenar la matriz hacia la derecha
        matriz[posicion][i] = numero
        numero += 1
    for i in range(posicion + 1, tope + 1):  # For para llenar la matriz hacia abajo
        matriz[i][tope] = numero
        numero += 1
    for i in range(posicion, tope)[::-1]:  # For para llenar la matriz hacia la izquierda
        matriz[tope][i] = numero
        numero += 1
    for i in range(posicion + 1, tope)[::-1]:  # For para llenar la matriz hacia arriba
        matriz[i][posicion] = numero
        numero += 1
    # Reasignando datos para hacer el caracol interior
    posicion = posicion + 1
    tope = tope - 1

# Mostrando matriz en caracol
for i in range(len(matriz)):
    print()
    for j in range(len(matriz)):
        print(matriz[i][j], "\t", end="")
