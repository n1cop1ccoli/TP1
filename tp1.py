# Integrantes
# Bercini Genaro, Egidi Kevin, Piccoli jlas

import getpass
import os
import pickle
import io
import os.path


class Users:
        def _init_(self):
            self.code: 0
            self.user: "0"
            self.key: "0"
            self.type: "0"

class Shops:
    def _init_(self):
        self.codShop: 0
        self.name: "0"
        self.location: "0"
        self.category: "0"
        self.codUser: 0
        self.status: "0"
            
      
#Variables utilizadas globalmente en todo el programa.

def openFiles():
    global ffUsers, lfUsers, ffShops, lfShops
    #ffUsers = "D:\\Gena\\TP1\\users.dat"
    ffUsers = "C:\\Users\\nicop\\OneDrive\\Escritorio\\ALGORITMOS\\TP1\\users.dat"
    lfUsers = open(ffUsers, "w+b")
    #ffShops = "D:\\Gena\\TP1\\shops.dat"
    ffShops = "C:\\Users\\nicop\\OneDrive\\Escritorio\\ALGORITMOS\\TP1\\shops.dat"
    lfShops = open(ffShops, "w+b")

def closeFiles():
     lfUsers.close()
     lfShops.close()

def inicialization():
    global user ,ffUsers,lfUsers, count, type_menu, menu_admin,SHOPS, opcion_owner, opcion_customer, totalShops, businessShop, code, user, shop
    openFiles()
    shop = Shops()
    user = Users()
    user.code = 1
    user.user = "admin"
    user.key = "12345"
    user.type = "administrador"
    formatEntity("user", user)
    pickle.dump(user,lfUsers)
    lfUsers.flush()
    
    SHOPS = [['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']]
    totalShops = 0
    count = 3
    code = 0
    pointUser = 0
    type_menu = ""
    opcion_owner= "1"
    opcion_customer= "1"
    menu_admin = "1"
    businessShop=[["Indumentaria", "Perfumeria", "Comida"], [0,0,0]]
    spaceShops()
#Procedimiento para llenar la tabla de locales con espacios disponibles
def spaceShops():
    for i in range(0,6):
        for j in range(0,50):
            SHOPS[i] = "0"
    

#Procedimieno que dependiendo del sistema operativo limpia la terminal
def cleanWindow():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#Procedimiento utilizado para separar contenidos del programa.
def separation():
    print("-------------------------------------------------------------------------------------------------------------")
    
def validate_user(mail):
    global user
    flag = False
    limUsers = os.path.getsize(ffUsers)
    lfUsers.seek(0)
    while lfUsers.tell() < limUsers and flag == False:
        # pointUser = lfUsers.tell()
        user = pickle.load(lfUsers)
        if mail == user.user:
            flag = True
    return flag
        
# Procedimiento que valida si un dueño de local existe
def validate_owner(cod):
    global user
    flag = False
    limUsers = os.path.getsize(ffUsers)
    lfUsers.seek(0)
    while lfUsers.tell() < limUsers and flag == False:
        # pointUser = lfUsers.tell()
        user = pickle.load(lfUsers)
        if(cod == user.code):
            # if(user.type == "dueño               "):
            flag = True
    return flag
    
#Procedimiento para validar el usuario y contraseña, y verificar cantidad de intentos.
def validation(typeUser):
    global ffUsers,count,type_menu,lfUsers, workUser,pointUser,user
    cleanWindow()
    while (count > 0): 
        current_menu(typeUser)
        user_vd = input("Ingrese su usuario: ").ljust(100, " ")
        password_vd = getpass.getpass("Ingrese su contraseña: ").ljust(8, " ")
        flag = validate_user(user_vd)   
        if flag == True and password_vd == user.key:
            match user.type:
                case "administrador       ":
                    menu()
                case "cliente             ":
                    menu_customer()
                case "dueño             ":
                    menu_owner()
        
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
                
            
        
        
        
        # match typeUser:
        #     case "1":
        #         if(user_vd == USERS[1][0] and password_vd == USERS[2][0]):
        #             cleanWindow()
        #             current_menu("1")
        #             menu()
        #             count = 0
        #     case "2":
        #         if(user_vd == USERS[1][1] and password_vd == USERS[2][1] or user_vd == USERS[1][2] and password_vd == USERS[2][2]):
        #             cleanWindow()
        #             current_menu("2")
        #             menu_owner()
        #             count = 0
        #     case "3":
        #         if(user_vd == USERS[1][3] and password_vd == USERS[2][3]):
        #             cleanWindow()
        #             current_menu("3")
        #             menu_customer()
        #             count = 0
        # if (count != 0):
        #      if count == 1:
        #         count = count - 1
        #         separation()
        #         print("\nUsted ya alcanzo el limite de intentos, lo sentimos el programa se ha cerrado\n")
        #         separation()
        #      else:
        #         count = count - 1
        #         separation()
        #         print(f"\nEl usuario o contraseña son incorrectos le quedan {count} intentos.\n")
        #         separation()
                
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
    cleanWindow()
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
                shopsMenu()
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
def shopsMenu():
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

