#Josue Martinez
#Laboratorio de Programacion Para Ciberseguridad
#Si bien  l apractica decia que se tenia que hacer un ejecutable .sh el cual hiciera funcionar este script
#Como se me dificulto, opte por hacer un scritp mas interactivo, el cual te pida uno por uno lo que vas a hacer

#Bien, comenzamos importando las librerias
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage      #Aqui importe imagen, aunque no la pude usar porque me marcaba un error
import smtplib

#Vamos a pedirle al usuario mediante inputs que ingrese todos los datos
print("Bienvenido, por favor indica los datos que usaremos")
serve = str(input("Ingresa el servidor con el que enviaremos el correo: (ej: office365.com)\n"))
sender = str(input("Ingresa el correo electronico que lo enviara:\n"))
passusr = str(input("Ingresa tu contrasena:\n"))
reminder = str(input("Ingresa el correo al que se enviara\n"))
subject = str(input("Ingrese el asunto del correo:\n"))
body = str(input("Ingresa el mensaje del correo:\n"))
print("Espere un momento por favor")

#Creamos el objeto msg el cual sera nuestro correo electronico
msg = MIMEMultipart()

#Asignamos los diferentes datos
message = body
password = passusr
msg['From'] = sender
msg['To'] = reminder
msg['Subject'] = subject

#DE aqui en adelante solo trabajamos para mandar el mensaje
msg.attach(MIMEText(message, 'plain'))

temp = str('smtp.'+serve+':587')    #Aqui se usa una variable temporal para conectarnos al servidor
server = smtplib.SMTP(temp)
server.starttls()

#Iniciamos sesion en el servidor
server.login(msg['From'], password)

#Mandamos el mensaje y cerramos el servidor
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
#Imprimimos un mensaje de que todo salio bien
print("Correo enviado de forma exitosa a:",(msg['To']))
#Estuve haciendo pruebas para ver si se podria agregar la opcion de adjuntar archivos o imagenes
#Pero se quedaba congelado el script cuando lo intentaba
#Y me sacaba diciendo error timeout, asi que decidi no ponerlo en este script
#Lo hubiera puesto como una condicional o una funcion
#Josue Mtz
#:D