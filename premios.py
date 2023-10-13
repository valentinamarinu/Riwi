def main():
    grupoA = []
    grupoB = []
    grupoC = []

    while True:
        print("SISTEMA DE REGISTRO RIWI")
        print("1. Registro de grupos.")
        print("2. Lista de grupos.")
        print("3. Cambiar a un coder de grupo.")
        print("4. Registro de coders eliminados por inasistencia.")
        print("5. Datos ceremonia de premiación.") #AQUÍ DEBE DE TENER CONTEO DEL MÁS MONITOR, DEL QUE ENTREGO MÁS TALLERES, MÁS COLABORADOR Y PARTICIPATIVO Y MAYOR NOTA TEST NIVELACIÓN
        print("6. SALIR.")
        seleccion = int(input("Ingrese solo el número de la opción deseada: "))
        try:
            if(seleccion == 1):
                agregar_grupo(grupoA,grupoB,grupoC)
            
            elif(seleccion == 2):
                listar_grupo(grupoA,grupoB,grupoC)

            elif(seleccion == 3):
                cambiar_coder(grupoA,grupoB,grupoC)
            
            elif(seleccion == 4):
                eliminados(grupoA,grupoB,grupoC)
            
            elif(seleccion == 5):
                ceremonia(grupoA,grupoB,grupoC)

            elif(seleccion == 6):
                break
        except:
            print("El valor ingresado debe ser un número.")


"""                FUNCIONES                """

def agregar_grupo(grupoA,grupoB,grupoC):
        try:
            grupo = int(input("Seleccione el grupo a registar: \n1. Grupo A\n2. Grupo B\n3. Grupo C"))
            i = 1
            if grupo == 1:
                while True:
                    print("GRUPO A")
                    trainer = input("Ingrese el nombre del Trainer del grupo A: ")
                    print(f"Registro coder #{i}")
                    grupo = "Grupo A"
                    nombre = input("Ingrese el nombre: ")
                    ingreso = input("Ingrese el mes de ingreso: ")
                    edad = int(input("Ingrese la edad: "))
                    monitor = int(input("Ingrese las veces que fue monitor: "))
                    inasistencias = int(input("Ingrese las inasistencias: "))
                    talleres = int(input("Ingrese la cantidad de talleres entregados: "))
                    test = float(input("Ingrese la nota obtenida en el test de nivelación: "))
                    colaboracion = int(input("Ingrese nota de 1 a 10 para la colaboración: "))
                    participacion = int(input("Ingrese nota de 1 a 10 para la participación: "))

                    estudiante = {"Trainer":trainer.capitalize(), "Nombre":nombre.capitalize(), "Ingreso":ingreso.capitalize(), "Edad":edad, 
                                "Grupo": grupo.capitalize(), "Monitorias":monitor, "Inasistencias":inasistencias, "Talleres":talleres, 
                                "Test de nivelación": test, "Colaboración":colaboracion, "Participación":participacion}
                    grupoA.append(estudiante)
                
                    salir = input("¿Desea ingresar más coders al registro? S/N")
                    salir = salir.lower()

                    if salir == "s":
                        i += 1
                    elif salir == "n":
                        break
            elif grupo == 2:
                while True:
                    print(f"Registro coder #{i}")
                    grupo = "Grupo B"
                    nombre = input("Ingrese el nombre: ")
                    ingreso = input("Ingrese el mes de ingreso: ")
                    edad = int(input("Ingrese la edad: "))
                    monitor = int(input("Ingrese las veces que fue monitor: "))
                    inasistencias = int(input("Ingrese las inasistencias: "))
                    talleres = int(input("Ingrese la cantidad de talleres entregados: "))
                    test = float(input("Ingrese la nota obtenida en el test de nivelación: "))
                    colaboracion = int(input("Ingrese nota de 1 a 10 para la colaboración: "))
                    participacion = int(input("Ingrese nota de 1 a 10 para la participación: "))

                    estudiante = {"Nombre":nombre.capitalize(), "Ingreso":ingreso.capitalize(), "Edad":edad, "Grupo": grupo.capitalize(), 
                                "Monitorias":monitor, "Inasistencias":inasistencias, "Talleres":talleres, "Test de nivelación": test, 
                                "Colaboración":colaboracion, "Participación":participacion}
                    grupoB.append(estudiante)
                
                    salir = input("¿Desea ingresar más coders al registro? S/N")
                    salir = salir.lower()

                    if salir == "s":
                        i += 1
                    elif salir == "n":
                        break
            elif grupo == 3:
                while True:
                    print(f"Registro coder #{i}")
                    grupo = "Grupo C"
                    nombre = input("Ingrese el nombre: ")
                    ingreso = input("Ingrese el mes de ingreso: ")
                    edad = int(input("Ingrese la edad: "))
                    monitor = int(input("Ingrese las veces que fue monitor: "))
                    inasistencias = int(input("Ingrese las inasistencias: "))
                    talleres = int(input("Ingrese la cantidad de talleres entregados: "))
                    test = float(input("Ingrese la nota obtenida en el test de nivelación: "))
                    colaboracion = int(input("Ingrese nota de 1 a 10 para la colaboración: "))
                    participacion = int(input("Ingrese nota de 1 a 10 para la participación: "))

                    estudiante = {"Nombre":nombre.capitalize(), "Ingreso":ingreso.capitalize(), "Edad":edad, "Grupo": grupo.capitalize(), 
                                "Monitorias":monitor, "Inasistencias":inasistencias, "Talleres":talleres, "Test de nivelación": test, 
                                "Colaboración":colaboracion, "Participación":participacion}
                    grupoC.append(estudiante)
                
                    salir = input("¿Desea ingresar más coders al registro? S/N")
                    salir = salir.lower()

                    if salir == "s":
                        i += 1
                    elif salir == "n":
                        break
        except:
            print("El valor ingresado debe ser un número.")


