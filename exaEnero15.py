# PROBLEMA 1
# APARTADO A
def columna_equilibradas(matriz):
    contadorCeros = 0
    contadorUnos = 0

    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            if matriz[i,j] == 0:
                contadorCeros += 1
            elif matriz[i,j] == 1:
                contadorUnos += 1
        if contadorCeros != contadorUnos:
            return False
    return True 

# APARTADO B

def filas_con_tríos(matriz):
    candidato = 1
    lista = []

    for i in range(len(matriz)):
        for j in range(len(matriz)-1):
            if matriz[i][j] == matriz[i][j+1]:
                candidato += 1
            elif candidato >= 3 and i not in lista: 
                lista.append(i)
    return lista  
    
# APARTADO C

def columnas_repetidas(matriz,n):
    columnaUno = []
    columnasRepetidas = []

    for i in range(len(matriz)):
        columnaUno.append(matriz[i][n])

    for j in range(len(matriz[0])):
        columnaDos = []
        for i in range(len(matriz)):
            columnaDos.append(matriz[i][j])
        if columnaDos == columnaUno and n != j:
            columnasRepetidas.append(i)
        
    return columnasRepetidas

# PROBLEMA 2

# APARTADO A 

def mes_más_matriculaciones(fileName,tipo,provincias):
    meses = [0] * 12
    file = open(fileName, 'r', encoding='utf-8')
    linea = file.readline()

    while linea != "":
        coche = linea.split('|')

        for element in provincias:
            if element == coche[3] and coche[0] == tipo:
                meses[int(coche[5])-1] += 1
        
        linea = file.readline()

    mayor = 0
    for i in range(len(meses)):
        if meses[i] > mayor:
            mayor = meses[i]
            mes = i + 1 
    return mes

# APARTADO B