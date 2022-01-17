# Problema 1
# APARTADO  A) 
def distancia(ciudades, distancias, desde, hasta):

    for i in range(len(ciudades)):
        if desde == ciudades[i]:
            desde = i
            break
    for i in range(len(ciudades)):
        if hasta == ciudades[i]:
            hasta = i
            break 

    return distancias[desde][hasta] 
# APARTADO B)
def ciudades_más_separadas(ciudades,distancias):
    mayor = 0
    for i in range(len(distancias)):
        for j in range(len(distancias[0])):
            if distancias[i][j] > mayor:
                mayor = distancias[i][j]
                ciudadUno = i
                ciudadDos = j 
    return [ciudades[ciudadUno],ciudades[ciudadDos]]

# APARTADO C)

def tiempo_de_viaje(ciudades,distancias,viaje,velocidades):
    tiempo = 0
    for i in range(len(viaje) - 1):
        dist = distancia(ciudades,distancias,viaje[i],viaje[i+1])
        tiempo += dist / velocidades[i]
    return tiempo 
        
    

def main():

    distancias = [[ 0, 7, 13, 27, 80, 71, 6, 22],[ 7, 0, 6, 21, 88, 79, 5, 15], [ 13, 6, 0, 19, 97, 88, 8, 21], [ 27, 21, 19, 0, 111, 102, 25, 28], [ 80, 88, 97, 111, 0, 10, 90, 101], [ 71, 79, 88, 102, 10, 0, 81, 92],[ 6, 5, 8, 25, 90, 81, 0, 19], [ 22, 15, 21, 28, 101, 92, 19, 0]] 
    ciudades = ['Castellón de la Plana', 'Villarreal', 'Burriana', 'La Vall de Uxó', 'Vinaroz', 'Benicarló', 'Almazora', 'Onda']
    viaje = ['Vinaroz', 'Castellón de la Plana', 'Almazora']
    velocidades = [100, 60]
    print(distancia(ciudades, distancias, 'Villarreal', 'Castellón de la Plana'))
    print(ciudades_más_separadas(ciudades, distancias))
    print(tiempo_de_viaje(ciudades,distancias,viaje,velocidades))

main()

# Problema 2 

# APARTADO A
def crear_lista_meses(namefile, tipoDelito):

    file = open(namefile,'r',encoding='utf-8')
    listaMeses = [0] * 13
    linea = file.readline()

    while linea != "":

        delito = linea.split(',')
        if delito[3] == tipoDelito:           
            listaMeses[delito[1]] += 1
        linea = file.readline()

    del listaMeses[0]
    file.close()
    return listaMeses
# APARTADO B

def mayor_periodo_creciente(lista):
    candidato = 1 
    for i in range(len(lista) - 1):
        if lista[i] < lista[i+1]:
            candidato += 1 
        elif candidato >= mayor:
            mayor = candidato
            candidato = 1 

    return mayor 

class Localidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.delitos = 0
    def añadir(self, cantidad):
        self.delitos += cantidad

# APARTADO C 

def buscar(lista, localidad):
    for element in lista:
        if element.nombre == localidad:
            return element 
# APARTADO D

def delitos_por_localidad(fileName):
    file = open(fileName, 'r', encoding='utf-8')
    linea = file.readline()
    lista = []

    while linea != "":
        delito = linea.delitos(',')
        if buscar(lista, delito[2]) == None:
            lista.append(Localidad(delito[2]))
        else:
            for element in lista: 
                if element.nombre == delito[2]:
                    element.añadir(1)
        linea = file.readline()
    file.close()
    return lista

  