def listar_grupo(grupoA,grupoB,grupoC):
    if not (grupoA,grupoB,grupoC):
        print("\nEl grupo está vacio\n")
    else:
        try:
            seleccion = int(input("Seleccione una opción:\n1. Lista solo con nombres coders. \n2. Lista completa con toda la información por coder."))
            if seleccion == 1:
                tipo_lista = int(input("Seleccione la lista del grupo deseado: \n1. Grupo A\n2. Grupo B\n3. Grupo C"))
                print("\nLista de Grupos\n")
                if tipo_lista == 1:
                    print("GRUPO A")
                    for index, valor in enumerate(grupoA):
                        print(index,".-",valor["Nombre"])
                elif tipo_lista == 2:
                    print("GRUPO B")
                    for index, valor in enumerate(grupoB):
                        print(index,".-",valor["Nombre"])                    
                elif tipo_lista == 3:
                    print("GRUPO C")
                    for index, valor in enumerate(grupoC):
                        print(index,".-",valor["Nombre"])
            elif seleccion == 2:
                tipo_lista = int(input("Seleccione la lista del grupo deseado: \n1. Grupo A\n2. Grupo B\n3. Grupo C"))
                print("\nLista de Grupos\n")
                if tipo_lista == 1:
                    print("GRUPO A")
                    for index, valor in enumerate(grupoA):
                        print(index,".-",valor["Nombre"],"-",valor["Ingreso"],"-",valor["Edad"],"-",valor["Grupo"],"-",valor["Monitorias"],"-",valor["Inasistencias"],"-",valor["Talleres"],"-",valor["Test de nivelación"],"-",valor["Colaboración"],"-",valor["Participación"])       
                elif tipo_lista == 2:
                    print("GRUPO B")
                    for index, valor in enumerate(grupoB):
                        print(index,".-",valor["Nombre"],"-",valor["Ingreso"],"-",valor["Edad"],"-",valor["Grupo"],"-",valor["Monitorias"],"-",valor["Inasistencias"],"-",valor["Talleres"],"-",valor["Test de nivelación"],"-",valor["Colaboración"],"-",valor["Participación"])                       
                elif tipo_lista == 3:
                    print("GRUPO C")
                    for index, valor in enumerate(grupoC):
                        print(index,".-",valor["Nombre"],"-",valor["Ingreso"],"-",valor["Edad"],"-",valor["Grupo"],"-",valor["Monitorias"],"-",valor["Inasistencias"],"-",valor["Talleres"],"-",valor["Test de nivelación"],"-",valor["Colaboración"],"-",valor["Participación"])
        except:
            print("El valor ingresado debe ser un número.")


