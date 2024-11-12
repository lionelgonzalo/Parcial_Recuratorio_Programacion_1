import random

def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [0] * cantidad_columnas
        matriz += [fila]
    return matriz

# 1. Cargar Votos: Se realiza una carga secuencial de todos los votos de cada una de las
# cinco listas (Debe ser una matriz)
# NOTA: Validar todos los ingresos de datos, evitar votos negativos o nro de lista que no sean
# números de tres cifras.

def cargar_votos(matriz: list) -> list:
    '''
    Recibe una matriz y la cantidad de listas. Se encarga de pedir al usuario numero de lista, votos de cada turno y lo carga en la matriz. Retorna la matriz cargada
    '''
    for fil in range (len(matriz)): 

        numero_lista=int(input(f"\nIngrese el numero de la lista {fil+1} : "))
        while numero_lista < 100 or numero_lista > 999:
            numero_lista=int(input(f"Recuerde que el numero de listas son positivos y de 3 cifras\nReingrese el numero de de la lista {fil+1} : "))

        votos_mañana=int(input(f"Ingrese la cantidad de votos del turno *mañana* para la lista {numero_lista}: "))
        while votos_mañana < 1:
            votos_mañana=int(input(f"Recuerde que la cantidad de votos tiene que ser positiva!\nReingrese la cantidad de votos del turno *mañana* para la lista {numero_lista}: "))

        votos_tarde=int(input(f"Ingrese la cantidad de votos del turno *tarde* para la lista {numero_lista}: "))
        while votos_tarde < 1:
            votos_tarde=int(input(f"Recuerde que la cantidad de votos tiene que ser positiva\nReingrese la cantidad de votos del turno *tarde* para la lista {numero_lista}: "))

        votos_noche=int(input(f"Ingrese la cantidad de votos del turno *noche* para la lista {numero_lista}: "))
        while votos_noche < 1:
            votos_noche=int(input(f"Recuerde que la cantidad de votos tiene que ser positiva\nReingrese la cantidad de votos del turno *noche* para la lista {numero_lista}: "))

        matriz[fil][0] = numero_lista
        matriz[fil][1] = votos_mañana
        matriz[fil][2] = votos_tarde
        matriz[fil][3] = votos_noche

    return matriz

# 2. Mostrar Votos: Muestra en un lindo formato los siguientes datos:
# Nro Lista, Votos Turno Mañana,Votos Turno Tarde,Votos Turno Noche,Porcentaje Voto:

def calcular_porcentaje_votos(matriz: list) -> list:
    '''
    Se encarga de calcular el porcentaje de las listas. Recibe la matriz, suma los votos y calcula el porcentaje. Retorna una lista con los porcentajes
    '''
    acumulador_votos = 0
    lista_porcentaje = [0] * len(matriz)
    for fil in range (len(matriz)):
        suma_votos_lista = matriz[fil][1] + matriz[fil][2] + matriz[fil][3]
        acumulador_votos += suma_votos_lista
    for fil in range (len(matriz)):
        suma_votos_lista = matriz[fil][1] + matriz[fil][2] + matriz[fil][3]
        if acumulador_votos > 0:
            lista_porcentaje[fil] = round((suma_votos_lista * 100) / acumulador_votos, 2)
        else:
            lista_porcentaje[fil] = 0
    return lista_porcentaje

        
def mostrar_votos(matriz: list) -> None:
    '''
    Se encarga de mostrar la matriz, llama la funcion para calcular el porcentaje y muestra tanto los votos como los porcentajes
    '''
    print("\n########## VOTOS ##########")
    porcentaje = calcular_porcentaje_votos(matriz)
    for fil in range(len(matriz)):
        print(f"\nLISTA N°: {matriz[fil][0]}\nVotos Turno Mañana: {matriz[fil][1]}\nVotos Turno Tarde: {matriz[fil][2]}\nVotos Turno Noche: {matriz[fil][3]}\nPorcentaje votos: {porcentaje[fil]} %")

#3. Ordenar votos turno mañana: Ordena la matriz de mayor a menor por la cantidad de
#votos que tuvieron en el turno mañana.

def ordenar_matriz(matriz: list, indice: int) -> list:
    '''
    Ordena una matriz comparando una columna. Recibe la matriz y el numero de columna. Retorna la matriz ordenada
    '''
    for fil_i in range(len(matriz)-1):
        for fil_j in range(fil_i + 1,len(matriz)):
            if matriz[fil_i][indice] < matriz[fil_j][indice]:
                aux = matriz[fil_i]
                matriz[fil_i] = matriz[fil_j]
                matriz[fil_j] = aux
    return matriz
            
def mostrar_mayor_turno_mañana(matriz: list, indice: int) -> None:
    '''
    Muestra las listas ordenadas de mayor a menor segun los votos del turno mañana.
    '''
    matriz = ordenar_matriz(matriz, indice)
    print("\n########## MAYOR A MENOR SEGUN VOTO DE TURNO MAÑANA ##########\n")
    for fil in range (len(matriz)):
        print (f"# {fil+1} -> LISTA N: {matriz[fil][0]} con {matriz[fil][1]} votos del turno mañana")


