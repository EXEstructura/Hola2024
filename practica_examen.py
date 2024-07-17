# 1. Crea un archivo llamado "archivo.txt" y escribe en él "Hola, mundo!".
def crear_archivo():
    with open("archivo.txt","w") as archivo:
        archivo.write("hola, mundo"+"\n")
crear_archivo()
# 2. Lee el contenido del archivo "archivo.txt" y muéstralo por pantalla.
def leer_archivo():
    with open("archivo.txt","r") as archivo_lectura:
        contenido=archivo_lectura.read()
        print(contenido,end="")
# 3. Añade "¡Python es increíble!" al final del archivo "archivo.txt".
def añadir_linea(archivo):
    with open(archivo,"a") as archivo:
        archivo.write("Python es increible"+"\n")
añadir_linea("archivo.txt")
leer_archivo()
# 4. Cuenta cuántas líneas tiene el archivo "archivo.txt".
def contador_lineas(archivo):
    with open(archivo,"r") as archivo:
        contenido=archivo.readlines()
        print(len(contenido))
contador_lineas("archivo.txt")
# 5. Lee la segunda línea del archivo "archivo.txt".
def leer_segunda_linea(archivo):
    with open(archivo,"r") as archivo:
        contenido=archivo.readlines()
        if len(contenido)>=2:
            print(contenido[1].strip())
leer_segunda_linea("archivo.txt")
# 6. Crea una copia del archivo "archivo.txt" llamada "copia_archivo.txt".
def copiar_archivo(archivo_entrada,archivo_salida):
    with open(archivo_entrada,"r") as archivo_lectura:
        contenido=archivo_lectura.read()
    with open(archivo_salida,"w") as archivo_salida:
        archivo_salida.write(contenido)
archivo_entr="archivo.txt"
archivo_sal="copia_archivo.txt"
copiar_archivo(archivo_entr,archivo_sal)
# 7. Crea una función que reciba un nombre de archivo como parámetro y muestre su
# contenido por pantalla.
def presentar(archivo):
    with open(archivo,"r") as archivo_lectura:
        contenido=archivo_lectura.read()
        print(contenido)
presentar("archivo.txt")
# 8. Crea una función que reciba un nombre de archivo como parámetro y devuelva la
# cantidad de caracteres que contiene.
def cantidad_de_caracteres(archivo):
    with open(archivo,"r") as archivo_lectura:
        contenido=archivo_lectura.read()
        contenido_sin_eespacios="".join(contenido.split())
        contador=len(contenido_sin_eespacios)
    return contador
print(cantidad_de_caracteres("archivo.txt"))
# 9. Escribe una lista de números en un archivo llamado "numeros.txt", uno por línea.
def lista_numeros():
    with open("numeros.txt","w") as archivo:
        contenido=[i for i in range(1,11)]
        for numero in contenido:
            archivo.write(str(numero)+"\n")
    with open("numeros.txt","r") as archivo_lectura:
        pantalla=archivo_lectura.read()
        print(pantalla)
lista_numeros()
# 10. Lee el archivo "numeros.txt" y suma todos los números presentes en él.
def suma_numeros(archivo):
    acu=0
    with open(archivo,"r") as archivo:
        contenido=archivo.read()
        lista=contenido.split()
        for numero in lista:
            acu+=int(numero)
    return acu
print(suma_numeros("numeros.txt"))
# 11. Escribe un programa que pida al usuario ingresar una línea de texto y la guarde en un
# archivo llamado "entrada_usuario.txt".
def ingresar_linea(linea_nueva):
    with open("entrada_usuario.txt","w") as archivo:
        archivo.write(linea_nueva+"\n")
ingresar_linea("hola como estas")
# 12. Crea una función que tome un archivo HTML como entrada y cuente cuántas
# etiquetas <p> contiene.
def html(archivo_html):
    with open(archivo_html,"r",encoding="utf-8") as archivo:
        contador=0
        contenido=archivo.read()
        indice=contenido.find("<p>")
        while indice!=-1:
            contador+=1
            indice=contenido.find("<p>", indice + 1)
    return contador
archivohtml="archivo.html"
print(f"el archivo {archivohtml} contiene {html(archivohtml)} etiquetas <p>")
# 13. Escribe un programa que reemplace todas las ocurrencias de una palabra específica
# en un archivo de texto.
with open("ocurrencias.txt","w") as archivo_nuevo:
    archivo_nuevo.write("hola"+"\n")
    archivo_nuevo.write("hola"+"\n")
def eliminar_palabra_en_archivo(archivo, palabra):
    with open(archivo, 'r') as file:
        contenido = file.read()

    # Reemplazar todas las ocurrencias de la palabra con una cadena vacía
    contenido_modificado = contenido.replace(palabra, '')

    # Escribir el contenido modificado de vuelta al archivo
    with open(archivo, 'w') as file:
        file.write(contenido_modificado)

