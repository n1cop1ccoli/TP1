import getpass
#Variables utilizadas globalmente en todo el programa.
def inicialization():
    global USER, PASSWORD, count, type_user, admin, menu_admin, count_1, count_2, count_3
    USER = "admin@shopping.com"
    PASSWORD= "12345"
    count = 3  
    # 0: no logueado
    # 1: Admin
    # 2: Cliente
    # 3: Salir   
    type_user = "0"
    admin = False
    menu_admin = "6"
    #count_1 = indumentaria
    #count_2 = perfumeria
    #count_3 = comida
    count_1 = 0
    count_2 = 0
    count_3 = 0

#Procedimiento utilizado para separar contenidos del programa.  
def separation():
    print("-------------------------------------------------------------------------------------------------------------")    

#Procedimiento para validar el usuario y contraseña, y verificar cantidad de intentos.
def validation():
    global USER, PASSWORD, count,admin
    while (count > 0):
        user_vd = input("Ingrese su usuario: ").lower()
        password_vd = getpass.getpass("Ingrese su contraseña: ")
        if (user_vd != USER or password_vd != PASSWORD):
            if count == 1:
                count = count - 1
                separation()
                print("\nUsted ya alcanzo el limite de intentos, lo sentimos el programa se ha cerrado\n")
                separation()
            else:
                count = count - 1
                separation()
                print(f"\nEl usuario o contraseña son incorrectos le quedan {count} intentos.\n")
                separation()
        elif (user_vd == USER or password_vd == PASSWORD):
            count = 0
            admin = True

#Procedimiento que crea los locales y aumenta el contador dependiendo de su rubro
def createShop():
    global count_1, count_2, count_3
    separation()
    try:
        count_shop = int(input("Ingresar cantidad de locales a registrar o 0 para salir: "))
    except:
        print("Ingresar un valor valido")
        createShop()
    separation()
    while count_shop > 0:
        nameShop = input(f"Ingresar nombre del local {count_shop}: ")
        locationShop = input("Ingresar localizacion del local: ")
        print("\n1) Indumentaria \n2) Perfumeria \n3) Comida")
        categoryShop = input("Ingresar numero del rubro del local: ")
        while categoryShop != "1" and categoryShop != "2" and categoryShop != "3":
            categoryShop=input("\nIngrese una de las opciones validas:")
        match categoryShop:
            case "1":
                count_1=count_1 + 1
                categoryShop="Indumentaria" 
            case "2":
                count_2=count_2 + 1
                categoryShop="Perfumeria" 
            case "3":
                count_3=count_3 + 1
                categoryShop="Comida"
        separation()
        print(f"\nNombre del local: {nameShop}\nLocalizacion del local: {locationShop}\nRubro del local: {categoryShop}")
        separation()
        while count_shop == 1:
            try:
                count_shop = int(input("\nEs el ultimo local a registrar, si quiere ingresar mas locales coloque la cantidad sino coloque 0 para salir: "))
                if count_shop != 0:
                    count_shop = count_shop + 1
            except:
                print("Ingresa un valor valido")
        count_shop = count_shop - 1

#Procedimiento que exhibe el o los rubros que mayor cantidad de locales posee
def comparison_may():
    global count_1, count_2, count_3
    if count_1 > count_2 and count_1 > count_3:
        print(f"\nEl rubro que mayor cantidad de locales tiene es indumentaria con {count_1} cantidad de locales")
    elif(count_2 > count_1 and count_2 > count_3):
        print(f"\nEl rubro que mayor cantidad de locales tiene es perfumeria con {count_2} cantidad de locales")
    elif(count_3 > count_1 and count_3 > count_2):
        print(f"\nEl rubro que mayor cantidad de locales tiene es comida con {count_3} cantidad de locales")
    elif(count_1 == count_2):
        print(f"\nLos rubros que mayor cantidad de locales tienen son indumentaria con {count_1} y perfumeria con {count_2} cantidad de locales")
    elif(count_2 == count_3):
        print(f"\nLos rubros que mayor cantidad de locales tienen son perfumeria con {count_2} y comida con {count_3} cantidad de locales")
    elif(count_1 == count_3):
        print(f"\nLos rubros que mayor cantidad de locales tienen son indumentaria con {count_1} y comida con {count_3} cantidad de locales")

