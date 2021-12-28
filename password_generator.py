import webbrowser
import string
import ctypes
import glob
from random import randint, choice
from tkinter import *

ctypes.windll.user32.MessageBoxW(0, "Bienvenue sur le générateur de mots de passe", "Accueil", 64)


def console():


    print("language is English")
    note1 = str(input("close or restard app"))
    print(note1)
    note2 = str(input("are you sure ?"))
    print(note2)
    if note1 == str("close") and note2 == str("yes"):
        window.quit()
        print("close")
    elif note1 == str("restard") and note2 == str("yes"):
        ctypes.windll.user32.MessageBoxW(0, "redémarage de l'application", "Restard", 64)
        window_relod()
        print("restard")
    elif note1 == str("close") and note2 == str("no"):
        ctypes.windll.user32.MessageBoxW(0, "redémarage de l'application", "Restard", 64)
        window_relod()
        print("restard")
    else:
        print("error")
        ctypes.windll.user32.MessageBoxW(0, "ERROR", "ALERT", 20)


def exit():
    ctypes.windll.user32.MessageBoxW(0, "voulez vous vraiment fermer le générateur de mots de passe", "Exit manager", 20)
    window.quit()
    print("app fermer")


def open_credit():
    ctypes.windll.user32.MessageBoxW(0, "Credit:\njetbrain pycharm\ngraven sur youtube\nfranck inc | tout droit réserver\n", "Credit", 64)


def repertoire():
    arr = glob.glob('..\*.txt')
    count = 0
    for filename in arr:
        print(filename)
        count += 1
    print("d")
    file_index = ("L'historique ce trouve ici: E:" + filename)
    ctypes.windll.user32.MessageBoxW(0, str(file_index), "répertoire trouvé", 64)


def reset_window():
    ctypes.windll.user32.MessageBoxW(0, "Tout les mots de passe engeristrer vont être suprimé", "Warning!", 19)
    ctypes.windll.user32.MessageBoxW(0, "Tout les mots de passe engeristrer ont été suprimé correctement", "Réusite", 68)
    print("reset")
    file = open("historique.txt", "w+")
    file.write(".")
    file.close()


def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for _ in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    file = open("historique.txt", "a+")
    file.write(password + "\n")
    file.close()
    print(password)


def open_virusvirus04_channel():
    webbrowser.open_new("https://www.youtube.com/channel/UCe_4umq8TytJwk0fqkA7wgQ")


def window_relod():
   # creer la fenetre
    window = Tk()
    window.title("Générateur de mot de passe V3.2")
    window.geometry("1090x710")
    window.minsize(1085, 705)
    window.maxsize(1100, 720)
    window.iconbitmap("images_edited.ico")
    window.config(background='#4065A4')

    # creer la frame principale
    frame = Frame(window, bg='#4065A4')

    # creation d'image
    width = 770
    height = 577
    image = PhotoImage(file="logo_image.png").zoom(40).subsample(32)
    canvas = Canvas(frame, width=width, height=height, bg='#4065A4', bd=0)
    canvas.create_image(width / 2, height / 2, image=image)

    # creer une sous boite
    right_frame = Frame(frame, bg='#4065A4', )

    canvas.grid(row=0, column=0, sticky=W)
    frame.pack(expand=YES)

    # créer titre
    label_title = Label(right_frame, text="Mot de passe", font=("Courrier", 20), bg='#4065A4', fg='white')
    label_title.pack()

    # creer un champs/input

    password_entry = Entry(right_frame, font=("Courrier", 20), bg='#4065A4', fg='white')
    password_entry.pack()

    # creer un bouton
    password_button = Button(right_frame, text="Générer", font=("Courrier", 20), bg='#4065A4', fg='white',
                             command=generate_password)
    password_button.pack(fill=X)

    # bare de menu
    menu_bar = Menu(window)
    menu_bar1 = Menu(window, )
    # creer un premier menu
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="repertoire", command=repertoire)
    file_menu.add_command(label="my channel", command=open_virusvirus04_channel)
    file_menu.add_command(label="credit", command=open_credit)
    file_menu.add_command(label="open console", command=console)
    file_menu.add_command(label="Nouveau", command=generate_password)
    file_menu.add_command(label="suprimer les mots de passe engeristrer", command=reset_window)
    file_menu.add_command(label="Quitter", command=quit)

    menu_bar.add_cascade(label="Fichier", menu=file_menu)

    # config code
    right_frame.grid(row=0, column=2, sticky=W)

    # config fentre
    window.config(menu=menu_bar)

    #loop
    window.mainloop()
    print("language is English")
    note1 = str(input("close or restard app"))
    print(note1)
    note2 = str(input("are you sure ?"))
    print(note2)
    if note1 == str("close") and note2 == str("yes"):
        window.quit()
        print("close")
    elif note1 == str("restard") and note2 == str("yes"):
        ctypes.windll.user32.MessageBoxW(0, "redémarage de l'application", "Restard", 64)
        window_relod()
        print("restard")
    elif note1 == str("close") and note2 == str("no"):
        ctypes.windll.user32.MessageBoxW(0, "redémarage de l'application", "Restard", 64)
        window_relod()
        print("restard")
    else:
        print("error")
        ctypes.windll.user32.MessageBoxW(0, "ERROR", "ALERT", 20)


