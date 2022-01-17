# PROBLEMA1 

from re import A

# PROBLEMA !

# APARTADO A

def ganador_etapa(matriz, n):
    ganador = None
    for i in range(len(matriz)):
        if matriz[i][n] != None:
            ganador = matriz[0][n]
            break

    if ganador != None:
        for i in range(len(matriz)):
            if matriz[i][n] != None:
                if matriz[i][n] < ganador:                       
                    ganador = matriz[i][n]
        return ganador 

# APARTADO B 
def ganador_competición(matriz):
    lista_corredores = [0] * len(matriz)

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] != None:
                lista_corredores[i] += matriz[i][j]
            else:
                lista_corredores[i] = None
                break   

    for i in range(len(lista_corredores)):
        if lista_corredores[i] != None:
            ganador = lista_corredores[i]
            break

    for element in lista_corredores:
        if element != None:
            if element < ganador:
                ganador = element

    return ganador
# APARTADO C  
def más_etapas_ganadas(matriz):
    lista_corredores = [0] * len(matriz)
    mejor_tiempo = None
    for j in range(len(matriz[0])):

        for i in range(len(matriz)):
            if matriz[i][j] != None:
                mejor_tiempo = matriz[i][j]

        if mejor_tiempo != None:
            for i in range(len(matriz)):
                if matriz[i][j] != None:
                    if matriz[i][j] < mejor_tiempo:
                        mejor_tiempo = matriz[i][j]
                        mejor_corredor = i       
            lista_corredores[mejor_corredor] += 1

    for element in lista_corredores:
        if element > mayor:
            mayor = element

    return mayor 

    
# APARTADO D

def más_abandonos(matriz):
    etapas = [0] * len(matriz[0])
    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            if matriz[i][j] == None:
                etapas[j] += 1

    mayor = etapas[0]

    for i in range(len(etapas)):
        if mayor < etapas[i]:
            mayor = etapas[i]
            etapa_con_mas_abandonos = i
    return etapa_con_mas_abandonos

# PROBLEMA 2

class Canción:
    pass

# APARTADO A
def crear_lista_canciones(nomfile):
    file = open(nomfile, 'r', encoding='utf-8')

    canciones = []
    linea = file.readline()

    while linea != "":
        cancion = linea.split('#')
        interpretes = cancion[1].split('/')

        for element in canciones:
            if element.consultar_título() == cancion[0]:
                element.añadir_reproducción(cancion[2])
            else: 
                canciones.append(Canción(cancion[0],interpretes))
                canciones[-1].añadir_reproducción(cancion[2])
        linea.readline()
    file.close()
    return canciones

# APARTADO B 
def intérpretes_únicos(lista):
    interpretesUnicos = []
    for cancion in lista:
        intepretes_cancion = cancion.consultar_intérpretes()
        for interprete in intepretes_cancion:
            if interprete not in interpretesUnicos:
                interpretesUnicos.append(interprete)
    return interpretesUnicos

# APARTADO C  

def inteprete_con_mas_cacniones(canciones):
    interpretesUnicos = intérpretes_únicos(canciones)
    mayor = 0
    for interprete in interpretesUnicos:
        posible_mayor = 1 
        for i in range(len(canciones)):
            if interprete in canciones[i].consultar_intérpretes():
                posible_mayor += 1
        if posible_mayor > mayor: 
            mayor = posible_mayor
            interpreteMasCanciones = interprete


    return interpreteMasCanciones



# APARTADO D