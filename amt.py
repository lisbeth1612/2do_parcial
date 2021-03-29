Seguimiento = 0
while Seguimiento < 3:
    print('*************************')
    print('******* BIENVENIDO ******')
    print('*************************')

    Seguimiento = int(input('Que desea realizar \n 1. Crear una cuenta nueva \n 2. Ingresar al Cajeto Automatico \n 3. Deseo salir \n por favor digite 1 , 2 o 3 para seguir con la Transaccion\n'))    

    cuenta = []
    nombre = []
    balances =[]
    pinc =[]
    intentos = 3
    usuario = 0
    verificador = False 
    import csv        

    with open('cuentas.txt') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cuenta.append(row['cuenta'])
            nombre.append(row['nombre'])
            balances.append(row['balance'])
            pinc.append(row['pin'])  

    if Seguimiento == 1: 

        print('************************')
        print('* CREACCION DE CUENTAS *')
        print('************************')

        Archivo = open("cuentas.txt","a")
        Cuenta_new = int(input("digite su numero de cuenta \n"))
        nombre_new = input("Indique el nombre y apellido del cliente \n")
        balance_new = int(input("digite el balance (sin signos de moneda) \n"))
        pin_new = int(input("introduzca un pin de 4 digitos \n"))
        print('\n la cuenta a cargar es la siguiente: \n')
        cliente_new = Cuenta_new, nombre_new, balance_new, pin_new
        print (cliente_new)
        Archivo.write('\n')  
        Archivo.write(str(Cuenta_new))
        Archivo.write(',')
        Archivo.write(str(nombre_new))
        Archivo.write(',')
        Archivo.write(str(balance_new))
        Archivo.write(',') 
        Archivo.write(str(pin_new))
        Archivo.write('\n')      
        Archivo.close()  

        print('***************************************')
        print('* GRACIAS POR SU VISITA VUELVA PRONTO *')
        print('***************************************')

    if Seguimiento == 2:    

        print('*************************')
        print('*** CAJERO AUTOMATICO ***')
        print('*************************')        

        cliente = input("digite su numero de cuenta? ")        

        while (cliente not in cuenta):
            usuario = 0
            cliente = input(" ha surgido un error por favor digite su numero de cuenta sin espacios en blanco? ")
            
        if cliente == cuenta[usuario]:
            verificador=True
        else:
            while (cliente != cuenta[usuario]):
                usuario +=1
                if (cliente == cuenta[usuario]):
                    verificador=True
            
        while ((intentos > 0) and (verificador==True)):
            pin = int(input('inserte su codigo secreto: '))
            if pin == int(pinc[usuario]):
                print('ha ingresado su pin correctamente\n')
                print('presione 1 para balance\n')
                print('presione 2 para retiros \n')
                print('presione 3 para deposito\n')
                opcion = int(input('que operacion desea realizar?: '))
                if opcion == 1:
                    print('su balance es: ',balances[usuario], 'RD', '\n')
                    print('operacion efectuada correctamente')
                    print('***************************************')
                    print('* GRACIAS POR SU VISITA VUELVA PRONTO *')
                    print('***************************************')
                    break
                elif opcion == 2:
                    retiros = int(input('escriba el monto a retirar: '))
                    if retiros <= int(balances[usuario]):
                        balance = int(balances[usuario]) - retiros
                        print ('\n El Balance actual es: ',balance, 'RD')
                        '''Archivo = open("cuentas.txt","a")
                        Archivo.write(str(balance))      
                        Archivo.close()''' 
                        
                        print('operacion efectuada correctamente')
                        print('***************************************')
                        print('* GRACIAS POR SU VISITA VUELVA PRONTO *')
                        print('***************************************')
                        break
                    else:
                        print('su balance no cuenta con el monto suficiente para retirar esa cantidad \n')
                        break
                                 

                elif opcion == 3:
                    deposito = int(input('escriba el monto  para depositar: '))
                    balance = int(balances[usuario]) + int(deposito)
                    print ('\n El balance actual es: ',balance, 'RD')
                    print('operacion efectuada correctamente')
                    print('***************************************')
                    print('* GRACIAS POR SU VISITA VUELVA PRONTO *')
                    print('***************************************')
                    break
                    
                        
            if pin != pinc[usuario]:
                print('pin incorrecto')
                intentos = intentos - 1
            if intentos == 0:
                print('\n Ha excedido el limite de intentos, el usuario ha sido bloqueado')
                break    

    else:
        print('***************************************')
        print('* GRACIAS POR SU VISITA VUELVA PRONTO *')
        print('***************************************')
        break