# creer la fenetre
window = Tk()
window.title("Générateur de mot de passe V3.1")
window.geometry("1090x710")
window.minsize(1085, 705)
window.maxsize(1100, 720)
window.iconbitmap("images_edited.ico")
window.config(background='#4065A4')

# creer la frame principale
frame = Frame(window, bg='#4065A4')

# creation d'image
width = 770
height = 577
image = PhotoImage(file="logo_image.png").zoom(40).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg='#4065A4', bd=0)
canvas.create_image(width / 2, height / 2, image=image)

# creer une sous boite
right_frame = Frame(frame, bg='#4065A4', )

canvas.grid(row=0, column=0, sticky=W)
frame.pack(expand=YES)

# créer titre
label_title = Label(right_frame, text="Mot de passe", font=("Courrier", 20), bg='#4065A4', fg='white')
label_title.pack()

# creer un champs/input

password_entry = Entry(right_frame, font=("Courrier", 20), bg='#4065A4', fg='white')
password_entry.pack()

# creer un bouton
password_button = Button(right_frame, text="Générer", font=("Courrier", 20), bg='#4065A4', fg='white',
                         command=generate_password)
password_button.pack(fill=X)

# bare de menu
menu_bar = Menu(window)
menu_bar1 = Menu(window, )
# creer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="repertoire", command=repertoire)
file_menu.add_command(label="my channel", command=open_virusvirus04_channel)
file_menu.add_command(label="credit", command=open_credit)
file_menu.add_command(label="open console", command=console)
file_menu.add_command(label="restard", command=window_relod)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="suprimer les mots de passe engeristrer", command=reset_window)
file_menu.add_command(label="Quitter", command=quit)

menu_bar.add_cascade(label="Fichier", menu=file_menu)

# config code
right_frame.grid(row=0, column=2, sticky=W)

# config fentre
window.config(menu=menu_bar)

# afficher la fenetre
window.mainloop()
print("language is English")
note1 = str(input("close or restard app"))
print(note1)
note2 = str(input("are you sure ?"))
print(note2)
if note1 == str("close") and note2 == str("yes"):
    window.quit()
    print("close")
elif note1 == str("restard") and note2 == str("yes"):
    ctypes.windll.user32.MessageBoxW(0, "redémarage de l'application", "Restard", 64)
    window_relod()
    print("restard")
elif note1 == str("close") and note2 == str("no"):
    ctypes.windll.user32.MessageBoxW(0, "redémarage de l'application", "Restard", 64)
    window_relod()
    print("restard")
else:
    print("error")
    ctypes.windll.user32.MessageBoxW(0, "ERROR", "ALERT", 20)
    console()