def sort_shops():
    global ffUsers,lfUsers
    lfUsers.seek (0)
    aux = pickle.load(lfUsers)
    tamReg = lfUsers.tell() 
    tamArch = os.path.getsize(ffUsers)
    cantReg = int(tamArch / tamReg)  
    for i in range(0, cantReg-1):
        for j in range (i+1, cantReg):
            lfUsers.seek (i*tamReg, 0)
            auxi = pickle.load(lfUsers)
            lfUsers.seek (j*tamReg, 0)
            auxj = pickle.load(lfUsers)
            if (auxi.name < auxj.name):
                lfUsers.seek (i*tamReg, 0)
                pickle.dump(auxj, lfUsers)
                lfUsers.seek (j*tamReg, 0)
                pickle.dump(auxi,lfUsers)
                lfUsers.flush()

#Procedimiento utilizado para el ordenamiento de el array de locales
# def sort(Arr, lim, totalCol, Desc):
#     col= 1
#     if(lim > 1):
#         for i in range (0, lim):
#             for j in range(i+1, lim):
#                 if(Desc):
#                     if(Arr[col][i] < Arr[col]):
#                         for w in range(0,totalCol):
#                             aux = Arr[w][i]
#                             Arr[w][i] = Arr[w]
#                             Arr[w] = aux
#                 else:
#                     if(Arr[col][i] > Arr[col]):
#                         for w in range(0,totalCol):
#                             aux = Arr[w][i]
#                             Arr[w][i] = Arr[w]
#                             Arr[w] = aux
                        
#Procedimiento utilizado para formatear los datos de usuarios
def formatEntity(typeEntity, entity):
    if(typeEntity == "user"):
        entity.user = str(entity.user)[:100].ljust(100, " ")
        entity.key = str(entity.key)[:8].ljust(8, " ")
        entity.type = str(entity.type)[:20].ljust(20, " ")
    if(typeEntity == "shop"):
        entity.name = str(entity.name)[:50].ljust(50, "a")
        entity.location = str(entity.location)[:50].ljust(50, "a")
        entity.category = str(entity.category)[:50].ljust(50, "a")
        entity.status = str(entity.status)[:1]


    

#Procedimiento utilizado para la busqueda de un nombre repetido si existe
def verifyName(nameShop):
    global lfShops, ffShops, shop
    repeat = False
    lim = os.path.getsize(ffShops)
    if(lim != 0):
        lfShops.seek(0)
        shop = pickle.load(lfShops)
        sizeReg = lfShops.tell()
        cantR = lim // sizeReg
        start = 0
        end = cantR-1
        while(end >= start and not repeat):
            mid = (start + end) // 2
            lfShops.seek(mid * sizeReg, 0)
            shop = pickle.load(lfShops)
            print("1",shop.name)
            print("2",nameShop)
            if(shop.name == nameShop):
                repeat = True
                print("3",shop.name)
            elif(shop.name > nameShop):
                end = mid - 1
                print("4",shop.name)
            else:
                start = mid + 1
                print("5",shop.name)
    print(repeat)
    return repeat


