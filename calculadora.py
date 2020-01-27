def operaciones(oper):
    if oper == 'suma':
        sum= fnum + fnum2
        print(sum)
    elif oper == 'resta':
        rest= fnum - fnum2
        print(rest)
    elif oper == 'multiplicacion':
        mult= fnum * fnum2
        print(mult)
    elif oper == 'division':
        divi= fnum / fnum2
        print(divi)
        
#Introducción:
nombre = input ("Cómo te llamas?: ")
print ("Hola", nombre, ", empecemos a operar!")

#Pedir el primer número:
while True:
    num= input('Introduce un número: ')
    try:
        fnum=float(num)
        break
    except:
        print ('Asegúrate que sea un valor numérico')
        continue

#Pedir el segundo número:
while True:
    num2= input('Ahora introduce otro número: ')
    try:
        fnum2= float(num2)
        break
    except:
        print ('Asegúrate que sea un valor numérico')
        continue
        
#Pedir la operación (que tirará de la función de arriba):
while True:
    signo= input ('Introduce un símbolo matemático ( + - / *): ')
    if signo is '+':
        operaciones('suma')
        break
    elif signo is "-":
        operaciones('resta')
        break
    elif signo is "*":
        operaciones('multiplicacion')
        break
    elif signo is "/":
        operaciones('division')
        break
    else:
        print ('Vuelve a escribir el símbolo bien')
        continue
