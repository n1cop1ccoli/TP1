# Integrantes
# Bercini Genaro, Egidi Kevin, Piccoli Nicolas

import getpass
import os

#Variables utilizadas globalmente en todo el programa.
def inicialization():
    global USER, PASSWORD, count, type_user, menu_admin, USERS, SHOPS, opcion_owner, opcion_customer, totalShops, businessShop, code
    USERS = [["1","4","6","9"],["admin@shopping.com","localA@shopping.com","localB@shopping.com","unCliente@shopping.com"],["12345","AAAA1111","BBBB2222","33xx33"],["administrador","dueñoLocal","dueñoLocal","cliente"]]
    SHOPS = [['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']]
    totalShops = 0
    count = 3
    code = 0
    type_user = ""
    opcion_owner= "1"
    opcion_customer= "1"
    menu_admin = "1"
    businessShop=[["Indumentaria", "Perfumeria", "Comida"], [0,0,0]]
    spaceShops()
#Procedimiento para llenar la tabla de locales con espacios disponibles
def spaceShops():
    for i in range(0,6):
        for j in range(0,50):
            SHOPS[i][j] = "0"
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
                
#Procedimeinto para mostrar el perfil que se esta utilizando en ese momento
def current_menu(typeUser):
    if(typeUser == "1"):
        print("> MENU ADMINISTRADOR <")
    if(typeUser == "2"):
        print("> MENU DUEÑO LOCAL <")
    if(typeUser == "3"):
        print("> MENU CLIENTE <")
                
#Procedimiento para mostrar menu de cliente
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
        opcion_owner = input("\nIngrese sector de menu: ").lower()
        while opcion_owner != "0" and opcion_owner != "1" and opcion_owner != "2" and opcion_owner != "3" and opcion_owner != "a" and opcion_owner != "b" and opcion_owner != "c" and opcion_owner != "d":
            opcion_owner=input("\nIngrese una de las opciones validas:").lower()
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

#Procedimiento que muestra el menu para administrar las novedades
def news():
    global menu_admin
    separation()
    print(">GESTION DE NOVEDADES<")
    separation()
    print("\na) Crear novedades \nb) Modificar novedad \nc) Eliminar novedad \nd) Ver reporte de novedades \ne) Volver")
    aux = input("\nIngrese sector de menu: ").lower()
    while aux != "a" and aux != "b" and aux != "c" and aux != "d" and aux != "e":
        aux = input("Ingresar un valor valido: ").lower()
    if aux == "e":
        cleanWindow()
    else:
        cleanWindow()
        print("En construccion.")
        separation()
        menu_admin="4"
        
#Procedimiento que muestra el menu de administrar locales y muestra el o los rubros que mayor y menor cantidad de locales tienen.
def shop():
    global menu_admin
    separation()
    if businessShop[1][0] > businessShop[1][1] and businessShop[1][0] > businessShop[1][2] or businessShop[1][1] > businessShop[1][0] and businessShop[1][1] > businessShop[1][2] or businessShop[1][2] > businessShop[1][1] and businessShop[1][2] > businessShop[1][0]:
        print(f"El rubro con mayor cantidad de locales es {businessShop[0][0]} con {businessShop[1][0]} locales")
        print(f"El segundo rubro con mayor cantidad de locales es {businessShop[0][1]} con {businessShop[1][1]} locales")
        print(f"El rubro con menor cantidad de locales es {businessShop[0][2]} con {businessShop[1][2]} locales")
    elif(businessShop[1][0] == businessShop[1][1] and businessShop[1][0] == businessShop[1][2]):
        print(f"Los rubros tienen la misma cantidad de locales con {businessShop[1][0]} cantidad de locales")
    else:
        print(f"Los rubros que tienen la mayor cantidad de locales son {businessShop[0][0]} y {businessShop[0][1]} con {businessShop[1][0]} cantidad de locales")
    separation()
    print("\na) Crear locales \nb) Modificar local \nc) Eliminar local \nd) Mapa de locales \ne) Volver")
    shop_menu = input("\nIngrese sector de menu: ").lower()
    while shop_menu != "a" and shop_menu != "b" and shop_menu != "c" and shop_menu != "e" and shop_menu != "d":
        shop_menu=input("\nIngrese una de las opciones validas:").lower()
    match shop_menu:
        case "a":
           cleanWindow()
           createShop()
           menu_admin = "1"
        case "b":
            cleanWindow()
            modShop()
            cleanWindow()
            menu_admin="1"
        case "c":
            cleanWindow()
            deleteShop()
            cleanWindow()
            menu_admin="1"
        case "d":
            cleanWindow()
            map()
            cleanWindow()
            menu_admin="1"
        case "e":
            cleanWindow()


