def ejercicio_1 ():
    nombre = input("ingrese nombre : ")
    print(f"Hola coder , bienvenido a riwi {nombre}")


def ejercicio_2 ():
    num1 = int(input("ingrese numero 1 :"))
    num2 = int(input("ingrese numero 2 :"))
    suma = num1+num2
    print(f"La suma es : {suma}")

def ejercicio_3 ():
    numero =  int(input("Ingrese un número: "))
    if numero  % 2 == 0:
       print(numero, "es par.")
    else:
      print(numero, "es impar.")


def ejercicio_4 ():
  edad = int(input("Por Favor Dame Tu edad: "))
  if edad >= 18 : 
    print("Eres mayor de edad")
  else:
   print("Eres menor de edad")

def ejercicio_5 ():
  grados_celsius = int(input("Por Favor, Ingrese Grados celsius: "))
  fahrenheit = (grados_celsius * 9/5) + 32.
  print(f"{grados_celsius} grados Celsius son {fahrenheit} grados Fahrenheit")

def ejercicio_6 ():
  base = int(input("Ingrese base del triagulo : "))
  altura = int(input("Ingrese altura del triagulo : "))
  area = (base * altura) / 2
  print(f"El area es : {area}")

def ejercicio_7 ():
   lista_numeros = []
   i = 0
   for i in range(4) :
    numeros = int(input("Ingrese Numero : "))
    lista_numeros.append(numeros)
    i = i+1
   
   if lista_numeros :
    print(f"Numero mayor es : {max(lista_numeros)}")

def ejercicio_8():
  palabra = input("Ingrese una palabra: ")
  letra_a_contar = input("Ingrese la letra a contar: ")
  contador = 0

  for letra in palabra:
    if letra == letra_a_contar:
        contador += 1

  print("La letra '" + letra_a_contar + "' aparece " + str(contador) + " veces en la palabra.")

def ejercicio_9():
 numeros = input("Ingrese una lista de números separados por espacios: ").split()
 pares = []

 for numero in numeros:
    if int(numero) % 2 == 0:
        pares.append(int(numero))

 print("Números pares:", pares)


def ejercicio_10():
    palabra = input("Ingrese una palabra: ")
    palabra_limpia = "".join(palabra.lower().split())  # Eliminar espacios y convertir a minusculas
    palindromo = palabra_limpia == palabra_limpia[::-1]

    if palindromo:
        print("La palabra ingresada es un palindromo")
    else:
        print("La palabra ingresada no es un palindromo")

def ejercicio_11(): 
    numero = int(input("Introduce un numero: "))
    factorial = 1
    if numero < 0:
        print("El factorial no esta definido para numeros negativos")
    elif numero == 0:
        print("El factorial de 0 es 1")
    else:
        for i in range(1, numero + 1):
            factorial *= i
        print("El factorial de", numero, "es", factorial)

def ejercicio_12():
    lista = input("Ingrese los numeros separados por espacios: ").split()

    try:
        lista = [int(num) for num in lista]
    except ValueError:
        print("Error: Ingresa solo numeros.")
        exit()

    unicos = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                if lista[i] not in unicos:
                    unicos.append(lista[i])

    if unicos:
        print("Los numeros unicos son:", unicos)
    else:
        print("No hay numeros unicos en la lista.")
  
def ejercicio_13():
    print("""Juego de "Fizz"(pares), "Buzz"(impares) o "FizzBuzz(negativos)""")
    numero = int(input("Ingrese un numero : "))
    if numero % 2 == 0:
       print("Fizz")
    else:
       print("Buzz")
    if numero == 0:
       print("Numero no entra en juego !")
    if numero < 0 :
       print("FizzBuzz")

def ejercicio_14():
    cadena = input("Por favor, ingresar una cadena de texto: ")
    contador_vocales = 0
    vocales = "aeiouAEIOU"

    for caracter in cadena:
      es_vocal = False
      for vocal in vocales:
        if caracter == vocal:
          es_vocal = True
          break
      if es_vocal:
        contador_vocales += 1

    print(f"La cadena '{cadena}' tiene {contador_vocales} vocales.")

def ejercicio_15():
    palabra = input("Ingrese una palabra: ")
    inversion = palabra[::-1]  
    print(inversion)      

def ejercicio_16(): 
  contrasena = input("Por favor, ingresa tu contraseña: ")
  tiene_mayuscula = False
  tiene_minuscula = False
  tiene_numero = False
  tiene_simbolo = False
  simbolos = """!@#$%^&*()_+=-`~[]\{}|;':\",./<>?"""  # Lista de símbolos comunes

  for caracter in contrasena:
    if 'A' <= caracter <= 'Z':
      tiene_mayuscula = True
    elif 'a' <= caracter <= 'z':
      tiene_minuscula = True
    elif '0' <= caracter <= '9':
      tiene_numero = True
    elif caracter in simbolos:
      tiene_simbolo = True

  if tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_simbolo:
    print("La contraseña cumple con los requisitos de seguridad.")
  else:
    print("La contraseña NO cumple con los siguientes requisitos:")
    if not tiene_mayuscula:
      print("Debe contener al menos una letra mayuscula.")
    if not tiene_minuscula:
      print("Debe contener al menos una letra minuscula.")
    if not tiene_numero:
      print("Debe contener al menos un numero.")
    if not tiene_simbolo:
      print("Debe contener al menos un simbolo .")

def ejercicio_17():
    import random
    print("Simulando el lanzamiento de un dado")
    resultado = int(random.random() * 6) + 1
    print(f"El resultado del lanzamiento es: {resultado}")

def ejercicio_18():
     entrada = input("Por favor, ingresa los numeros separados por espacios: ")
     numeros_str = entrada.split()
     lista_numeros = []

     for num_str in numeros_str:
      numero = int(num_str)
      lista_numeros.append(numero)
 
      no_repetidos = []
      for numero in lista_numeros:
          contador = 0
          for otro_numero in lista_numeros:
            if numero == otro_numero:
              contador += 1
          if contador == 1:
            no_repetidos.append(numero)

          suma_no_repetidos = 0
          for numero_unico in no_repetidos:
            suma_no_repetidos += numero_unico

      print(f"La lista de numeros ingresada es: {lista_numeros}")
      print(f"Los numeros que no se repiten son: {no_repetidos}")
      print(f"La suma de los números que no se repiten es: {suma_no_repetidos}")

def ejercicio_19():
  import random
  import string

  longitud_str = input("Por favor, ingresa la longitud deseada para la contraseña: ")
  longitud = int(longitud_str)

  caracteres = string.ascii_letters + string.digits + string.punctuation
  contrasena = ""

  for _ in range(longitud):
    indice_aleatorio = int(random.random() * len(caracteres))
    caracter_aleatorio = caracteres[indice_aleatorio]
    contrasena += caracter_aleatorio

  print(f"La contraseña aleatoria generada es: {contrasena}")



