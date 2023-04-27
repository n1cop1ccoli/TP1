import getpass

def inicialization():
    global user, password, count, type_user, admin
    user = "admin"
    password= 12345
    count = 0   
    type_user = 0
    admin = False
    
def validation():
    global user, password, count,admin
    while (count < 3):
        user_vd = input("\nIngrese su usuario: ")
        password_vd = int(getpass.getpass("Ingrese su contraseña: "))
        if (user != user_vd or password != password_vd) and (count < 2):
            print("\nEl usuario o contraseña son incorrectos vuelva a intentarlo\n")
        if (user == user_vd and password == password_vd):
            count = count + 3
            admin = True
        if (count == 2):
         print("\nUsted ya alcanzo el limete de intentos, lo sentimos el programa se ha cerrado")
        count = count + 1

def menu():
    print("\n 1. Gestión de locales\n 2. Crear cuentas de dueños de locales\n 3. Aprobar / Denegarsolicitud de descuento\n 4. Gestión de Novedades\n 5. Reporte de utilización de descuentos\n 0. Salir\n")
    

inicialization()
while(type_user == 0):
    print("1 si es administrador  \n2 cliente \n3 salir")
    type_user = int(input("Ingrese el tipo de usuario: "))
    if (type_user== 2):
        type_user = int(input("Esta seccion se encuentra en contruccion, presione 0 para volver: "))
    if (type_user == 1):
        validation()
    if(type_user == 3):
        print("se cerro")

if (admin == True):
    menu()
    