# Ejemplo de uso
archivo = 'ocurrencias.txt'
palabra_a_eliminar = 'hola'
eliminar_palabra_en_archivo(archivo, palabra_a_eliminar)
# 14. Crea un programa que lea un archivo JSON y muestre solo los elementos que
# cumplen cierta condición.
import json

def mostrar_elemento(archivo_json,condicion):
    with open(archivo_json,"r") as archivo:
        contenido= json.load(archivo)
    
    for elemento in contenido:
        if condicion(elemento):
            print(elemento)
def condicion_mayor(elemento):
   return elemento["edad"]>25
archivo_json = 'datos.json'
mostrar_elemento(archivo_json,condicion_mayor)
# 15. Crea un programa que concatene dos archivos de texto en uno nuevo.
def concatenar(archivo1,archivo2,salida):
    with open(archivo1,"r") as archivo:
        contenido1=archivo.read()
    with open(archivo2,"r") as archivop:
        contenido2= archivop.read()
    with open(salida,"w") as archivo_salida:
        archivo_salida.write(contenido1+contenido2)
arch="archivo.txt"
arch2="entrada_usuario.txt"
salidaa="archivo_concatenado.txt"
concatenar(arch,arch2,salidaa)
# 16. Escribe una función que tome una lista de nombres y los escriba en un archivo de
# texto, uno por línea.
lista_nombres=["jose","miguel","andres"]
def lista_nom(lista):
    with open("archivo_lista.txt","w") as archivo:
        for nombre in lista:
            archivo.write(nombre+"\n")
lista_nom(lista_nombres)
# 17. Crea un programa que ordene alfabéticamente las líneas de un archivo de texto.
def ordenar(archivo,archivo_ordenado):
    with open(archivo,"r") as archivo:
        contenido=archivo.readlines()
        contenido.sort()
    with open(archivo_ordenado,"w") as archivops:
        for linea in contenido:
         archivops.write(linea)
a1="archivo_concatenado.txt"
a2="archivo_ordenado"
ordenar(a1,a2)
# 18. Escribe una función que lea un archivo de texto y elimine las líneas duplicadas.
with open("duplicado.txt","w") as ar:
    ar.write("hola"+"\n")
    ar.write("hola"+"\n")
def lineas_duplicadas(archivo,salida):
    lineas_unicas=set()
    with open(archivo,"r") as archivos:
        for i in archivos:
            lineas_unicas.add(i)
    with open(salida,"w") as arch:
        for i in lineas_unicas:
            arch.write(i)
arc="duplicado.txt"
arc2="sin_duplicar.txt"
lineas_duplicadas(arc,arc2)
# 19. Crea un programa que recorra todos los archivos de un directorio y muestre sus
# nombres.
import os
def directorio_(directorio):
    if not os.path.exists(directorio):
        print(f"el {directorio} no existe")
    archivoss=os.listdir(directorio)
    for i in archivoss:
        print(i)
directorio="./"
directorio_(directorio)
# 20. Crea un programa que lea un archivo de texto y reemplace las vocales con acento por
# vocales sin acento.
# Diccionario de vocales con acento
vocales_con_acento = {
    'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
    'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
    'ü': 'u', 'Ü': 'U'
}
with open("con_acento.txt","w") as arrchiv:
    arrchiv.write("josué"+"\n")
def reemplazar(archivo):
    with open(archivo,"r") as ar:
        contenido=ar.read()
    for vocales, sin_acento in vocales_con_acento.items():
        contenido=contenido.replace(vocales,sin_acento)
    with open(archivo,"w") as ar1:
        ar1.write(contenido)
filee="con_acento.txt"
reemplazar(filee)

# 21. Escribe una función que lea un archivo de texto y cuente la cantidad de veces que
# aparece una palabra específica.
with open("repetido.txt","w") as archivito:
    archivito.write("josue"+"\n")
    archivito.write("josue"+"\n")
    archivito.write("fernando"+"\n")

def contar_repetido(archivo,palabra):
    contador=0
    with open(archivo,"r") as archivoo:
        contenido=archivoo.read()
        palabras=contenido.split()
    for i in palabras:
        if i==palabra:
            contador+=1
    return contador
file="repetido.txt"
palabras="fernando"
print(contar_repetido(file,palabras))
# 22. Escribe una función que reciba el nombre de un archivo y devuelva la longitud del
# contenido más largo de una línea.
def mas_larga(archivo):
    max_longitud=0
    with open(archivo,"r") as archivo:
        contenido=archivo.readlines()
        for i in contenido:
            i=i.strip()
            longitud_actual=len(i)
        if longitud_actual>max_longitud:
            max_longitud=longitud_actual
    return max_longitud           
fil="repetido.txt"
print(mas_larga(fil))
# 23. Implementa un programa que encuentre la palabra más larga en un archivo de texto.
def palabra_mas_larga(archivo):
    palabra_max=0
    with open(archivo,"r") as archiv:
        contenido=archiv.read()
        contenido=contenido.split()
        for i in contenido:
            longitud_actual=len(i)
        if longitud_actual>palabra_max:
         palabra_max=longitud_actual
    return palabra_max
