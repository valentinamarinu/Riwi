# Calculadora de calificaciones
nota = float(input("Ingrese una nota: "))
try:
    if nota<0:
        print("Se ingreso una nota negativa, ingrese una not válida.")
    elif (nota<=1) :
        print(f"La nota ingresada es {nota} y la calificacion obtenida es E")
    elif (nota>1) and (nota<=2):
        print(f"La nota ingresada es {nota} y la calificacion obtenida es D")
    elif (nota>2) and (nota<=3):
        print(f"La nota ingresada es {nota} y la calificacion obtenida es C")
    elif (nota>3) and (nota<=4):
        print(f"La nota ingresada es {nota} y la calificacion obtenida es B")
    elif (nota>4) and (nota<=5):
        print(f"La nota ingresada es {nota} y la calificacion obtenida es A")
    else :
        print("Ingrese una nota válida.")
except ValueError:
        print("Ingrese una nota válida.")



# Verificar si un número es par o no, y además si es mayor a 10
try:
    verificar = int(input("Ingrese un número entero: "))
    par = verificar%2

    if (par == 0):
        if (verificar<10):
            print("El número que ingresaste es par y es menor a diez.")
        else:
            print("El número que ingresaste es par y es mayor a diez.")

    else:
        if (verificar<10):
            print("El número que ingresaste es impar y es menor a diez.")
        else:
            print("El número que ingresaste es impar y es mayor a diez.")
except ValueError:
    print("Ingrese un número válido.")



# Al ingresar 3 números verificar si son multiplos de 3 y 5
try:
    for i in range(3):
        multiplo = int(input(f"Ingrese el número entero {i+1}: "))
        tres = multiplo%3
        cinco = multiplo%5

        if (tres == 0) and (cinco == 0):
            print(f"El número {i+1} es multiplo de tres y cinco.")
        elif tres == 0 :
            print(f"El numero {i+1} es multiplo de tres.")
        elif cinco == 0:
            print(f"El numero {i+1} es multiplo de cinco.")
        else:
            print("El número ingresado no es multiplo de tres o cinco.")
except ValueError:
    print("Ingrese un número entero válido.")



# Calculadora notas finales universidad
try:
    nParcial = float(input("Ingrese la nota del parcial: "))
    nTrabajos = float(input("Ingrese la nota de los trabajos: "))
    parcial = nParcial*0.8
    print(parcial)
    trabajos = nTrabajos*0.2
    print(trabajos)
    final = parcial + trabajos

    if (parcial<0) or (trabajos<0):
        print("Revisar notas ingresadas, alguna tiene valor negativo.")
    elif final<3:
        print("El estudiante no superó la nota mínima, perdió el curso.")
    else: 
        print("El estudiante superó la nota mínima,aprovó el curso.")
except ValueError:
    print("Ingrese una nota válida.")








        

