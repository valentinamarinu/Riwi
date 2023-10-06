nombre = "Ana"
# Formas para concatenar (coma, suma, )
print("Hola mundo", "soy", nombre)
print(nombre + " hola mundo" + " soy")
print(f"Hola mi nombre es {nombre}")


# Algoritmo para sumar dos números
a = 2
b = 3
c = 9
c = a + b

print(f"La suma de {a} más {b} es igual a {c}")


try:
    d = int(input("Ingres el primer número a operar: "))
    e = int(input("Ingrese el segundo número a operar: "))
    f = d + e
    g = d - e
    h = d * e
    k = d ** e
    i = d / e
    l = d // e
    j = d % e

    print(f"La resta de {d} menos {e} es igual a {g}")
    print(f"La multiplicación de {d} por {e} es igual a {h}")
    print(f"La potencia de {d} a la {e} es igual a {k}")
    print(f"La potencia de {d} a la {e} es igual a {pow(d,e)}")
    print(f"La división de {d} entre {e} es igual a {i}")
    print(f"La división entera de {d} entre {e} es igual a {l}")
    print(f"El módulo {d} de {e} es igual a {j}")
except ValueError:
    print("El valor que ingresaste no corresponde a un número, por favor vuelve a ingresar un número.")



