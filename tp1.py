import getpass
import os

#Variables utilizadas globalmente en todo el programa.
def inicialization():
    global USER, PASSWORD, count, type_user, menu_admin, count_1, count_2, count_3, USERS, SHOPS, opcion_owner, opcion_customer, totalShops
    USERS = [["1","4","6","9"],["admin","localA","localB","cliente"],["12345","AAAA1111","BBBB2222","33xx33"],["administrador","dueñoLocal","dueñoLocal","cliente"]]
    SHOPS = []
    totalShops = 0
    count = 3
    type_user = "notAuth"
    opcion_owner= "1"
    opcion_customer= "1"
    menu_admin = "1"
    count_1 = 0
    count_2 = 0
    count_3 = 0
    llenarLocales()
#Procedimiento para llenar la tabla de locales con espacios disponibles
def llenarLocales():
    for i in range(0,3):
        SHOPS.append([])
        for j in range(0, 49):
            SHOPS[i].append(0)
    print(SHOPS)
#Procedimieno que dependiendo del sistema operativo limpia la terminal
def cleanWindow():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#Procedimiento utilizado para separar contenidos del programa.
def separation():
    print("-------------------------------------------------------------------------------------------------------------")

def current_menu(typeUser):
    if(typeUser == "1"):
        print("> MENU ADMINISTRADOR <")
    if(typeUser == "2"):
        print("> MENU DUEÑO LOCAL <")
    if(typeUser == "3"):
        print("> MENU CLIENTE <")

#Procedimiento para validar el usuario y contraseña, y verificar cantidad de intentos.
def validation(typeUser):
    global USERS,USER,PASSWORD,count,type_user
    cleanWindow()
    while (count > 0):
        current_menu(typeUser)
        user_vd = input("Ingrese su usuario: ")
        password_vd = getpass.getpass("Ingrese su contraseña: ")
        match typeUser:
            case "1":
                if(user_vd == USERS[1][0] and password_vd == USERS[2][0]):
                    cleanWindow()
                    current_menu("1")
                    menu()
                    count = 0
            case "2":
                if(user_vd == USERS[1][1] and password_vd == USERS[2][1] or user_vd == USERS[1][2] and password_vd == USERS[2][2]):
                    cleanWindow()
                    current_menu("2")
                    menu_owner()
                    count = 0
            case "3":
                if(user_vd == USERS[1][3] and password_vd == USERS[2][3]):
                    cleanWindow()
                    current_menu("3")
                    menu_customer()
                    count = 0
        if (count != 0):
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
       
#Procedimiento que crea los locales y aumenta el contador dependiendo de su rubro
def createShop():
    global count_1, count_2, count_3
    cleanWindow()
    current_menu("1")
    separation()
    if(totalShops < 50):
        nameShop = input(f"Ingresar nombre del local o * para culminar: ")
        while nameShop != '*':
            SHOPS[0][totalShops] = nameShop
            SHOPS[1][totalShops] = input("Ingresar localizacion del local (Piso, Ala, Sector): ")
            print("\n1) Indumentaria \n2) Perfumeria \n3) Comida")
            categoryShop = input("Ingresar numero del rubro del local: ")
            while categoryShop != "1" and categoryShop != "2" and categoryShop != "3":
                categoryShop=input("\nIngrese una de las opciones validas:")
            match categoryShop:
                case "1":
                    count_1=count_1 + 1
                    SHOPS[2][totalShops]="Indumentaria"
                case "2":
                    count_2=count_2 + 1
                    SHOPS[2][totalShops]="Perfumeria"
                case "3":
                    count_3=count_3 + 1
                    SHOPS[2][totalShops]="Comida"
            print("\n4) Dueño Local A \n6) Dueño Local B")
            dueñoShop = input("Ingresar numero del rubro del local: ")
            while dueñoShop != "4" and dueñoShop != "6":
                dueñoShop=input("\nIngrese una de las opciones validas:")
            SHOPS[3][totalShops]=dueñoShop
            nameShop = input(f"Ingresar nombre del local o * para culminar: ")
        cleanWindow()
        print(SHOPS)
        # nameShop = input(f"Ingresar nombre del local o * para culminar: ")
        # while nameShop != '*':
        #     locationShop = input("Ingresar localizacion del local: ")
        #     print("\n1) Indumentaria \n2) Perfumeria \n3) Comida")
        #     categoryShop = input("Ingresar numero del rubro del local: ")
        #     while categoryShop != "1" and categoryShop != "2" and categoryShop != "3":
        #         categoryShop=input("\nIngrese una de las opciones validas:")
        #     match categoryShop:
        #         case "1":
        #             count_1=count_1 + 1
        #             SHOPS[2][totalShops]="Indumentaria"
        #         case "2":
        #             count_2=count_2 + 1
        #             SHOPS[2][totalShops]="Perfumeria"
        #         case "3":
        #             count_3=count_3 + 1
        #             SHOPS[2][totalShops]="Comida"
        #     separation()
        #     print(f"\nNombre del local: {nameShop}\nLocalizacion del local: {locationShop}\nRubro del local: {categoryShop}")
        #     separation()
        #     nameShop = input(f"Ingresar nombre del local o * para culminar: ")
        # cleanWindow()

