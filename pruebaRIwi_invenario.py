def main():  
    while True:
        print("\n         Inventario SodimacColombia           \n")
        print("           -- MENÚ DE OPCIONES--           \n")
        print("1. Agregar un producto al inventario.")
        print("2. Actualizar cantidades de un producto en el stock.")
        print("3. Verificar stock de un producto.")
        print("4. Venta de un producto.")
        print("5. Salir.")
        
        try:
            seleccion = int(input("Ingrese opción deseada: "))
        except:
            print("Ingrese una opción válida.")
        
        inventario = []
        if seleccion == 1:
            agregar(inventario)
        elif seleccion == 2:
            actualizar(inventario)
        elif seleccion == 3:
            listar(inventario)  
        elif seleccion == 4:
            venta(inventario)
        elif seleccion == 5:
            break


def agregar(inventario):
    name = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad de existencias del producto: "))
    producto = {"producto" : name.capitalize(), "cantidad": cantidad}
    inventario.append(producto)
    print("\nProducto registrado correctamente.\n")


def listar(inventario):
    busqueda = input("Ingrese el nombre del producto del que quiere verificar el stock: ")

    for index in inventario:
        if busqueda.low() == inventario[index]["producto"]:
            stock = inventario[index]["cantidad"]
            print(f"El producto {busqueda} tiene un stock de {stock} ")
        else:
            print("El producto no ha sido encontrado.")


def actualizar(inventario):
    try:
        indice = int(input("Ingrese el indice del producto a actualizar: "))

        if(indice < 0 or indice > len(inventario)):
            print("El indice ingresado no corresponde con ningun producto.")
        else:
            print("Actualizando el producto -", inventario[indice]["producto"])
            nombre = input("Ingrese el nuevo nombre del producto: ")
            cantidad = input("Ingrese la nueva cantidad del producto: ")

            inventario[indice]["producto"] = nombre
            inventario[indice]["cantidad"] = int(cantidad)
            print("El producto fue actualizado correctamente. ")
    except:
        print("Ingrese una opción válida.")


def venta(inventario):
    try:
        indice = int(input("Ingrese el indice del producto a vender: "))
        if(indice <0 or indice > len(inventario)):
            print("El indice no corresponde a ningún producto.")
        else: 
            conformacion = input("Esta seguro que desea vender este producto? S/N ")
            if(conformacion.lower() == "s"):
                inventario.pop(indice)
                print("Producto vendido correctamente, stock actualizado.")
    except:
        print("El indice no es válido.")


main()