#Procedimiento que exhibe el o los rubros que menor cantidad de locales posee
def comparison_men():
    global count_1, count_2, count_3
    if (count_1 < count_2 and count_1 < count_3):
        print(f"\nEl rubro que menor cantidad de locales tiene es indumentaria con {count_1} cantidad de locales")
    elif(count_2 < count_1 and count_2 < count_3):
        print(f"\nEl rubro que menor cantidad de locales tiene es perfumeria con {count_2} cantidad de locales")
    elif(count_3 < count_1 and count_3 < count_2):
        print(f"\nEl rubro que menor cantidad de locales tiene es comida con {count_3} cantidad de locales")
    elif(count_1 < count_3 and count_2 < count_3 and count_1 == count_2):
        print(f"\nLos rubros que menor cantidad de locales tienen son indumentaria con {count_1} y perfumeria con {count_2} cantidad de locales")
    elif(count_2 < count_1 and count_3 < count_1 and count_2 == count_3):
        print(f"\nLos rubros que menor cantidad de locales tienen son perfumeria con {count_2} y comida con {count_3} cantidad de locales")
    elif(count_1 < count_2 and count_3 < count_2 and count_1 == count_3):
        print(f"\nLos rubros que menor cantidad de locales tienen son indumentaria con {count_1} y comida con {count_3} cantidad de locales")

#Procedimiento que muestra el menu de administrar locales y muestra el o los rubros que mayor y menor cantidad de locales tienen.
def shop():
    global menu_admin
    separation()
    comparison_may()
    comparison_men()
    separation()
    print("\na) Crear locales \nb) Modificar local \nc) Eliminar local \nd) Volver")
    shop_menu = input("\nIngrese sector de menu: ")
    while shop_menu != "a" and shop_menu != "b" and shop_menu != "c" and shop_menu != "d":
        shop_menu=input("\nIngrese una de las opciones validas:")
    match shop_menu:
        case "a":
           createShop()
           menu_admin = "1"
        case "b":
            separation()
            print("En construccion...")
            menu_admin=input("\nIngresar 6 para volver: ")
        case "c":
            separation()
            print("En construccion...")
            menu_admin=input("\nIngresar 6 para volver: ")
        case "d":
            menu_admin = "6"
            
#Procedimiento que muestra el menu para administrar las novedades
def news():
    global menu_admin
    separation()
    print("\na) Crear novedades \nb) Modificar novedad \nc) Eliminar novedad \nd) Ver reporte de novedades \ne) Volver")
    aux = input("\nIngrese sector de menu: ")
    while aux != "a" and aux != "b" and aux != "c" and aux != "d" and aux != "e":
        aux = input("Ingresar un valor valido: ")
    if aux == "e":
        menu_admin = "6"
    else:
        separation()
        print("En construccion.")
        menu_admin = input("Ingrese 4 para volver: ")
                
                
#Procedimiento que muestra el menu de administrador.
def menu():
    global admin, menu_admin
    while menu_admin != "0" and menu_admin != "1" and menu_admin != "2" and menu_admin != "3" and menu_admin != "4" and menu_admin != "5" and menu_admin != "6":
        menu_admin=input("\nIngrese una de las opciones validas:")
    match menu_admin:
        case "0":
            separation()
            print("Saliste del programa.")
            admin = False
        case "1":
           shop()
        case "2":
            separation()
            print("En construccion...")
            menu_admin = input("Ingrese 6 para volver: ")
        case "3":
            separation()
            print("En construccion...")
            menu_admin = input("Ingrese 6 para volver: ")
        case "4":
            news()
        case "5":
             separation()
             print("En construccion...")
             menu_admin = input("Ingrese 6 para volver: ")
        case "6":
            separation()
            print("\n 1) Gestión de locales\n 2) Crear cuentas de dueños de locales\n 3) Aprobar / Denegar solicitud de descuento\n 4) Gestión de Novedades\n 5) Reporte de utilización de descuentos\n 0) Salir")
            menu_admin = input("\nIngrese sector de menu: ")
    
#Programa principal
inicialization()
while(type_user == "0"):
    print("1) Administrador  \n2) Cliente")
    type_user = input("Ingrese el tipo de usuario o presione 3 para salir: ")
    while(type_user != "1" and type_user != "2" and type_user != "3" and type_user != "0"):
        type_user=input("\nIngrese una de las opciones validas:")
    match type_user:
        case "1":
            validation()
        case "2":
            separation()
            input("Esta seccion se encuentra en contruccion, ingrese cualquier tecla para volver: ")
            type_user="0"
        case "3":
            separation()
            print("Saliste del programa.")

while (admin == True):
    menu()