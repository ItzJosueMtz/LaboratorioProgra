import wikipediaapi
#Se crea un objeto con el que se trabajará
wiki_wiki = wikipediaapi.Wikipedia('en')
#Para hacerlo mas didactico le pediremos al usuario poner el titulo para buscar una pagina web
print("Welcome to this part of the program, we'll be looking if a page exists in Wikipedia in English")
pagina=str(input("Please Insert The Name Of A Page To Look If That Page Exists:\n"))
page_py = wiki_wiki.page(pagina)
if (page_py.exists()== True):
    print("That Page Exists")
    opt1=str(input("Do you wanna get the URL of that page?\ny/n\n"))
    opt1.lower()
    if(opt1=="y"):
        print(page_py.fullurl)
    opt2=str(input("Do you want to save the link in a txt?\ny/n\n"))
    opt2.lower()
    if(opt2=="y"):
        txtcont=str(page_py.fullurl)
        print(txtcont)
        fo=open("Url_Wikipedia.txt","w")
        fo.write (str(txtcont))
        fo.close()
else:
    print("That Page Doesn't Exists")

