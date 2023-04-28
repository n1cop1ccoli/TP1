import getpass

def inicialization():
    global USER, PASSWORD, count, type_user, admin, menu_admin
    USER = "admin"
    PASSWORD= 12345
    count = 3
    # 0: no logueado
    # 1: Admin
    # 2: Cliente
    # 3: Salir   
    type_user = 0
    admin = False
    menu_admin = 6
    
def validation():
    global USER, PASSWORD, count,admin
    while (count > 0):
        user_vd = input("\nIngrese su usuario: ")
        try:
            password_vd = int(getpass.getpass("Ingrese su contraseña: "))
        except:
            print("Please enter a number.. hijo de puta")
        if (user_vd != USER or password_vd != PASSWORD):
            if count == 1:
                count = count - 1
                print("\nUsted ya alcanzo el limite de intentos, lo sentimos el programa se ha cerrado")
            else:
                count = count - 1
                print(f"\nEl usuario o contraseña son incorrectos le quedan {count} intentos.\n")
        elif (user_vd == USER or password_vd == PASSWORD):
            count = 0
            admin = True

def menu():
    global admin, menu_admin
    match menu_admin:
        case 0:
            print("fuiste..se cerro el programa")
            admin = False
        case 1:
            print("\na) Crear locales \nb) Modificar local \nc) Eliminar local \nd) Volver\n")
            back = input("\n Ingrese sector de menu: ")
            if back == "d":
                menu_admin = 6
        case 2:
            print("En construccion...")
            try:
                menu_admin = int(input("Ingrese 6 para volver: "))
            except:
                print("Please enter a number.. hijo de puta")
        case 3:
            print("En construccion...")
            try:
                menu_admin = int(input("Ingrese 6 para volver: "))
            except:
                print("Please enter a number.. hijo de puta")
        case 4:
            print("\na) Crear novedades \nb) Modificar novedad \nc) Eliminar novedad \nd) Ver reporte de novedades \ne) Volver\n")
            back = input("\n Ingrese sector de menu: ")
            if type(int(back)) == int:
                print("\nPlease enter a letter.. hijo de puta")
                back = input("\n Ingrese sector de menu: ")
            elif back == "e":
                menu_admin = 6
        case 5:
            print("En construccion...")
            try:
                menu_admin = int(input("Ingrese 6 para volver: "))
            except:
                print("Please enter a number.. hijo de puta")
        case 6:
            print("\n 1. Gestión de locales\n 2. Crear cuentas de dueños de locales\n 3. Aprobar / Denegar solicitud de descuento\n 4. Gestión de Novedades\n 5. Reporte de utilización de descuentos\n 0. Salir\n")
            try:
                menu_admin = int(input("\n Ingrese sector de menu: "))
            except:
                print("Please enter a number.. hijo de puta")

inicialization()
while(type_user == 0):
    print("1 Administrador  \n2 Cliente")
    try:
        type_user = int(input("Ingrese el tipo de usuario o presione 3 para salir: "))
    except:
        print("Te dije que pongas 3.. hijo de puta")
    match type_user:
        case 1:
            validation()
        case 2:
            try:
              type_user = int(input("Esta seccion se encuentra en contruccion, presione 0 para volver: "))
            except:
                print("Te dije que pongas 0.. hijo de puta")
        case 3:
            print("fuiste..se cerro el programa")

while (admin == True):
    menu()