#Procedure utilizado para mostrar la lista de locales.
def showShops():
    global shop
    show = input("Desea ver los locales creados hasta el momento? S: para si, N: para no: ").upper()
    while show != "S" and show != "N":
        print(show)
        show = input("El codigo ingresado no es valido, desea ver los locales creados hasta el momento? S: para si, N: para no: ").upper()
    if(show == "S"):
        limShop = os.path.getsize(ffShops)
        lfShops.seek(0)
        while lfShops.tell() < limShop:
            shop = pickle.load(lfShops)
            print("+-----------------------------------------------------------------------------------------------------------+")
            print(f"CODIGO: {shop.code}\nNOMBRE: {shop.name}\nLOCALIZACION: {shop.location}\nRUBRO: {shop.category}\nDUEÑO: {shop.codUser}\nESTADO: {shop.status}")
            print("+-----------------------------------------------------------------------------------------------------------+")


       
#Procedimiento que crea los locales y aumenta el contador dependiendo de su rubro
def createShop():
    global totalShops, SHOPS, lfShops, ffShops, shop
    cleanWindow()
    separation()
    nameShop = input(f"Ingresar nombre del local o * para culminar: ").ljust(50, "a")
    print("name",nameShop)
    while nameShop != '*aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa':
        repeat = verifyName(nameShop)
        while repeat:
            print(f"El Nombre {nameShop} ya existe en los locales")
            nameShop = input(f"Ingresar nombre del local o * para culminar: ")
            repeat = verifyName(nameShop)
        shop = Shops()
        shop.code = count_entity("shop")
        shop.name = nameShop
        shop.location = input("Ingresar localizacion del local (Piso, Ala, Sector): ")
        print("\n1) Indumentaria \n2) Perfumeria \n3) Comida")
        categoryShop = input("Ingresar numero del rubro del local: ")
        while categoryShop != "1" and categoryShop != "2" and categoryShop != "3":
            categoryShop=input("\nIngrese una de las opciones validas:")
        match categoryShop:
            case "1":
                # increase("Indumentaria")
                shop.category ="Indumentaria"
            case "2":
                # increase("Perfumeria")
                shop.category ="Perfumeria"
            case "3":
                # increase("Comida")
                shop.category ="Comida"
        ownerShop = int(input("Ingresar codigo del dueño del local: "))
        exist = validate_owner(ownerShop)
        while exist == False:
            ownerShop = int(input("Ingresar codigo del dueño del local: "))
            exist = validate_owner(ownerShop)
        shop.codUser = ownerShop
        shop.status = "A"
        formatEntity("shop", shop)
        pickle.dump(shop,lfShops)
        lfShops.flush()
        cleanWindow()
        sort_shops()
        nameShop = input(f"Ingresar nombre del local o * para culminar: ").ljust(50,"a")
        
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
        if businessShop[0] == businness:
            businessShop[1]=businessShop[1]-1
            
def verify_shop(cod):
    global shop,ffShops, lfShops
    flag = False
    limShop = os.path.getsize(ffShops)
    if limShop != 0:
        lfShops.seek(0)
        while lfShops.tell() < limShop and flag == False:
            shop = pickle.load(lfShops)
            if(cod == shop.code):
                flag = True
    return flag
  
def search_shop(cod):
    global lfShops, ffShops,shop
    repeat = False
    lim = os.path.getsize(ffShops)
    if(lim != 0):
        lfShops.seek(0)
        shop = pickle.load(lfShops)
        sizeReg = lfShops.tell()
        cantR = lim // sizeReg
        start = 0
        end = cantR-1
        while(end >= start and not repeat):
            mid = (start + end) // 2
            lfShops.seek(mid * sizeReg, 0)
            punShop = lfShops.tell()
            shop = pickle.load(lfShops)
            if(shop.code == cod):
                repeat = True
            elif(shop.code > cod):
                end = mid - 1
            else:
                start = mid + 1
    return punShop
                
