def suma():
    sum= fnum + fnum2
    print(sum)

def resta():
    rest= fnum - fnum2
    print (rest)

def multiplicacion():
    mult= fnum * fnum2
    print (mult)

def division():
    divi= fnum / fnum2
    print (divi)

nombre = input ("Cómo te llamas?: ")
print ("Hola", nombre, ", empecemos a operar!")
while True:
    num= input('Introduce un número: ')
    try:
        fnum=float(num)
        break
    except:
        print ('Asegúrate que sea un valor numérico')
        continue
while True:
    num2= input('Ahora introduce otro número: ')
    try:
        fnum2= float(num2)
        break
    except:
        print ('Asegúrate que sea un valor numérico')
        continue
while True:
    signo= input ('Introduce un símbolo matemático ( + - / *): ')
    if signo is '+':
        suma()
        break
    elif signo is "-":
        resta()
        break
    elif signo is "*":
        multiplicacion()
        break
    elif signo is "/":
        division()
        break
    else:
        print ('Vuelve a escribir el símbolo bien')
        continue
