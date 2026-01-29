saludo='Hola Mundo'

print("LONGITUD DE CADENAS")
print("-"*30)
longitud=len(saludo)
print(saludo)
print("La longitud de la cadena es:",longitud)

print("-"*30)
print("CADENAS Y CADENAS")
print("-"*30)
cad="Esta es una 'cadena con comillas simples' dentro de comillas dobles"
print(cad)
cad=cad+" Algo"
print(cad)
print(cad[0])
# cad[0]='e'  #Error, las cadenas son inmutables
lenguaje="Python"
descripcion="Este es un buen curso"
frase=descripcion+" de "+lenguaje
print(frase)

print("-"*30)
print("CADENAS Y NUMEROS")
print("-"*30)
total=5500
#mensaje="El total de la compra es: "+total+" pesos"
mensaje="El total de la compra es: "+str(total)+" pesos"
print(mensaje)
mensaje=f"El total de la compra es: {total} pesos"
print(mensaje)

print("-"*30)
print("AGREGAR SALTOS DE LINEAS A CADENAS")
print("-"*30)
mensaje="Orden con 10 elementos\nCargo $5500.99\n¡Gracias por su preferencia!"
print(mensaje)

print("-"*30)
print("FUNCIONES CON CADENAS")
print("-"*30)
nombres="Ana,Maria,Juan,Carlos,Luis"
elementos="a a a b b B c c c c c aa"
print(nombres.upper()) #convierte una cadena a mayúscula
print(nombres.lower()) #Convierte una cadena a minúscula
print(nombres.capitalize()) #Convierte la primera letra en mayúscula
print(nombres.title()) #Convierte en mayúscula cada letra de la cadena
print(nombres.replace("a","x")) #Remplaza una letra a por la letra x
print(nombres.split(",")) #Divide la cadena hasta que encuentre la , o el caracter especificado
print(nombres.count("a")) #Cuenta el número de a que existe en la cadena nombres
print(elementos.count("a")) #Cuenta cuantas "a" hay en una cadena
print(nombres.split(",")[0]) #Divide la cadena y extrae el elmento 0 de izq. a der.
print(nombres.split(",")[-1]) #Divide la cadena y extrae el elemento -1 de derecha a izquierda
print(nombres.split(",")[-2]) #DIvide la cadena y extrae el elemento '2
#print(nombres.split(",")[-6])
print(nombres.replace("Juan","Pedro")) #Reemplaza la cadena Juna por Pedro
print(nombres.replace(","," ")) #Reemplaza el caracter , por " "
print(nombres.endswith("Luis")) #Pregunta si la cadena finaliza con LUis
print(nombres.startswith("Ana")) #Pregunta si la cadena inicia con ANa
print(nombres.index("Carlos"))#Cuenta la posición en donde empieza la palabra Carlos
print(nombres.find("Juan")) #Busca y muestra en que posición empieza el nombre JUan

print("-"*30)
print("Cadenas multilínea")
print("-"*30)
texto_multilinea="""Este es un texto
[][]que abarca varias líneas.
**Podemos escribir lo que queramos aquí,
$$y se mantendrá el formato!!."""
print(texto_multilinea)
cadena_limpia=texto_multilinea.replace("[]","")\
    .replace("**","").replace("$$","") #Reemplaza un caracter por espacios en blanco
print(cadena_limpia)