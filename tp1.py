import getpass

def inicialization():
    global USER, PASSWORD, count, type_user, admin, menu_admin, count_1, count_2, count_3
    USER = "admin"
    PASSWORD= "12345"
    count = 3  
    # 0: no logueado
    # 1: Admin
    # 2: Cliente
    # 3: Salir   
    type_user = 0
    admin = False
    menu_admin = 6
    #count_1 = indumentaria
    #count_2 = perfumeria
    #count_3 = comida
    count_1 = 0
    count_2 = 0
    count_3 = 0
    
def validation():
    global USER, PASSWORD, count,admin
    while (count > 0):
        user_vd = input("\nIngrese su usuario: ")
        password_vd = getpass.getpass("Ingrese su contraseña: ")
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

def createShop():
    global count_1, count_2, count_3
    count_shop = int(input("Ingresar cantidad de locales a registrar o 0 para salir: "))
    while count_shop > 0:
        nameShop = input("Ingresar nombre del local: ")
        locationShop = input("Ingresar localizacion del local: ")
        print("\n1 Indumentaria \n2 perfumeria \n3 comida")
        categoryShop = int(input("Ingresar numero del rubro del local: "))
        match categoryShop:
            case 1:
                count_1 = count_1 + 1 
            case 2:
                count_2 = count_2 + 1 
            case 3:
                count_3 = count_3 + 1
        print(f"\n Nombre del local: {nameShop} \n Localizacion del local: {locationShop}")
        if count_shop == 1:
            count_shop = int(input("\nEs el ultimo local a registrar, si quiere ingresar mas locales coloque la cantidad sino coloque 0 para salir: "))+1
        count_shop = count_shop - 1

#Funcion que devuelve el rubro que mayor cantidad de locales posee
def comparison_may():
    global count_1, count_2, count_3
    if count_1 > count_2 and count_1 > count_3:
        print(f"\nEl rubro que mayor cantidad de locales tiene es indumentaria con {count_1} cantidad de locales")
    elif(count_2 > count_1 and count_2 > count_3):
        print(f"\nEl rubro que mayor cantidad de locales tiene es perfumeria con {count_2} cantidad de locales")
    else:
        print(f"\nEl rubro que mayor cantidad de locales tiene es comida con {count_3} cantidad de locales")

#Funcion que devuelve el rubro que manor cantidad de locales posee
def comparison_men():
    global count_1, count_2, count_3
    if count_1 < count_2 and count_1 < count_3:
        print(f"\nEl rubro que menor cantidad de locales tiene es indumentaria con {count_1} cantidad de locales")
    elif(count_2 < count_1 and count_2 < count_3):
        print(f"\nEl rubro que menor cantidad de locales tiene es perfumeria con {count_2} cantidad de locales")
    else:
       print(f"\nEl rubro que menor cantidad de locales tiene es comida con {count_3} cantidad de locales")

def shop():
    global menu_admin
    comparison_may()
    comparison_men()
    print("\na) Crear locales \nb) Modificar local \nc) Eliminar local \nd) Volver\n")
    #Usamos la variable local shop_menu para determinar a que seccion del menu ingresar
    shop_menu = input("\n Ingrese sector de menu: ")
    match shop_menu:
        case "a":
           createShop()
           menu_admin = 1
        case "b":
            print("En construccion...")
        case "c":
            print("En construccion...")
        case "d":
            menu_admin = 6

def menu():
    global admin, menu_admin
    match menu_admin:
        case 0:
            print("fuiste..se cerro el programa")
            admin = False
        case 1:
           shop()
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
#Programa principal
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