def cambiar_coder(grupoA,grupoB,grupoC):
        try:
            salida = int(input("Ingrese el grupo actual del coder a cambiar: \n1. Grupo A\n2. Grupo B\n3. Grupo C"))
            indice = int(input("Ingrese el indice del coder a cambiar en la lista actual: "))
            cambio = int(input("Ingrese el grupo al que desea cambiar al coder: \n1. Grupo A\n2. Grupo B\n3. Grupo C"))

            if salida == 1:
                if cambio == 2:
                    if (indice <0 or indice>len(grupoA)):
                        print("El indice ingresado no corresponde con ningun coder.")
                    else:
                        grupoB.append(grupoA[indice])
                        grupoA.pop(indice)
                        print("Cambio exitoso.")
                if cambio == 3:
                    if (indice <0 or indice>len(grupoA)):
                        print("El indice ingresado no corresponde con ningun coder.")
                    else:
                        grupoC.append(grupoA[indice])
                        grupoA.pop(indice)
                        print("Cambio exitoso.")                        
            elif salida == 2:
                if cambio == 1:
                    if (indice <0 or indice>len(grupoB)):
                        print("El indice ingresado no corresponde con ningun coder.")
                    else:
                        grupoA.append(grupoB[indice])
                        grupoB.pop(indice)
                        print("Cambio exitoso.")
                if cambio == 3:
                    if (indice <0 or indice>len(grupoB)):
                        print("El indice ingresado no corresponde con ningun coder.")
                    else:
                        grupoC.append(grupoB[indice])
                        grupoB.pop(indice)
                        print("Cambio exitoso.")  
            elif salida == 3:
                if cambio == 1:
                    if (indice <0 or indice>len(grupoC)):
                        print("El indice ingresado no corresponde con ningun coder.")
                    else:
                        grupoA.append(grupoC[indice])
                        grupoC.pop(indice)
                        print("Cambio exitoso.")
                if cambio == 2:
                    if (indice <0 or indice>len(grupoC)):
                        print("El indice ingresado no corresponde con ningun coder.")
                    else:
                        grupoB.append(grupoC[indice])
                        grupoC.pop(indice)
                        print("Cambio exitoso.")                          
        except:
            print("El valor ingresado debe ser un número.")


def eliminados(grupoA,grupoB,grupoC):
    contA = 0
    eliminadosA = []
    contB = 0
    eliminadosB = []
    contC = 0
    eliminadosC = []

    for index in grupoA:
        if grupoA["Inasistencias"] >= 15:
            contA += 1
            eliminadosA.append(grupoA[index]["Inasistencias"])
            grupoA.pop(index)

    for index in grupoB:
        if grupoB["Inasistencias"] >= 15:
            contB += 1
            eliminadosB.append(grupoB[index]["Inasistencias"])
            grupoB.pop(index)

    for index in grupoC:
        if grupoC["Inasistencias"] >= 15:
            contC += 1
            eliminadosC.append(grupoB[index]["Inasistencias"])
            grupoC.pop(index)

    try:
        seleccion = int(input("Seleccione el grupo del que quiere ver los eliminados por inasistencia: \n1. Grupo A\n2. Grupo B\n3. Grupo C"))

        if seleccion == 1:
            print(eliminadosA)
        elif seleccion == 2:
            print(eliminadosB)
        elif seleccion == 3:
            print(eliminadosC)
    except:
        print("El valor ingresado debe ser un número.")


