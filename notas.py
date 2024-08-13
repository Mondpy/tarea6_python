def ingresar_puntuacion_y_comentario():
    while True:
        print('Por favor, ingrese una puntuación entre 1 y 5')
        point = input()
        if point.isdecimal():
            point = int(point)
            if point <= 0 or point > 5:
                print('Por favor, ingrese un valor entre 1 y 5')
            else:
                print('Por favor, ingrese un comentario')
                comment = input()
                post = f'Puntuación: {point} Comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                break
        else:
            print('La puntuación debe ser un número')

def ver_resultados_anteriores():
    print('Resultados anteriores')
    with open("data.txt", "r") as read_file:
        print(read_file.read())

def menu():
    while True:
        print('Por favor, seleccione el proceso que desea realizar')
        print('1: Ingresar puntuación y comentario')
        print('2: Ver resultados anteriores')
        print('3: Salir')
        num = input()

        if num.isdecimal():
            num = int(num)

            if num == 1:
                ingresar_puntuacion_y_comentario()
            elif num == 2:
                ver_resultados_anteriores()
            elif num == 3:
                print('Saliendo')
                break
            else:
                print('Por favor, ingrese un número entre 1 y 3')
        else:
            print('Por favor, ingrese un número entre 1 y 3')

# Llamar al método del menú para iniciar el programa
menu()