#Procedimiento utilizado para el ordenamiento de el array de locales
def sort(Arr, lim, totalCol, Desc):
    col= 1
    if(lim > 1):
        for i in range (0, lim):
            for j in range(i+1, lim):
                if(Desc):
                    if(Arr[col][i] < Arr[col][j]):
                        for w in range(0,totalCol):
                            aux = Arr[w][i]
                            Arr[w][i] = Arr[w][j]
                            Arr[w][j] = aux
                else:
                    if(Arr[col][i] > Arr[col][j]):
                        for w in range(0,totalCol):
                            aux = Arr[w][i]
                            Arr[w][i] = Arr[w][j]
                            Arr[w][j] = aux
                        

#Procedimiento utilizado para la busqueda de un nombre repetido si existe
def verifyName(nameShop):
    repeat = False
    col = 1
    comi = 0
    fin = totalShops
    while(fin >= comi and not repeat):
        medio = (comi + fin) // 2
        if(SHOPS[col][medio] == nameShop):
            repeat = True
        elif(SHOPS[col][medio] > nameShop):
            fin = medio - 1
        else:
            comi = medio + 1
    return repeat


#Procedure utilizado para mostrar la lista de locales.
def showShops():
    show = input("Desea ver los locales creados hasta el momento? S: para si, N: para no: ").upper()
    while show != "S" and show != "N":
        print(show)
        show = input("El codigo ingresado no es valido, desea ver los locales creados hasta el momento? S: para si, N: para no: ").upper()
    if(show == "S"):
            if(totalShops == 0):
                print("No hay locales creados hasta el momento")
            else:
                for j in range(0,totalShops):
                    print("+-----------------------------------------------------------------------------------------------------------+")
                    print(f"CODIGO: {SHOPS[0][j]}\nNOMBRE: {SHOPS[1][j]}\nLOCALIZACION: {SHOPS[2][j]}\nRUBRO: {SHOPS[3][j]}\nDUEÑO: {SHOPS[4][j]}\nESTADO: {SHOPS[5][j]}")
                print("+-----------------------------------------------------------------------------------------------------------+")


       
#Procedimiento que crea los locales y aumenta el contador dependiendo de su rubro
def createShop():
    global totalShops, SHOPS
    cleanWindow()
    separation()
    showShops()
    if(totalShops < 50):
        nameShop = input(f"Ingresar nombre del local o * para culminar: ")
        repeat = verifyName(nameShop)
        while repeat:
            print(f"El Nombre {nameShop} ya existe en los locales")
            nameShop = input(f"Ingresar nombre del local o * para culminar: ")
            repeat = verifyName(nameShop)
        while nameShop != '*':
            SHOPS[0][totalShops] = totalShops+1
            SHOPS[1][totalShops] = nameShop
            SHOPS[2][totalShops] = input("Ingresar localizacion del local (Piso, Ala, Sector): ")
            print("\n1) Indumentaria \n2) Perfumeria \n3) Comida")
            categoryShop = input("Ingresar numero del rubro del local: ")
            while categoryShop != "1" and categoryShop != "2" and categoryShop != "3":
                categoryShop=input("\nIngrese una de las opciones validas:")
            match categoryShop:
                case "1":
                    increase("Indumentaria")
                    SHOPS[3][totalShops]="Indumentaria"
                case "2":
                    increase("Perfumeria")
                    SHOPS[3][totalShops]="Perfumeria"
                case "3":
                    increase("Comida")
                    SHOPS[3][totalShops]="Comida"
            print("\n4) Dueño Local A \n6) Dueño Local B")
            dueñoShop = input("Ingresar codigo del dueño del local: ")
            while dueñoShop != "4" and dueñoShop != "6":
                dueñoShop=input("\nIngrese una de las opciones validas:")
            SHOPS[4][totalShops]=dueñoShop
            SHOPS[5][totalShops]="A"
            totalShops = totalShops + 1
            sort(SHOPS, totalShops, 5, False)
            sort(businessShop, 3, 2, True)
            cleanWindow()
            nameShop = input(f"Ingresar nombre del local o * para culminar: ")
            repeat = verifyName(nameShop)
            while repeat:
                print(f"El Nombre {nameShop} ya existe en los locales")
                nameShop = input(f"Ingresar nombre del local o * para culminar: ")
                repeat = verifyName(nameShop)
        cleanWindow()
        
def map():
    print("> MAPA DE LOCALES <")
    aux=""
    while aux != "*":
        indx=5
        for i in range(0,9):
                print("+-+-+-+-+-+")
                print(f"|{SHOPS[0][indx-5]}|{SHOPS[0][indx-4]}|{SHOPS[0][indx-3]}|{SHOPS[0][indx-2]}|{SHOPS[0][indx-1]}|")
                indx = indx+5
        print("+-+-+-+-+-+")
        aux=input("Ingrese * para salir: ")
        while aux != "*":
            aux=input("!OPCION INVALIDA¡ Ingrese * para salir: ")
            

