'''
    5IM10. PÉREZ GALICIA ADRIÁN
    PROTOCOLO
'''


import itertools

print("\n\nBienvenido a mi creador de protocolos: ")

def menu():
    print("\nImprima el número con la opción que desea realiar: ")
    print("\n1. Crear protocolo")
    print("2. Agregar elementos")
    print("3. Borrar elementos")
    print("4. Leer contenido")
    print("5. Salir")
    print("\n*LÍMITE DE PASOS: 15*")


protocolo = []
inst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

while True:
    menu()

    opc = int(input("\n¿Qué opción le gustaría realizar?: "))
    if opc == 1:
        print("\n¡EL PROTOCOLO HA SIDO CREADO SATISFACTORIAMENTE!\n")

    elif opc == 2:
        a = input("\nEscriba la instrucción: ")
        protocolo.append(a)
        more = input ("\n¿Deseas escribir otra instrucción? S/N: ")
        if more == "S":
            pasos = int(input("\n¿Cuántas instrucciones quieres incluir al protocolo?: "))
            for x in itertools.repeat(None, pasos):
                a = input("\nEscriba la nueva instrucción: ")
                protocolo.append(a)
        elif more == "N":
            print("")
            menu()
        else:
            print("¡ELIJA UNA OPCIÓN VALIDA!")
            print("")
    elif opc == 3:
        elim = int(input("\n¿Que instrucción desea eliminar?: "))
        protocolo.pop(elim)
        print(f"Se ha eliminado exitosamente el paso {elim}\n")

    elif opc == 4:
        union = list(zip(inst, protocolo))
        for i in union:
            print(i)
    elif opc == 5:
        print("\n\n\nGracias por probar mi programa. Hasta luego...")
        break
    else:
        print("¡ERROR! ESCOJA UNA OPCIÓN VÁLIDA")