archivo_="archivo.txt"
print(palabra_mas_larga(archivo_))

# 24. Crea un programa que lea un archivo de texto y elimine todas las líneas en blanco.
with open("archivo_blanco.txt","w") as archp:
    archp.write(" "+"\n")
    archp.write(" "+"\n")
    archp.write("josue"+"\n")
def eliminar_lineas_en_blanco(archivo):
    with open(archivo) as archivs:
        contenido=archivs.readlines()
    
    lineas_filtradas=[i for i in contenido if i.strip() !=""]
    with open(archivo,"w") as archivo_sal:
        archivo_sal.writelines(lineas_filtradas)
a="archivo_blanco.txt"
eliminar_lineas_en_blanco(a)
# 25. Escribe una función que lea un archivo de texto y cuente cuántas vocales hay en él.
def contar_vocales(archivo):
    vocales="aeiouAEIOU"
    contador=0
    with open(archivo,"r") as archivo:
        contenido=archivo.read()
    for i in contenido:
        if i in vocales:
            contador+=1
    return contador
archv="archivo.txt"
print(contar_vocales(archv))
# 26. Crea una función que lea dos archivos de texto, los compare y muestre las líneas que
# son iguales en ambos.
def lineas_iguales(archivo,archivo2):
    with open(archivo,"r") as archivo:
        contenido1=archivo.readlines()
    with open(archivo2) as archivo2:
        contenido2=archivo2.readlines()
    lineas_unicas=set(contenido1).intersection(set(contenido2))
    for i in lineas_unicas:
        print(i.strip())
archivo1 = "duplicado.txt"
archivo2 = "sin_duplicado.txt"
lineas_iguales(archivo1, archivo2)      
# 27. Escribe un programa que recorra todos los archivos de un directorio y muestre sus
# nombres junto con la cantidad de líneas que contienen.
import os

def mostrar_lineas_directorio(directorio):
    if not os.path.exists(directorio):
        print(f"El directorio {directorio} no existe")
        return  # Salir de la función si el directorio no existe
    
    archivos_directorio = os.listdir(directorio)
    for nombre_archivo in archivos_directorio:
        ruta_archivo = os.path.join(directorio, nombre_archivo)
        if os.path.isfile(ruta_archivo):
            try:
                with open(ruta_archivo, "r", encoding='utf-8') as archivo:
                    lineas = archivo.readlines()
                    print(f"{nombre_archivo}: {len(lineas)} líneas")
            except Exception as e:
                print(f"No se pudo leer el archivo {nombre_archivo}: {e}")

# Ejemplo de uso
directorio = "./"
mostrar_lineas_directorio(directorio)
# 28. Intenta dividir dos números, captura la excepción si se intenta dividir por cero.
def numeros(n1,n2):
    try:
        resultado=n1/n2
        print(resultado)
    except ZeroDivisionError:
        print(f"no se puede divir por cero")
n1=7
n2=0
numeros(n1,n2)
# 29. Accede a una propiedad que no existe en un objeto, captura la excepción.
class persona:
    def __init__(self,nombre):
        self.nombre=nombre
objeto=persona("josue")

try:
    print(objeto.edad)
except AttributeError:
    print("Error: la propiedad que intentas acceder no existe en el objeto")
# 30. Crea una función que espera dos argumentos y llámala con solo uno. Captura la
# excepción.
def sumas(n1,n2):
    suma=n1+n2
    print(suma)
try:
    sumas(1)
except TypeError:
    print("la funcion necesita de dos argumentos para poder funcionar")
# 31. Intenta crear un objeto con una propiedad llamada class, captura la excepción.
class MiClase:
    def __init__(self):
        # Usamos setattr() para establecer el atributo dinámicamente
        setattr(self, 'class', 'Ejemplo')

# Intentamos crear un objeto de la clase
try:
    objeto = MiClase()
    # Accedemos al atributo 'class' utilizando getattr()
    print(getattr(objeto, 'class'))
except Exception as e:
    print(f"Error al intentar crear el objeto: {e}")


# 32. Intenta acceder a un índice que está fuera del rango de un arreglo.
def indice():
    try:
        lista=[i for i in range(1,11)]
        print(lista[20])
    except IndexError:
        print("el indice al cual intentas acceder no existe")
indice()
# 33. Intenta abrir un archivo que no existe y captura la excepción.
try:
    with open("archivoxd.txt","r") as arrr:
        contenido=arrr.read()
        print(contenido)
except FileNotFoundError:
    print("Error: el archivo que intentas leer no existe")
# 34. Utiliza una URL inválida y maneja la excepción.
import urllib.request
def url(URL):
    try:
       response=urllib.request.urlopen(URL)
       print(response)
    except Exception as e:
        print(f"error al abrir la url:{e}")

URL="http://ejemplo_url_invalida"
url(URL)