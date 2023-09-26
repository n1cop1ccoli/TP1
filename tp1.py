# Integrantes
# Bercini Genaro, Egidi Kevin, Piccoli nicolás

import getpass
import os
import pickle
import io
import os.path
from datetime import datetime, timedelta
from datetime import date



class Users:
    def _init_(self):
        self.code: 0
        self.user: "0"
        self.key: "0"
        self.type: "0"

class Shops:
    def _init_(self):
        self.code: 0
        self.name: "0"
        self.location: "0"
        self.category: "0"
        self.codUser: 0
        self.status: "0"

class Promotions:
    def _init_(self):
        self.codPromo: 0
        self.textPromo: "0"
        self.dateSince: "0"
        self.dateUntil: "0"
        self.weekDay: [0,0,0,0,0,0,0,0]
        self.status: "0"
        self.code: 0
      
#Variables utilizadas globalmente en todo el programa.

def openFiles():
    global ffUsers, lfUsers, ffShops, lfShops,lfProm, ffProm
    #ffUsers = "D:\\Gena\\TP1\\users.dat"
    ffUsers = "C:\\Users\\nicop\\OneDrive\\Escritorio\\ALGORITMOS\\TP1\\users.dat"
    lfUsers = open(ffUsers, "w+b")
    ffProm = "C:\\Users\\nicop\\OneDrive\\Escritorio\\ALGORITMOS\\TP1\\promotions.dat"
    lfProm = open(ffProm, "w+b")
    #ffShops = "D:\\Gena\\TP1\\shops.dat"
    ffShops = "C:\\Users\\nicop\\OneDrive\\Escritorio\\ALGORITMOS\\TP1\\shops.dat"
    lfShops = open(ffShops, "w+b")

def closeFiles():
     lfUsers.close()
     lfShops.close()

def inicialization():
    global user ,ffUsers,lfUsers, count, type_menu, menu_admin,SHOPS, opcion_owner, opcion_customer, totalShops, businessShop, code, user, shop, Promo
    openFiles()
    shop = Shops()
    promo = Promotions()
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
    global user, pointUser
    flag = False
    limUsers = os.path.getsize(ffUsers)
    lfUsers.seek(0)
    while lfUsers.tell() < limUsers and flag == False:
        pointUser = lfUsers.tell()
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
        pointUser = lfUsers.tell()
        user = pickle.load(lfUsers)
        if(cod == user.code):
                if(user.type == "dueño               "):
                    flag = True
                    
    return flag
    
#Procedimiento para validar el usuario y contraseña, y verificar cantidad de intentos.
def validation(typeUser):
    global ffUsers,count,type_menu,lfUsers, workUser,pointUser,user, opcion_customer, opcion_owner, menu_admin
    cleanWindow()
    count = 3
    while (count > 0): 
        current_menu(typeUser)
        user_vd = input("Ingrese su usuario: ").ljust(100, " ")
        password_vd = getpass.getpass("Ingrese su contraseña: ").ljust(8, " ")
        flag = validate_user(user_vd)   
        if flag == True and password_vd == user.key:
            match user.type:
                case "administrador       ":
                    menu()
                    count = 0
                    menu_admin = "1"
                case "cliente             ":
                    menu_customer()
                    count = 0
                    opcion_customer= "1"
                case "dueño               ":
                    menu_owner()
                    count = 0
                    opcion_owner= "1"
            
        
        elif (count != 0):
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

def verifyCode(codeShop,userCode):
    flag = False
    limShop = os.path.getsize(ffShops)
    lfShops.seek(0)
    while lfShops.tell() < limShop and flag == False:
        shop = pickle.load(lfShops)
        if (shop.codUser == userCode and shop.code == codeShop):
            flag = True
    return flag
            