#Procedimiento que exhibe el o los rubros que mayor cantidad de locales posee
def comparison_may():
    global count_1, count_2, count_3
    if count_1 > count_2 and count_1 > count_3:
        print(f"\nEl rubro que mayor cantidad de locales tiene es indumentaria con {count_1} cantidad de locales")
    elif(count_2 > count_1 and count_2 > count_3):
        print(f"\nEl rubro que mayor cantidad de locales tiene es perfumeria con {count_2} cantidad de locales")
    elif(count_3 > count_1 and count_3 > count_2):
        print(f"\nEl rubro que mayor cantidad de locales tiene es comida con {count_3} cantidad de locales")
    elif(count_1 == count_2 and count_3 == count_1):
        print(f"\nLos rubros tienen la misma cantidad de locales con {count_1} cantidad de locales")
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
    current_menu("1")
    separation()
    comparison_may()
    comparison_men()
    separation()
    print("\na) Crear locales \nb) Modificar local \nc) Eliminar local \nd) Mapa de locales \ne) Volver")
    shop_menu = input("\nIngrese sector de menu: ")
    while shop_menu != "a" and shop_menu != "b" and shop_menu != "c" and shop_menu != "e" and shop_menu != "d":
        shop_menu=input("\nIngrese una de las opciones validas:")
    match shop_menu:
        case "a":
           cleanWindow()
           createShop()
           menu_admin = "1"
        case "b":
            cleanWindow()
            separation()
            print("En construccion...")
            menu_admin="1"
        case "c":
            cleanWindow()
            separation()
            print("En construccion...")
            menu_admin="1"
        case "d":
            cleanWindow()
            print("mapardo")
        case "e":
            cleanWindow()

#Procedimiento que muestra el menu para administrar las novedades
def news():
    global menu_admin
    current_menu("1")
    separation()
    print("\na) Crear novedades \nb) Modificar novedad \nc) Eliminar novedad \nd) Ver reporte de novedades \ne) Volver")
    aux = input("\nIngrese sector de menu: ")
    while aux != "a" and aux != "b" and aux != "c" and aux != "d" and aux != "e":
        aux = input("Ingresar un valor valido: ")
    if aux == "e":
        cleanWindow()
    else:
        cleanWindow()
        separation()
        print("En construccion.")
        menu_admin="4"

def menu_customer():
    global opcion_customer
    while opcion_customer != "0":
        print("\n1) Registrarme \n2) Buscar descuentos en locales \n3) Solicitar descuento \n4) Ver novedades \n0) Salir")
        opcion_customer = input("\nIngrese sector de menu: ")
        while opcion_customer != "0" and opcion_customer != "1" and opcion_customer != "2" and opcion_customer != "3" and opcion_customer != "4":
            opcion_customer=input("\nIngrese una de las opciones validas:")
        match opcion_customer:
            case "0":
                cleanWindow()
                separation()
                print("Saliste del programa.")
            case "1":
                cleanWindow()
                print("En construccion...")
                separation()
            case "2":
                cleanWindow()
                print("En construccion...")
                separation()
            case "3":
                cleanWindow()
                print("En construccion...")
                separation()
            case "4":
                cleanWindow()
                print("En construccion...")
                separation()

#Procedimeinto que muestra el menu para dueño de local
def menu_owner():
    global opcion_owner
    while opcion_owner != "0" and opcion_owner != "d":
        print("\n1) Gestión de Descuentos \n  a) Crear descuento para mi local \n  b) Modificar descuento de mi local \n  c) Eliminar descuento de mi local \n  d) Volver \n2) Aceptar / Rechazar pedido de descuento\n3) Reporte de uso de descuentos\n0) Salir")
        opcion_owner = input("\nIngrese sector de menu: ")
        while opcion_owner != "0" and opcion_owner != "1" and opcion_owner != "2" and opcion_owner != "3" and opcion_owner != "a" and opcion_owner != "b" and opcion_owner != "c" and opcion_owner != "d":
            opcion_owner=input("\nIngrese una de las opciones validas:")
        match opcion_owner:
            case "0":
                cleanWindow()
                separation()
                print("Saliste del programa.")
            case "1":
                cleanWindow()
                print("En construccion...")
                separation()
            case "2":
                cleanWindow()
                print("En construccion...")
                separation()
            case "3":
                cleanWindow()
                print("En construccion...")
                separation()
            case "a":
                cleanWindow()
                print("En construccion...")
                separation()
            case "b":
                cleanWindow()
                print("En construccion...")
                separation()
            case "c":
                cleanWindow()
                print("En construccion...")
                separation()
            case "d":
                cleanWindow()
                separation()
                print("Saliste del programa.")


#Procedimiento que muestra el menu de administrador.
def menu():
    global menu_admin
    while menu_admin != "0":
        print("\n 1) Gestión de locales\n 2) Crear cuentas de dueños de locales\n 3) Aprobar / Denegar solicitud de descuento\n 4) Gestión de Novedades\n 5) Reporte de utilización de descuentos\n 0) Salir")
        menu_admin = input("\nIngrese sector de menu: ")
        while menu_admin != "0" and menu_admin != "1" and menu_admin != "2" and menu_admin != "3" and menu_admin != "4" and menu_admin != "5" and menu_admin != "6":
            menu_admin=input("\nIngrese una de las opciones validas:")
        match menu_admin:
            case "0":
                cleanWindow()
                separation()
                print("Saliste del programa.")
            case "1":
                cleanWindow()
                shop()
            case "2":
                cleanWindow()
                print("En construccion...")
                separation()
            case "3":
                cleanWindow()
                print("En construccion...")
                separation()
            case "4":
                cleanWindow()
                news()
            case "5":
                cleanWindow()
                print("En construccion...")
                separation()


#Programa principal
inicialization()
while(type_user == "notAuth"):
    print("1) Administrador  \n2) Dueño Local \n3) Cliente")
    type_user = input("Ingrese el tipo de usuario o presione 0 para salir: ")
    while(type_user != "1" and type_user != "2" and type_user != "3" and type_user != "0"):
        type_user=input("\nIngrese una de las opciones validas:")
    if type_user == "1" or type_user == "2" or type_user == "3":
        validation(type_user)
    else:
        cleanWindow()
        separation()
        print("Saliste del programa.")