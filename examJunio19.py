# PROBLEMA 1
# APARTADO A
def índice_repartido(lista,nombreRepartidor):
    for i in range(lista):
        if lista[i] == nombreRepartidor:
            index = i
    return index
# APARTADO B 
def crear_matriz_horas(repartidores,fileName):
    file = open(fileName, 'r', encoding='UTF-8')
    linea = file.readline()
    matriz = []

    for i in range(len(repartidores)):
        matriz.append([0] * 31)


    while linea != "":
        repartidor = linea.split('#')
        i = índice_repartido(repartidores, repartidor[0])

        for j in range(len(matriz[0])):
            if j == int(repartidor[1]) - 1:
                matriz[i][j] = int(repartidor[2])
        linea = file.readline()
    
    return matriz
# APARTADO C  

def duracion_mayor_secuencia(matriz,lista,repartidor):
    indice = índice_repartido(lista,repartidor)
    horas_repartidor = matriz[indice]

    candidato = 1
    mayor = 0

    for i in range(len(horas_repartidor)-1):
        if horas_repartidor[i] != 0 and horas_repartidor[i+1] != 0:
            candidato += 1 
        elif candidato > mayor:
            mayor = candidato
    return mayor
# PROBLEMA 2

class TiempoDeUso():
    pass
# APARTADO A
def añadir(lista,nombreUsuario,nombreAplicacion,tiempo):
    for element in lista:
        if element.usuario == nombreUsuario and element.aplicación == nombreAplicacion: 
            element.tiempo += tiempo
            return False
        else:
            lista.append(TiempoDeUso(nombreUsuario,nombreAplicacion))
            lista[-1].tiempo += tiempo
            return True

# APARTADO B 
def borrar(lista,nombreUsuario):
    objetosAborrar = []
    for i in range(len(lista)):
        if lista[i].usuario == nombreUsuario:
            objetosAborrar.append(i)

    for element in objetosAborrar:
        del lista[element]

# APARTADO C  
def se_debe_bloquear(lista,nombreUsuario,minutos):
    suma = 0
    for element in lista:
        if element.nombreUsuario == nombreUsuario:
            suma += element.tiempo

    if minutos > suma:
        return True
    else:
        return False

# APARTADO D

def bloqueados(lista,tiempo_max):
    usuariosBloqueados = []
    for element in lista:
        if se_debe_bloquear(lista,element.nombreUsuario,tiempo_max) == True and element.nombreUsuario not in usuariosBloqueados:
            usuariosBloqueados.append(element.nombreUsuario)
    return usuariosBloqueados