def showProm(point):
    global ffProm,lfProm, promo, lfUsers,ffUsers
    limProm = os.path.getsize(ffProm)
    if limProm != 0:
        lfProm.seek(0) 
        lfUsers.seek(point)
        user = pickle.load(lfUsers)
        while lfProm.tell() < limProm:
            promo = pickle.load(lfProm)
            flag = verifyCode(promo.code,user.code)
            if flag == True:
                print("+-----------------------------------------------------------------------------------------------------------+")
                print(f"CODIGO DE PROMO: {promo.codPromo}\nDESCRIPCIÓN: {promo.textPromo}\nFECHA DE INCICIO: {promo.dateSince}\nFECHA DE FINALIZACIÓN: {promo.dateUntil}\nDÍAS DE DESCUENTO: \nLUNES:{promo.weekDay[0]} \nMARTES:{promo.weekDay[1]} \nMIERCOLES:{promo.weekDay[2]} \nJUEVES:{promo.weekDay[3]} \nVIERNES:{promo.weekDay[4]} \nSABADO:{promo.weekDay[5]} \nDOMINGO:{promo.weekDay[6]}  \nESTADO: {promo.status} \nCODIGO LOCAL:{promo.code}")
                print("+-----------------------------------------------------------------------------------------------------------+")
    else:
        print("No hay promociones cargadas hasta el momento.")  
    
              
def createProm():
    global pointUser
    showProm(pointUser)
    promo = Promotions()
    descrption = input(f"Ingresar la descipción de la promoción o * para culminar: ").ljust(20, " ")
    while descrption != "*                   ":
        promo.textPromo = descrption
        flag = False
        promo.codPromo = count_entity("promo")
        while flag == False:
            dateSince = input("Ingrese fecha de comienzo de la promocion (dd-mm-aaaa): ")
            dateSin= datetime.strptime(dateSince, "%d-%m-%Y").date()
            dateUntil = input("Ingrese fecha de culminacion de la promocion (dd-mm-aaaa): ")
            dateUnt = datetime.strptime(dateUntil, "%d-%m-%Y").date()
            today = date.today()
            if dateSin <= dateUnt and dateSin >= today:
                flag = True
                promo.dateSince = dateSin
                promo.dateUntil = dateUnt
            else:
                print("La fecha es invalida, ingrese una fecha de inicio que sea mayor o igual a la fecha del día de hoy y una fecha de finalizacion que sea mayor o igual a la fecha de inicio")
        print("Ingrese el numero 1 para los días de la semana que la oferta sea valida y un 0 para aquellos en los que no")
        auxWeek= [0,0,0,0,0,0,0]
        auxDay= ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
        for i in range (0,7):
            print(f"Día {auxDay[i]}")
            auxDays = int(input("Ingrese 1 o 0: "))
            while auxDays != 1 and auxDays != 0:
                auxDays = int(input("La opcion que ingreso no corresponde, ingrese una de las opciones validas 1 o 0: "))
            auxWeek[i] = auxDays
        promo.weekDay = auxWeek
        promo.status = "Pendiente"
        auxCodShop = int(input("Ingrese el codigo del local al cual le quiere aplicar la promocion: "))
        codFlag = False
        while codFlag == False: 
            lfUsers.seek(pointUser)
            user = pickle.load(lfUsers)
            codFlag = verifyCode(auxCodShop,user.code)
            if codFlag == False:
                auxCodShop = int(input("El codigo del local que ingreso no es valido, por favor ingrese otro: "))
        promo.code = auxCodShop
        formatEntity("promo", promo)
        pickle.dump(promo,lfProm)
        lfProm.flush()
        print(promo.code)
        descrption = input(f"Si desea crear otra promocion ingrese su descipción o * para culminar: ").ljust(20, " ")

    
    
