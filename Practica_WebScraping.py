#Josue Mtz
#Practica de Web Scraping con la cual obtendremos la tabla de posiciones de la Liga MX
#Primero se importan las liberias con las que trabajaremos, ahora no haremos un Try, por lo que se recomeinda
#Instalarlas desde la terminal/consola con pip install
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

#Yo guarde externamente el url de la pagina a la que le haremos WebScraping
url = "https://mexico.as.com/resultados/futbol/mexico_apertura/clasificacion/"

#Ahora toca trabajar con la pagina, primero descargamos el codigo HTML de la misma
page = requests.get(url)
#Y ahora le damos forma para trabajar con el mas facil
soup = bs(page.content, 'html.parser')

#En lo que el script trabaja damos un saludito
print("Hola, espera un momento que ya tendre para ti la tabla general de la Liga MX :D\n")

#Parte de los equipos
#Primero encontraremos los nombres de los equipos de la tabla general
eq = soup.find_all('span', class_='nombre-equipo')
#Con un ciclo los guardamos en una lista
equipos = []
temp = 0                                #Usamos una variable temporal de ayuda
for i in eq:                            #Ya que puede haber mas nombres de los que queremos
    if (temp < 18):                     #Como son 18 equipos solo lo hacemos con los primero 18 resultados
        equipos.append(i.text)
    else:
        break
    temp += 1

#Repetimos el mismo proceso para encontrar los puntos que tiene cada equipo
pts = soup.find_all('td', class_='destacado')
puntos = []
temp = 0
for i in pts:
    if (temp < 18):
        puntos.append(i.text)
    else:
        break
    temp += 1

#Con ayuda de la libreria Pandas, creamos un diccionario chido que tendra los datos dentro de el de forma ordenada
dic = pd.DataFrame({'Nombre':equipos,'Puntos':puntos}, index=list(range(1,19)))
#Imprimimos nuestro diccionario
print(dic)
#Josue Mtz
#:D