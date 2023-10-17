def main():
    try:
        name = input("Ingresa tu nombre:")
        greetUser(name)

        makeTalk(name)

        dismissUser(name)
    except:
        print("Ingresa un nombre válido.")


def greetUser(name):
    print(f"Hola, feliz día {name}. ")


def makeTalk(name): 
    try:
        respuesta = int(input(f"¿Cómo inicias la semana {name}? \n 1. Bien 2. Mal\n"))
        if respuesta == 1:
            print(f"Me alegra mucho que inicies de la mejor forma esta nueva semana {name}.")
        elif respuesta == 2:
            print(f"Lo siento mucho {name}, ten la seguridad que la semana va mejorar, ¡Animos!")
    except:
        print("La respuesta ingresada no es válida, intenta nuevamente.")


def dismissUser(name):
    print(f"Hasta una próxima oportunidad volveremos a charlar {name}, hasta luego.")


main()