#Procedimeinto que muestra el menu para dueño de local
def menu_owner():
    global opcion_owner
    while opcion_owner != "0" and opcion_owner != "d":
        print("\n1) Crear descuento \n2) Reporte de uso de descuento\n3) Ver novedades \n0) Salir")
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
                createProm()
                separation()
            case "2":
                cleanWindow()
                print("En construccion...")
                separation()
            case "3":
                cleanWindow()
                print("Diagramado en chapín")
                separation()
            


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
                sing_up("dueño")
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
    global ffShops,lfShops
    lfShops.seek (0)
    aux = pickle.load(lfShops)
    tamReg = lfShops.tell() 
    tamArch = os.path.getsize(ffShops)
    cantReg = int(tamArch / tamReg)  
    for i in range(0, cantReg-1):
        for j in range (i+1, cantReg):
            lfShops.seek (i*tamReg, 0)
            auxi = pickle.load(lfShops)
            lfShops.seek (j*tamReg, 0)
            auxj = pickle.load(lfShops)
            if (auxi.name > auxj.name):
                lfShops.seek (i*tamReg, 0)
                pickle.dump(auxj, lfShops)
                lfShops.seek (j*tamReg, 0)
                pickle.dump(auxi,lfShops)
                lfShops.flush()
                        
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
    if (typeEntity == "promo"):
        entity.textPromo = str(entity.textPromo)[:20].ljust(20, " ")
        entity. dateSince = str(entity.dateSince)[:10]
        entity. dateUntil =  str(entity.dateUntil)[:10]
        entity.status = str(entity.status)[:10].ljust(10, " ")
        


    

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
            if(shop.name == nameShop):
                repeat = True
            elif(shop.name > nameShop):
                end = mid - 1
            else:
                start = mid + 1
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
        print(shop.code)
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
    global ffShops,lfShops
    print("> MAPA DE LOCALES <") 
    exit=""
    while exit != "*":
        fil = 0
        col = 0
        aux=[0,0,0,0,0]
        aux[0] = colorizar_texto(str(aux[0]), "amarillo")
        aux[1] = colorizar_texto(str(aux[0]), "amarillo")
        aux[2] = colorizar_texto(str(aux[0]), "amarillo")
        aux[3] = colorizar_texto(str(aux[0]), "amarillo")
        aux[4] = colorizar_texto(str(aux[0]), "amarillo")
        lim = os.path.getsize(ffShops)
        lfShops.seek(0)
        while fil < 10:
            while lfShops.tell() < lim:
                while col < 5 and lfShops.tell() < lim:
                    shop = pickle.load(lfShops)
                    if(shop.status == "A"):
                        aux[col] = shop.code
                        aux[col] = colorizar_texto(str(aux[col]), "verde")
                    else:
                        aux[col] = shop.code
                        aux[col] = colorizar_texto(str(aux[col]), "rojo")
                    col = col +1
                print("+-+-+-+-+-+")
                print(f"|{aux[0]}|{aux[1]}|{aux[2]}|{aux[3]}|{aux[4]}|")
                aux=[0,0,0,0,0]
                aux[0] = colorizar_texto(str(aux[0]), "amarillo")
                aux[1] = colorizar_texto(str(aux[0]), "amarillo")
                aux[2] = colorizar_texto(str(aux[0]), "amarillo")
                aux[3] = colorizar_texto(str(aux[0]), "amarillo")
                aux[4] = colorizar_texto(str(aux[0]), "amarillo")
                col = 0
                fil = fil +1
            aux=[0,0,0,0,0]
            aux[0] = colorizar_texto(str(aux[0]), "amarillo")
            aux[1] = colorizar_texto(str(aux[0]), "amarillo")
            aux[2] = colorizar_texto(str(aux[0]), "amarillo")
            aux[3] = colorizar_texto(str(aux[0]), "amarillo")
            aux[4] = colorizar_texto(str(aux[0]), "amarillo")
            fil = fil +1
            print("+-+-+-+-+-+")
            print(f"|{aux[0]}|{aux[1]}|{aux[2]}|{aux[3]}|{aux[4]}|")
        print("+-+-+-+-+-+")
        exit=input("Ingrese * para salir: ")
        while exit != "*":
            exit=input("!OPCION INVALIDA¡ Ingrese * para salir: ")


def colorizar_texto(texto, color):
    colores = {
        'reset': '\033[0m',
        'negro': '\033[30m',
        'rojo': '\033[31m',
        'verde': '\033[32m',
        'amarillo': '\033[33m',
        'azul': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'blanco': '\033[37m'
    }
    return f"{colores[color]}{texto}{colores['reset']}"
    
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
        while lfShops.tell() < lim and repeat == False:
            pointShop = lfShops.tell()
            shop = pickle.load(lfShops)
            if (shop.code == cod):
                punShop = pointShop
                repeat = True
    else:
        punShop = lfShops.tell()
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
            if shop.status == "B":
                current_status = input(f"\nEl local con codigo {shop.code} se encuentra en BAJA, debe activarlo para modificarlo, desea hacerlo? A: para si, * para no: ")
                if(current_status.lower() == "a"):
                    shop.code = "A"
            if shop.status == "A":
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
                sort_shops()
                showShops()
        codShop = int(input("Ingrese el codigo del local que quiere modificar o 0 para culminar: "))
    
