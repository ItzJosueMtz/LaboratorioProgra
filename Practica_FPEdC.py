#Josue Mtz
#Primero importo las librerias que voy a ocupar y que ya se encuentran instaladas
import time, os
from bs4 import BeautifulSoup as bs

#Tambien importamos y en su defecto instalamos las librerias que usaremos: WikipediaApi y Requests
try:
    import wikipediaapi
except ImportError:
    os.system('pip3 install wikipedia-api')
    print("Se instalo la libreria de wikipedia, por favor ejecute de nuevo")
    exit()

try:
    import requests
except ImportError:
    os.system('pip install requests')
    print("Se instalo la libreria de requests, por favor ejecute de nuevo")
    exit()

#Aqui inicia nuestro programa
# Primero generamos la funcion de busqueda e imprimir el primer parrafo
def respuesta(link):
    page = requests.get(link)               #Hacemos una solicitud para obtener el codigo de la pagina
    soup = bs(page.content,"html.parser")
    po = soup.find_all("p")                 #Lo trabajamos con BeautifulSoup y optenemos el primer parrafo
    sopa = po[0].getText()                  #Que normalmente es la definicion, y la imprimimos
    print(sopa)

#Aqui generamos la funcion para guardar el sitio en un archivo html
def archivo(link):
    page = requests.get(link)               #Hacemos una solicitud para obtener el codigo de la pagina
    soup = bs(page.content,"html.parser")
    fo = open("busqueda.html", "w")         #Lo trabajamos con BeautifulSoup y lo guardamos en un archivo html
    fo.close
    fo = open("busqueda.html", "w")         #Creamos el archivo, lo cerramos, y lo volvemos a abrir para escribir en el
    soup = str(soup)
    fo.write(soup)                          #Escribimos el codigo en el y lo cerramos
    fo.close

#Aqui inicia el Programa
wiki_wiki = wikipediaapi.Wikipedia('es')    #Seteamos el lenguaje con el que trabajaremos
while True:
    print ("Hola, Bienvenido a nuestro diccionario!\nOperamos con ayuda de Wikipedia: La Enciclopedia Libre en Español")
    busqueda = str(input("Por favor ingresa tu busqueda:\n"))
    page_py = wiki_wiki.page(busqueda)      #Pedimos a wikipedia que verifique si existe una pagina con ese nombre
    if (page_py.exists()==True):
        link = str(page_py.fullurl)         #Si existe, pedidmos su link y lo mandamos a la funcion
        respuesta(link)
        resp = str(input("Deseas guardar la pagina en tu computadora?\ns/n\n"))
        resp.lower()
        if (resp=="s"):
            archivo(link)                   #Preguntamos si quiere el archivo, si si, llamamos a la funcion
            time.sleep(2)
            print('Se ha guardado el archivo como "busqueda.html"!')
        else:
                continue
    else:
        continue
# :D