#Procedimiento que modifica locales
def modShop():
    SHOPS, lfShops, ffShops
    showShops()
    codShop = int(input("Ingrese el codigo del local que quiere modificar o 0 para culminar: "))
    while codShop != 0:
        repeat = verify_shop(codShop)
        while not repeat:
            print(f"El codigo {codShop} no se encuentra en el sistema")
            codShop = int(input(f"Ingrese el codigo del local o 0 para culminar: "))
            if codShop == 0:
                repeat = True
            else:
                repeat = verify_shop(codShop)
        if codShop != 0:
            position_shop = search_shop(codShop)
            shop = Shops()
            lfShops.seek(position_shop)
            punShop = lfShops.tell()
            shop = pickle.load(lfShops)  
            print("code",shop.code)
            print("name",shop.name)
            print("estado",shop.status)
            if shop.status == "B":
                current_status = input(f"\nEl local con codigo {shop.code} se encuentra en BAJA, debe activarlo para modificarlo, desea hacerlo? A: para si, * para no: ")
                if(current_status.lower() == "a"):
                    shop.code = "A"
            if shop.status == "A":
                print("codeeee",shop.code)
                print("\nEl codigo del local es valido y el local esta activado")
                nameShop= input(f"\nEl nombre actual del local es '{shop.name}',ingrese el nuevo nombre o de caso contrario ingrese *: ").ljust(50,"a")
                if (nameShop != "*aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"):
                    repeat = verifyName(nameShop)
                    while repeat:
                        print(f"El Nombre {nameShop} ya existe en los locales")
                        nameShop = input(f"Ingresar el nuevo nombre del local: ").ljust(50, "a") 
                        repeat = verifyName(nameShop)
                    shop.name = nameShop
                new_location = input(f"\nLa ubicacion actual del local es '{shop.location}',ingrese la nueva localizacion o de caso contrario ingrese *: ").ljust(50, "a")
                if new_location != "*aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa":
                    shop.location = new_location 
                new_category = input(f"\nEl rubro actual del local es '{shop.category}',ingrese * para mantenerlo o cualquier tecla para cambiarlo: ").ljust(50, "a")
                if new_category  != "*aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa":
                    print("\n1) Indumentaria \n2) Perfumeria \n3) Comida")
                    categoryShop = input("Ingresar numero del rubro del local: ")
                    while categoryShop != "1" and categoryShop != "2" and categoryShop != "3":
                        categoryShop=input("\nIngrese una de las opciones validas:")
                    match categoryShop:
                        case "1":
                            # increase("Indumentaria")
                            shop.category ="Indumentaria"
                        case "2":
                            # increase("Perfumeria")
                            shop.category ="Perfumeria"
                        case "3":
                            # increase("Comida")
                            shop.category ="Comida"
                new_owner = int(input(f"\nEl dueño actual del local es '{shop.codUser}',ingrese el nuevo codigo de dueño o de caso contrario ingrese 0: "))
                if (new_owner != 0):
                    exist = validate_owner(new_owner)
                    while exist == False:
                        new_owner = int(input("El dueño que quiere ingresar no existe, ingrese un codigo del dueño del local valido: "))
                        exist = validate_owner(new_owner)
                    shop.codUser = new_owner
                formatEntity("shop", shop)
                lfShops.seek(punShop,io.SEEK_SET)
                pickle.dump(shop,lfShops)
                lfShops.flush()
                cleanWindow()
                showShops()
        codShop = int(input("Ingrese el codigo del local que quiere modificar o 0 para culminar: "))
        
    # global code, SHOPS
    # showShops()
    # exist = False
    # while not exist:
    #     code = int(input("Ingrese el codigo del local que desea modificar o 0 para salir: "))
    #     if code != 0:
    #         for i in range(0, totalShops):
    #             if (SHOPS[0][i] == code):
    #                 exist = True
    #                 if(SHOPS[5][i] == "B"):
    #                     auxStatus = input(f"\nEl local con codigo '{SHOPS[0][i]}' se encuentra en BAJA, debe activarlo para modificarlo, desea hacerlo? A: para si, * para no: ")
    #                     if(auxStatus.lower() == "a"):
    #                         SHOPS[5][i] = "A"
    #                 if(SHOPS[5][i] == "A"):
    #                     print("\nEl codigo del local es valido y el local esta activado")
    #                     name = input(f"\nEl nombre actual del local es '{SHOPS[1][i]}',ingrese el nuevo nombre o de caso contrario ingrese *: ")
    #                     if (name != "*"):
    #                         repeat = verifyName(name)
    #                         while repeat:
    #                             print(f"El Nombre {name} ya existe en los locales")
    #                             name = input(f"Ingresar otro nombre del local: ")
    #                             repeat = verifyName(name)
    #                         SHOPS[1][i] = name 
    #                     location = input(f"\nLa ubicacion actual del local es '{SHOPS[2][i]}',ingrese la nueva localizacion o de caso contrario ingrese *: ")
    #                     if (location != "*"):
    #                         SHOPS[2][i] = location   
    #                     business = input(f"\nEl rubro actual del local es '{SHOPS[3][i]}',ingrese * para mantenerlo o cualquier tecla para cambiarlo: ")
    #                     if (business != "*"):
    #                         decrease(SHOPS[3][i])
    #                         print("\n1) Indumentaria \n2) Perfumeria \n3) Comida")
    #                         businessAux = input("Ingresar numero del nuevo rubro del local: ")
    #                         while businessAux != "1" and businessAux != "2" and businessAux != "3":
    #                             businessAux=input("\nIngrese una de las opciones validas:")
    #                         match businessAux:
    #                             case "1": 
    #                                 increase("Indumentaria")
    #                                 SHOPS[3][i] = "Indumentaria"
    #                             case "2":
    #                                 increase("Perfumeria")
    #                                 SHOPS[3][i] = "Perfumeria"
    #                             case "3":
    #                                 increase("Comida")
    #                                 SHOPS[3][i] = "Comida" 
    #                     owner = input(f"\nEl dueño actual del local es '{SHOPS[4][i]}',ingrese el nuevo codigo de dueño o de caso contrario ingrese *: ")
    #                     if (owner != "*"):
    #                         print("\n4) Dueño Local A \n6) Dueño Local B")
    #                         owner = input("Ingresar codigo del dueño del local: ")
    #                         while owner != "4" and owner != "6":
    #                             owner=input("\nIngrese una de las opciones validas:")
    #                         SHOPS[4][i] = owner
    #                 sort(SHOPS, totalShops, 5, False)
    #                 sort(businessShop, 3, 2, True)
    #     else:
    #         exist = True
    #     if (not exist):
    #         print("El codigo de local no es valido")
            
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