def deleteShop():
    global SHOPS, shop
    showShops()
    codShop = int(input("Ingrese el codigo del local que desea dar de BAJA o 0 para salir: "))
    if(codShop != 0):
        print(codShop)
        exist = verify_shop(codShop)
        if(exist == True):
            position_shop = search_shop(codShop)
            shop = Shops()
            lfShops.seek(position_shop)
            punShop = lfShops.tell()
            shop = pickle.load(lfShops)
            print(shop.name)
            print(shop.status)
            if(shop.status == "A"):
                auxDelete=input(f"Esta seguro que desea dar de BAJA al local con el codigo '{codShop}', presione B: para si, * para no: ")
                while auxDelete != '*' and auxDelete.lower() != 'b':
                    print(f'Opcion {auxDelete} no valida')
                    auxDelete=input(f"Esta seguro que desea dar de BAJA al local con el codigo '{codShop}', presione B: para si, * para no: ")
                if(auxDelete.lower() == "b"):
                    shop.status = "B"
                    print(f"El local con codigo '{codShop}' fue dado de BAJA")
            else:
                  print(f"El local con el codigo '{codShop}' ya esta dado de BAJA")
        print(shop.name)
        print(shop.status)
        lfShops.seek(punShop,io.SEEK_SET)
        pickle.dump(shop,lfShops)
        lfShops.flush()
            
def sing_up(typeUser):
    global user,Users,lfUsers,ffUsers
    cleanWindow()
    new_user = input("Ingrese el correo a registrar: ").ljust(100, " ")
    flag = validate_user(new_user)
    while flag == True:
        new_user = input("El mail que intenta registrar ya existe, ingrese otro: ").ljust(100, " ")
        flag = validate_user(new_user)
    new_password = input("Ingrese la contraseña a registrar: ").ljust(8, " ")
    user = Users()
    user.code = count_entity("user")
    user.user = new_user
    user.key = new_password
    if typeUser == "cliente":
        user.type = "cliente".ljust(20, " ")
    if typeUser == "dueño":
        user.type = "dueño".ljust(20, " ")
    formatEntity("user", user)
    pickle.dump(user,lfUsers)
    lfUsers.flush()

def count_entity(typeEntity):
    global user, ffUsers, lfUsers, shop, ffShops, lfShops,lfProm, ffProm,promo
    if(typeEntity == "user"):
        lim = os.path.getsize(ffUsers)
        lastCode = 0
        lfUsers.seek(0)
        while lfUsers.tell() < lim:
            user = pickle.load(lfUsers)
            if user.code > lastCode:
                lastCode = user.code
        return lastCode+1
    if(typeEntity == "shop"):
        lim = os.path.getsize(ffShops)
        if( lim != 0):
            lastCode = 0
            lfShops.seek(0)
            while lfShops.tell() < lim:
                shop = pickle.load(lfShops)
                if shop.code > lastCode:
                    lastCode = shop.code
            return lastCode+1
        return 1
    if(typeEntity == "promo"):
        lim = os.path.getsize(ffProm)
        if( lim != 0):
            lastCode = 0
            lfProm.seek(0)
            while lfProm.tell() < lim:
                promo = pickle.load(lfProm)
                if promo.codPromo > lastCode:
                    lastCode = promo.codPromo
            return lastCode+1
        return 1
        # lim = os.path.getsize(ffUsers)
        # lfUsers.seek(0)
        # user = pickle.load(lfUsers)
        # treg = lfUsers.tell()
        # longe = lim - treg
        # print(longe, treg, lim)
        # lfUsers.seek(longe)
        # print(lfUsers)
        # user = pickle.load(lfUsers)
        # return user.code+1

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
            type_menu = ""
        case "2":
            sing_up("cliente")
            type_menu= ""    
        case "3":
            cleanWindow()
            separation()
            print("Saliste del programa.")