def ceremonia(grupoA,grupoB,grupoC):
    monA = [], monB = [], monC = [], numMon = [], maxMonA = [], maxMonB = [], maxMonC = []
    talA = [] , talB = [], talC = [], numTal = [], mxTalA = [], mxTalB = [], mxTalC = []
    colA = [] , colB = [], colC = [], numCol = [], maColA = [], maColB = [], maColC = []
    parA = [] , parB = [], parC = [], numPar = [], axParA = [], axParB = [], axParC = []
    nilA = [] , nilB = [], nilC = [], numNil = [], xNilA = [], xNilB = [], xNilC = []

    for index in grupoA:
        if grupoA[index]["Monitorias"] > numMon:
            monA.append(grupoA[index]["Monitorias"])
            maxMonA.append(grupoA[index]["Nombre"])
            numMon = grupoA[index]["Monitorias"]

        if grupoA[index]["Talleres"] > numTal:
            talA.append(grupoA[index]["Talleres"])
            mxTalA.append(grupoA[index]["Nombre"])
            numTal = grupoA[index]["Talleres"]

        if grupoA[index]["Colaboración"] > numCol:
            colA.append(grupoA[index]["Colaboración"])
            maColA.append(grupoA[index]["Nombre"])
            numCol = grupoA[index]["Colaboración"]      

        if grupoA[index]["Participación"] > numPar:
            parA.append(grupoA[index]["Participación"])
            axParA.append(grupoA[index]["Nombre"])
            numPar = grupoA[index]["Participación"]  

        if grupoA[index]["Participación"] > numNil:
            nilA.append(grupoA[index]["Participación"])
            xNilA.append(grupoA[index]["Nombre"])
            numNil = grupoA[index]["Participación"] 

    for index in grupoB:
        if grupoB[index]["Monitorias"] > numMon:
            monB.append(grupoB[index]["Monitorias"])
            maxMonB.append(grupoB[index]["Nombre"])
            numMon = grupoB[index]["Monitorias"]

        if grupoB[index]["Talleres"] > numTal:
            talB.append(grupoB[index]["Talleres"])
            mxTalB.append(grupoB[index]["Nombre"])
            numTal = grupoB[index]["Talleres"]

        if grupoB[index]["Colaboración"] > numCol:
            colB.append(grupoB[index]["Colaboración"])
            maColB.append(grupoB[index]["Nombre"])
            numCol = grupoB[index]["Colaboración"]      

        if grupoB[index]["Participación"] > numPar:
            parB.append(grupoB[index]["Participación"])
            axParB.append(grupoB[index]["Nombre"])
            numPar = grupoB[index]["Participación"]  

        if grupoB[index]["Participación"] > numNil:
            nilB.append(grupoB[index]["Participación"])
            xNilB.append(grupoB[index]["Nombre"])
            numNil = grupoB[index]["Participación"]

    for index in grupoC:

        if grupoC[index]["Monitorias"] > numMon:
            monC.append(grupoC[index]["Monitorias"])
            maxMonC.append(grupoC[index]["Nombre"])
            numMon = grupoC[index]["Monitorias"]

        if grupoC[index]["Talleres"] > numTal:
            talC.append(grupoC[index]["Talleres"])
            mxTalC.append(grupoC[index]["Nombre"])
            numTal = grupoC[index]["Talleres"]

        if grupoC[index]["Colaboración"] > numCol:
            colC.append(grupoC[index]["Colaboración"])
            maColC.append(grupoC[index]["Nombre"])
            numCol = grupoC[index]["Colaboración"]      

        if grupoC[index]["Participación"] > numPar:
            parC.append(grupoC[index]["Participación"])
            axParC.append(grupoC[index]["Nombre"])
            numPar = grupoC[index]["Participación"]  

        if grupoC[index]["Participación"] > numNil:
            nilC.append(grupoC[index]["Participación"])
            xNilC.append(grupoC[index]["Nombre"])
            numNil = grupoC[index]["Participación"] 

    print(f"El coder del grupo A que ha sido más veces monitor es {maxMonA}")
    print(f"El coder del grupo B que ha sido más veces monitor es {maxMonB}")
    print(f"El coder del grupo C que ha sido más veces monitor es {maxMonC}")
    
    if talA>talB:
        if talA>talC:
            print(f"El coder que fue más veces monitor es {mxTalA}")
        else:  
            print(f"El coder que fue más veces monitor es {mxTalA}")
        

main()