# 4. No te votó nadie: Encontrar y mostrar a las listas que tengan menos del 5% de todos
# los votos

def encontrar_no_te_voto_nadie(matriz: list) -> list:
    '''
    Identifica listas con menos del 5% de los votos y las marca en una lista.
    '''
    porcentaje = calcular_porcentaje_votos(matriz) 
    lista_no_te_voto_nadie = [0] * len(matriz)
    for fil in range(len(matriz)):
        if porcentaje[fil] < 5:
            lista_no_te_voto_nadie[fil] = 1
    return lista_no_te_voto_nadie 

def mostrar_no_te_voto_nadie(matriz: list) -> None:
    '''
    Muestra las listas que obtuvieron menos del 5% de los votos.
    '''
    print("\n########## NO TE VOTO NADIE ##########\n\nListas con menos de 5 porciento de los votos:")
    no_te_voto_nadie = encontrar_no_te_voto_nadie(matriz)
    porcentaje = calcular_porcentaje_votos(matriz)
    bandera = False
    for fil in range(len(matriz)):
        if no_te_voto_nadie[fil] == 1:
            print (f"# -> LISTA N: {matriz[fil][0]} con {porcentaje[fil]} %")
            bandera=True
    if bandera == False:
        print (f"# -> No se encontro ninguna lista con menos del 5 % de votos")


# 5. Turno que más fue a votar: Mostrar cuál fue el turno o los turnos al que más alumnos
# fueron a votar.


def sumar_votos_por_turno(matriz: list) -> list:
    '''
    Calcula la suma de votos por cada turno (mañana, tarde, noche) y la devuelve en una lista.
    '''
    votos_mañana = 0
    votos_tarde = 0
    votos_noche = 0

    for fil in range(len(matriz)):
        votos_mañana += matriz[fil][1]  
        votos_tarde += matriz[fil][2]   
        votos_noche += matriz[fil][3] 

    matriz_turnos_votos = [["mañana", votos_mañana],
                    ["tarde", votos_tarde],
                    ["noche", votos_noche]]
    
    return matriz_turnos_votos

def mostrar_mayor_votos_turno(matriz: list) -> None:
    '''
    Muestra el ranking de turnos con mayor cantidad de votos.
    '''
    print("\n########## TOP DE TURNOS QUE MÁS FUE A VOTAR ##########\n")
    matriz_turnos_votos = sumar_votos_por_turno(matriz)
    matriz_turnos_votos = ordenar_matriz(matriz_turnos_votos,1)
    for i in range(3):
        print(f"# {i+1} -> El turno {matriz_turnos_votos[i][0]} con {matriz_turnos_votos[i][1]} votos.")


# 6. Ballotage:Verifica si hay segunda vuelta o no, según las reglas estudiantiles la única
# forma de evitar la segunda vuelta es que una lista tenga más del 50% de los votos.

def verificar_ballotage(matriz: list) -> bool:
    """
    Verifica si alguna lista tiene más del 50% de los votos,
    en cuyo caso no se realiza segunda vuelta.
    """
    porcentaje = calcular_porcentaje_votos(matriz)
    for i in porcentaje:
        if i > 50:
            return True
    return False

def mostrar_ballotage(matriz: list) -> None:
    '''
    Muestra los resultados del ballotage, indicando si es necesario o no
    según si alguna lista supera el 50% de los votos.
    '''
    ordenar_listas_votos_total(matriz)
    porcentaje= calcular_porcentaje_votos(matriz)
    if verificar_ballotage(matriz):
        print(f"\nNo existe la segunda vuelta! Una lista superó el 50 % de los votos.\n")
        print(f"########## GANADOR DE LAS ELECCIONES EN PRIMERA VUELTA ##########\n\n-> # 1 LISTA: {matriz[0][0]} con un: {porcentaje[0]} % de los votos")
    else:
        print(f"Ninguna lista superó el 50 % de los votos.\n\n########## BALLOTAGE ##########\n\n# -> LAS LISTAS {matriz[0][0]} y {matriz[1][0]} IRAN A UNA SEGUNDA VUELTA!!!!\n")

def ordenar_listas_votos_total(matriz: list) -> None:
    porcentaje = calcular_porcentaje_votos(matriz)
    for i in range(len(porcentaje) - 1):
        for j in range(i + 1, len(porcentaje)):
            if porcentaje[i] < porcentaje[j]:
                aux_porcentaje = porcentaje[i]
                porcentaje[i] = porcentaje[j]
                porcentaje[j] = aux_porcentaje
                aux_matriz = matriz[i]
                matriz[i] = matriz[j]
                matriz[j] = aux_matriz
    return matriz

# 7. Realizar segunda vuelta:Se encarga de realizar la segunda vuelta electoral con los
# dos candidatos más votados. Se le pide al usuario la cantidad de alumnos que fueron
# a votar en cada turno en la segunda vuelta y de manera random se calculan los votos
# del primer y segundo candidato en cada turno. Al final de ello se calcula el porcentaje
# final de cada lista y se muestra al ganador de las elecciones.
# NOTA: Solo se accede si hay la opción 6 verificó que hay segunda vuelta, sino indicar
# que no hubo segunda vuelta.


