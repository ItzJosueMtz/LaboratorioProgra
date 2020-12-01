from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

window = Tk()
window.title("Correo electronico con SMTP")
window.geometry('500x200')

lbl0 = Label(window, text="Servidor",font=("Arial Bold", 11))
lbl0.grid(column=0, row=0)
combo = Combobox(window)
combo['values']= ("office365.com")
combo.current(0)
combo.grid(column=1, row=0)

lbl1 = Label(window, text="Correo electronico",font=("Arial Bold", 11))
lbl1.grid(column=0, row=1)
sender = Entry(window,width=30)
sender.grid(column=1, row=1)

lbl2 = Label(window, text="Contraseña",font=("Arial Bold", 11))
lbl2.grid(column=0, row=2)
passusr = Entry(window,width=30)
passusr.grid(column=1, row=2)

lbl3 = Label(window, text="Destinatario",font=("Arial Bold", 11))
lbl3.grid(column=0, row=3)
reminder = Entry(window,width=30)
reminder.grid(column=1, row=3)

lbl4 = Label(window, text="Asunto",font=("Arial Bold", 11))
lbl4.grid(column=0, row=4)
subject = Entry(window,width=30)
subject.grid(column=1, row=4)

lbl5 = Label(window, text="Contenido",font=("Arial Bold", 11))
lbl5.grid(column=0, row=5)
body = Entry(window,width=30)
body.grid(column=1, row=5)


def clicked():
    a = combo.get()
    b = sender.get()
    c = passusr.get()
    d = reminder.get()
    e = subject.get()
    f = body.get()
    msg = MIMEMultipart()
    message = str(f)
    password = str(c)
    msg['From'] = str(b)
    msg['To'] = str(d)
    msg['Subject'] = str(e)
    msg.attach(MIMEText(message, 'plain'))
    temp = str('smtp.'+a+':587')
    server = smtplib.SMTP(temp)
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    messagebox.showwarning('Correo electronico con SMTP', 'Se ha enviado el correo')

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=6)
    
window.mainloop()