def sing_up():
    global user,Users,lfUsers,ffUsers
    cleanWindow()
    new_user = input("Ingrese el correo a registrar: ")
    flag = validate_user(new_user)
    while flag == True:
        new_user = input("El mail que intenta registrar ya existe, ingrese otro: ")
        flag = validate_user(new_user)
    new_password = input("Ingrese la contraseña a registrar: ")
    user = Users()
    user.code = count_entity()
    user.user = new_user
    user.key = new_password
    user.type = "cliente"
    formatEntity("user", user)
    pickle.dump(user,lfUsers)
    lfUsers.flush()

def count_entity(typeEntity):
    global user, ffUsers, lfUsers, shop, ffShops, lfShops
    if(typeEntity == "user"):
        lim = os.path.getsize(ffUsers)
        lfUsers.seek(0)
        user = pickle.load(lfUsers)
        treg = lfUsers.tell()
        longe = lim - treg
        lfUsers.seek(longe)
        user = pickle.load(lfUsers)
        return user.code+1
    if(typeEntity == "shop"):
        lim = os.path.getsize(ffShops)
        if( lim != 0):
           lfShops.seek(0)
           shop = pickle.load(lfShops)
           treg = lfShops.tell()
           longe = lim - treg
           lfShops.seek(longe)
           shop = pickle.load(lfShops)
           return shop.code+1
        return 1

#Programa principal
inicialization()

while(type_menu == ""):
    print("1) Ingresar como usario registrado  \n2) Registrarse como cliente \n3) Salir")
    type_menu= input("Ingrese la manera con la cual quiere ingresar: ")
    while(type_menu != "1" and type_menu != "2" and type_menu != "3" and type_menu != "0"):
        type_menu=input("\nIngrese una de las opciones validas:")
    match type_menu:
        case "1":
            validation(type_menu)
        case "2":
            sing_up()
            type_menu= ""    
        case "3":
            cleanWindow()
            separation()
            print("Saliste del programa.")