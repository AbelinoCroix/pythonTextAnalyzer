#El dia estuvo muy bien, porque aprendí a programar un analizador de texto en Python.
text=input("Ingrese cualquier texto que desee: ")
textMinuscula=text.lower()

#Contador de letras
letras=['','','']
letras[0]=input("Ingresa la primer letra a buscar: ")
letras[1]=input("Ingresa la segunda letra a buscar: ")
letras[2]=input("Ingresa la tercer letra a buscar: ")
letras[0]=letras[0].lower()
letras[1]=letras[1].lower()
letras[2]=letras[2].lower()

l1Count=textMinuscula.count(letras[0])
l2Count=textMinuscula.count(letras[1])
l3Count=textMinuscula.count(letras[2])
print(f"Las letras {letras} aparecen {l1Count}, {l2Count} y {l3Count} veces, respectivamente")

#Contador de palabras
textSeparado= text.split(" ")
palabras=len(textSeparado)
print(f"El texto contiene {palabras} palabras")

#Primer y ultima letra
textLetras=list(text)
primerLetra=textLetras[0]
ultimaLetra=textLetras[-1]
print(f"La primer letra del texto es {primerLetra} y la última letra es {ultimaLetra}")

#Orden inverso
textReversa=textSeparado
textReversa.reverse()
print(f"El texto escrito de forma inversa se ve de la siguiente manera: {textReversa}")

#Buscador de Python
encuentraPy= "Python" in textSeparado
if encuentraPy == True:
    print("La palabra 'Python' sí se encuentra en el texto")
else:
    print("La palabra 'Python' no se encuentra en el texto")