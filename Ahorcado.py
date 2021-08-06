# Funcion que añade guiones a la palabra que ingresa el usuario
def palabraMayus (x):
    cap = x.capitalize()
    i = 0
    s = cap[0]
    while i<(len(cap)-1):
        s += " " + "_"
        i+= 1 
    return s
# Funcion que muestra la palabra con las las letras que ingresa el usuario
def mostrarLetra (a,y,z):
    i = 1
    while(i<=(len(y)-1)):
        if ( a == y[i]):
            z= z[:i*2] + a + z[i*2 + 1:]
        i=i+1
    return z
# Funcion que muestra un texto segun las respuestas contestadas correctamente
def calcularResultado (x,y):
    if x==y: 
        print("¡¡¡Ganaste pa'!!!")
        print("Respuestas correctas " + str(x) + "/" + str(y))
    elif x>y/2 and x!=y: 
        print("Not bad")
        print("Respuestas correctas " + str(x) + "/" + str(y))      
    else:
        print("uff como le pifiaste eh")
        print("Respuestas correctas " + str(x) + "/" + str(y))  
jugarDenuevo = "si"
while jugarDenuevo == "si":
    palabras = ["regalo","australia","masticas","domingo","baranda","tesoro","plegable","jugosa","palacio","calavera"]
    i = 0
    contadorErrores = 0
    cantAdivinadas = len(palabras)
    intRes = len(palabras[i])-2
    print("Adivina la palabra")
    palabMayus = palabraMayus(palabras[i])
    print(palabMayus)
    a = str(input("Ingresa una letra o palabra:  ").lower())
    while (len(palabras)-1)>=i:
        # Si la letra o palabra ingresada por el usuario es correcta
        if a in palabras [i] or a == palabras[i]:
            if a == palabras[i]:
                print("Correctooo")
                print ("Siguiente palabra: ")
                i = i+1
                intRes=len(palabras[i])-2
                palabMayus = palabraMayus(palabras[i])
                contadorErrores = 0
                print(palabMayus)     
            if  a in palabras [i]:
                palabMayus =  mostrarLetra (a,palabras[i],palabMayus)
                print (palabMayus)
            a = str(input("Ingresa una letra o palabra:  ").lower())     
            if palabras [i] == palabras[len(palabras)-1] and palabras [i] == a:
                calcularResultado(cantAdivinadas, len(palabras))
                break
      # Si la letra ingresada por el usuario no es correcta       
        elif len(a)==1:
            if contadorErrores == 0:
                s = ""
                s = s + a
                print("Letras incorrectas: " + s)
                intRes = intRes - 1
                contadorErrores = contadorErrores + 1  
                print("Intentos restantes: " + str(intRes))
            elif a in s:
                print("Letras incorrectas: " + s )
                intRes = intRes - 1
                contadorErrores = contadorErrores + 1  
                print("Intentos restantes: " + str(intRes))    
            else:
                if intRes==0 :
                    print("Intentos acabados")
                    contadorErrores = 0
                    i=i+1
                    intRes=len(palabras[i])-2
                    palabMayus = palabraMayus(palabras[i])              
                else:
                    s = s + " - " + a
                    print("Letras incorrectas: " + s )
                    intRes = intRes - 1
                    contadorErrores = contadorErrores + 1  
                    print("Intentos restantes: " + str(intRes))
            print(palabMayus)
            a = str(input("Ingresa una letra o palabra:  ").lower())       
        # Si la palabra ingresada por el usuario no es correcta   c  
        else:
            print("Respuesta incorrecta")
            cantAdivinadas = cantAdivinadas - 1 
            try: 
                i = i + 1
                intRes=len(palabras[i])-2
                palabMayus = palabraMayus(palabras[i])
                print(palabMayus)
                a = str(input("Ingresa una letra o palabra:  ").lower())  
            except IndexError:
                calcularResultado(cantAdivinadas, len(palabras))
                break
    print ("Jugar denuevo?   si / no" )
    jugarDenuevo = input().lower()