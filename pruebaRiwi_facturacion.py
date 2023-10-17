def main():
        while True:
            print("         Facturación Tienda Pepito           \n")
            print("           -- MENÚ DE OPCIONES--           \n")

            print("1. Registrar cliente.")
            print("2. Registrar un nuevo producto a la factura.")
            print("3. Listar productos actuales de la factura.")
            print("4. Mostrar factura.")
            print("5. Salir.")
            try:
                seleccion = int(input("Ingrese opción deseada: "))
            except:
                print("Ingrese una opción válida.")
            cliente = []
            productos = []
            if seleccion == 1:
                clientes(cliente)
            elif seleccion == 2:
                registrar(productos)
            elif seleccion == 3:
                listar(productos)  
            elif seleccion == 4:
                factura(cliente, productos)
            elif seleccion == 5:
                break


def clientes(cliente):
        try:
            name = input("Ingrese el nombre del cliente: ")
            lastName = input("Ingrese los apellidos del cliente: ")
            id = int(input("Ingrese el número de la cédula del cliente: "))
            cliente.append(name)
            cliente.append(lastName)
            cliente.append(id)
            print("\nCliente registrado correctamente.\n")
                
        except:
            print("Ingrese información válida solicitada.")
        

def registrar(productos):
        while True:            
            try:
                item = input("Ingrese el nombre del producto: ")
                precio = float(input("Ingrese el precio del producto: "))
            except:
                print("Ingrese una opción válida.")

            producto = {"item" : item.capitalize(), "precio" : precio}
            productos.append(producto)

            print("\nProducto registrado correctamente.\n")
            
            salir = input("¿Desea ingresar más productos en la facturación? S/N")
            salir = salir.lower()
            if salir == "n":
                break


def listar(productos):
    print("Productos ingresados: ")
    for index, valor in enumerate(productos):
        print(index,". Producto: ", valor["item"],"- Precio :", valor["precio"])


def total(productos):
    totalProducto = 0
    
    for item in productos:
        totalProducto += productos[item]["precio"]
    
    totalProducto = totalProducto + (totalProducto*0.19)
    return totalProducto


def factura(cliente, productos):
    print("          --FACTURA--          ")
    print(f"Cliente : {cliente[0]} {cliente[1]}")

    listar(productos)
    
    conteo = 0
    totalFactura = 0
    for item in productos:
        conteo += 1
    print(f"Número de productos registrados: {conteo}")

    if conteo == 1:
        if productos["precio"] > 500000:
           print("Tu compra esta excenta del IVA. ")
           totalFactura = total(productos) - (total(productos) * 0.19)
           print(F"El total a pagar es de ${totalFactura}")
        else:
           totalFactura = total(productos)
           print(F"El total a pagar es de ${totalFactura}")

      
    elif conteo >= 7:
        print("Te regalamos un bono de $100.000 para redimir en tu siguiente compra.")
        totalFactura = total(productos)
        print(F"El total a pagar es de ${totalFactura}")


    elif conteo >= 5:
        print("Se aplico un despuento del 10%.")
        totalFactura = total(productos) - (total(productos) * 0.1)
        print(F"El total a pagar es de ${totalFactura}")

    elif conteo >= 3 :
        print("Se aplico un despuento del 5%.")
        totalFactura = total(productos) - (total(productos) * 0.05)
        print(F"El total a pagar es de ${totalFactura}")


main()