#Procedimiento que aumenta la cantidad de locales por rubro
def increase(business):
    for k in range(0,3):
        if businessShop[0][k] == business:
            businessShop[1][k]=businessShop[1][k]+1
            

#Procedimiento que resta la cantidad de locales
def decrease(businness):
    for j in range(0,3):
        if businessShop[0][j] == businness:
            businessShop[1][j]=businessShop[1][j]-1
            
  
#Procedimiento que modifica locales
def modShop():
    global code, SHOPS
    showShops()
    exist = False
    while not exist:
        code = int(input("Ingrese el codigo del local que desea modificar o 0 para salir: "))
        if code != 0:
            for i in range(0, totalShops):
                if (SHOPS[0][i] == code):
                    exist = True
                    if(SHOPS[5][i] == "B"):
                        auxStatus = input(f"\nEl local con codigo '{SHOPS[0][i]}' se encuentra en BAJA, debe activarlo para modificarlo, desea hacerlo? A: para si, * para no: ")
                        if(auxStatus.lower() == "a"):
                            SHOPS[5][i] = "A"
                    if(SHOPS[5][i] == "A"):
                        print("\nEl codigo del local es valido y el local esta activado")
                        name = input(f"\nEl nombre actual del local es '{SHOPS[1][i]}',ingrese el nuevo nombre o de caso contrario ingrese *: ")
                        if (name != "*"):
                            repeat = verifyName(name)
                            while repeat:
                                print(f"El Nombre {name} ya existe en los locales")
                                name = input(f"Ingresar otro nombre del local: ")
                                repeat = verifyName(name)
                            SHOPS[1][i] = name 
                        location = input(f"\nLa ubicacion actual del local es '{SHOPS[2][i]}',ingrese la nueva localizacion o de caso contrario ingrese *: ")
                        if (location != "*"):
                            SHOPS[2][i] = location   
                        business = input(f"\nEl rubro actual del local es '{SHOPS[3][i]}',ingrese * para mantenerlo o cualquier tecla para cambiarlo: ")
                        if (business != "*"):
                            decrease(SHOPS[3][i])
                            print("\n1) Indumentaria \n2) Perfumeria \n3) Comida")
                            businessAux = input("Ingresar numero del nuevo rubro del local: ")
                            while businessAux != "1" and businessAux != "2" and businessAux != "3":
                                businessAux=input("\nIngrese una de las opciones validas:")
                            match businessAux:
                                case "1": 
                                    increase("Indumentaria")
                                    SHOPS[3][i] = "Indumentaria"
                                case "2":
                                    increase("Perfumeria")
                                    SHOPS[3][i] = "Perfumeria"
                                case "3":
                                    increase("Comida")
                                    SHOPS[3][i] = "Comida" 
                        owner = input(f"\nEl dueño actual del local es '{SHOPS[4][i]}',ingrese el nuevo codigo de dueño o de caso contrario ingrese *: ")
                        if (owner != "*"):
                            print("\n4) Dueño Local A \n6) Dueño Local B")
                            owner = input("Ingresar codigo del dueño del local: ")
                            while owner != "4" and owner != "6":
                                owner=input("\nIngrese una de las opciones validas:")
                            SHOPS[4][i] = owner
                    sort(SHOPS, totalShops, 5, False)
                    sort(businessShop, 3, 2, True)
        else:
            exist = True
        if (not exist):
            print("El codigo de local no es valido")
            
#Procedimiento que cambia el estado de un local para eliminarlo
def deleteShop():
    global SHOPS
    showShops()
    exist = False
    while not exist:
        code = int(input("Ingrese el codigo del local que desea dar de BAJA o 0 para salir: "))
        if code != 0:
            for i in range(0, totalShops):
                if (SHOPS[0][i] == code):
                    exist = True
                    if(SHOPS[5][i] == "A"):
                        auxDelete=input(f"Esta seguro que desea dar de BAJA al local con el codigo '{SHOPS[0][i]}', presione B: para si, * para no: ")
                        if(auxDelete.lower() == "b"):
                            SHOPS[5][i] = "B"
                            decrease(SHOPS[3][i])
                            print(f"El local con codigo '{SHOPS[0][i]}' fue dado de BAJA")
                    else:
                        print(f"El local con el codigo '{SHOPS[0][i]}' ya esta dado de BAJA")
        else:
            exist = True
        if (not exist):
            print("El codigo de local no es valido")

#Programa principal
inicialization()
while(type_user == ""):
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