
# PROBLEMA 1
# A) 
def mejor_comercial_último_año(matriz):
    suma_ventas = 0
    mejor_comercial = 0 
    mayor_venta = 0 
    for i in range(len(matriz)):
        for j in range(13):
            suma_ventas = matriz[i][j]
        if suma_ventas > mayor_venta:
            mejor_comercial = i 
            mayor_venta = matriz[i][j]

    return mejor_comercial

# B)

def facturación_total_por_mes(matriz):
    lista_total_meses = [0] * 13
    lista_suma_meses = []
    for i in range(len(matriz[0])):
        suma = 0
        for j in range(len(matriz)):
            suma += matriz[j][i]
        lista_suma_meses.append(suma)
    
    for i in range(len(lista_suma_meses)):
        lista_total_meses[i % 12] += lista_suma_meses[i]
    
    del lista_total_meses[-1]
    return lista_total_meses

# C)

def cantidad_valores_consecutivos_con_aumento(lista):
    mayor_crecimiento = 0
    posible_crecimiento = 1 # Se inicia en 1 porque el ultimo nunca se suma y ha de sumarse

    for i in range(len(lista)-1):
        if lista[i] < lista[i+1]:
            posible_crecimiento += 1
        elif posible_crecimiento > mayor_crecimiento:
            mayor_crecimiento = posible_crecimiento
            posible_crecimiento = 1
    return mayor_crecimiento

# Pruebas para los dos problemas

def main():
    matriz = [[2, 2, 3, 3, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 2, 1, 2, 1, 2, 1],[3, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 3, 3, 4, 4, 3, 3, 2, 2, 1, 1],[2, 2, 2, 3, 3, 3, 3, 3, 3, 2, 2, 2, 0, 0, 1, 1, 1, 0, 2, 0, 0, 1, 1, 1]]
    print(mejor_comercial_último_año(matriz))
    print(facturación_total_por_mes(matriz))
    print(cantidad_valores_consecutivos_con_aumento(facturación_total_por_mes(matriz)))

main()

# PROBLEMA 2

# A)

def posición(lista, numero):
    for i in range(len(lista)):
        if lista[i].teléfono == numero:
            return i

# B) 
def actualizar_minutos_consumidos(lista,fileName):
    file = open(fileName, 'r', encoding='utf-8')
    linea = file.readline()

    while linea != "":
        llamadas = linea.split('#')
        posicion = posición(lista,llamadas[0])
        if posicion != None:
            lista[posicion].minutos_consumidos += int(llamadas[1])
        
        linea = file.readline()
   
    file.close()

def excenden_minutos_gratis(lista):
    telefonos = []

    for i in range(len(lista)):
        if lista[i].minutos_gratis < lista[i].minutos_consumidos:
            telefonos.append(lista[i].teléfono)
    
    return telefonos

def mejores_clientes(lista,n):
    DNIs = []
    for element in lista:
        numero_de_lineas = 1
        for numero in lista:
            if element.dni == numero.dni:
                numero_de_lineas += 1

        if numero_de_lineas >= n and element.dni not in DNIs:
            DNIs.append(element.dni)

    return DNIs
    