def cargar_votos_ballotage(matriz: list, matriz_2: list) -> list:
    '''
    Carga los totales de votos de cada turno. Recibe dos matrices, una nueva y otra cargada. Retorna una matriz nueva con las listas y los totales de votos por turno
    '''
    ordenar_listas_votos_total(matriz_2)
    votos_mañana=int(input(f"Ingrese la cantidad de votos del turno *mañana* en total para la segunda vuelta: "))
    while votos_mañana < 1:
        votos_mañana=int(input(f"Recuerde que la cantidad de votos tiene que ser positiva!\nReingrese la cantidad de votos en total para la segunda vuelta: "))

    votos_tarde=int(input(f"Ingrese la cantidad de votos del turno *tarde* en total para la segunda vuelta: "))
    while votos_tarde < 1:
        votos_tarde=int(input(f"Recuerde que la cantidad de votos tiene que ser positiva\nReingrese la cantidad de votos en total para la segunda vuelta: "))

    votos_noche=int(input(f"Ingrese la cantidad de votos del turno *noche* en total para la segunda vuelta: "))
    while votos_noche < 1:
        votos_noche=int(input(f"Recuerde que la cantidad de votos tiene que ser positiva\nReingrese la cantidad de votos del turno *noche* en total para la segunda vuelta: "))
    for fil in range (len(matriz)):
        matriz[fil][0] = matriz_2[fil][0]
        matriz[fil][1] = votos_mañana
        matriz[fil][2] = votos_tarde
        matriz[fil][3] = votos_noche
    return matriz

def generar_votos_random(matriz: list, matriz_2: list) -> list:
    """
    Genera votos aleatorios para cada lista en cada turno y almacena la información en la matriz.
    """
    cargar_votos_ballotage(matriz, matriz_2)
    for fil in range(1, 4):
        votos_total_turno = matriz[0][fil] 
        votos_lista1 = random.randint(1, votos_total_turno)
        votos_lista2 = votos_total_turno - votos_lista1
        matriz[0][fil] = votos_lista1
        matriz[1][fil] = votos_lista2

    return matriz

def mostrar_ganador_ballotage(matriz: list, matriz_2: list) -> None:
    '''
    Se encarga de mostrar el resultado final del ballotage.
    '''
    generar_votos_random(matriz, matriz_2)
    porcentaje = calcular_porcentaje_votos(matriz)
    for fil in range(len(matriz)):
        print(f"\nLISTA N°: {matriz[fil][0]}\nVotos Turno Mañana: {matriz[fil][1]}\nVotos Turno Tarde: {matriz[fil][2]}\nVotos Turno Noche: {matriz[fil][3]}\nPorcentaje votos: {porcentaje[fil]} %\n")
    print("########## GANADOR DE LAS ELECCIONES EN BALLOTAGE ##########\n")
    if porcentaje[0] > porcentaje [1]:
        print(f"# -> LA LISTA: {matriz[0][0]} con: {porcentaje[0]} % del total de votos\n")
    else:
        print(f"# -> LA LISTA: {matriz[1][0]} con: {porcentaje[1]} % del total de votos\n")


cantidad_listas = 3
matriz_estudiantes = inicializar_matriz(cantidad_listas,4)
matriz_ballotage = inicializar_matriz(2,4)


def menu():
    print (f"\n########## ELECCIONES DEL CENTRO DE ESTUDIANTES !!!!!! ##########")
    Bandera_opcion_7 = False
    while True:
        print("\nMenu de Opciones:")
        print("\n1. Cargar votos")
        print("2. Mostrar votos y porcentaje")
        print("3. Ordenar votos turno mañana")
        print("4. No te voto nadie")
        print("5. Turno que mas fue a votar")
        print("6. Verificar Ballotage")
        print("7. Realizar segunda vuelta")
        print("8. Salir")

        opcion = int(input("\nSeleccione una opción: "))
        
        if opcion == 1:
            cargar_votos(matriz_estudiantes)
        elif opcion == 2:
            mostrar_votos(matriz_estudiantes)
        elif opcion == 3:
            mostrar_mayor_turno_mañana(matriz_estudiantes,1)
        elif opcion == 4:
            mostrar_no_te_voto_nadie(matriz_estudiantes)
        elif opcion == 5:
            mostrar_mayor_votos_turno(matriz_estudiantes)
        elif opcion == 6:
            mostrar_ballotage(matriz_estudiantes)
            Bandera_opcion_7 = True
        elif opcion == 7:
            if verificar_ballotage(matriz_estudiantes):
                print(f"No puede elegir esta opcion ya que existe un ganador en la primera vuelta !!!!")
            elif Bandera_opcion_7 == False:
                print(f"No se puede realizar la segunda vuelta ya que no se verifico el ballotage!")
            else:
                mostrar_ganador_ballotage(matriz_ballotage, matriz_estudiantes)
        elif opcion == 8:
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente nuevamente.")

menu()