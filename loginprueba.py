import tkinter 
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def inicio_sesion():
    global pantalla1
    pantalla1=Toplevel(pantalla)
    pantalla1.geometry("300x250")
    pantalla1.title("INICIO DE SESION")
    pantalla1.iconbitmap("images.ico")
    
    Label(pantalla1, text="POR FAVOR INGRESE SU USUARIO Y CONTRASEÑA").pack()
    Label(pantalla1,text="").pack()

    global nusuario_ver
    global contr_ver
    nusuario_ver=StringVar()
    contr_ver=StringVar()

    global nusuario_entrar
    global contr_entrar

    Label(pantalla1, text="USUARIO").pack()
    Label(pantalla1,text="").pack()
    nusuario_entrar = Entry(pantalla1, textvariable=nusuario_ver)
    nusuario_entrar.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="CONTRASEÑA").pack()
    Label(pantalla1,text="").pack()
    contr_entrar = Entry(pantalla1, textvariable=contr_ver)
    contr_entrar.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text = "INICIAR SESION").pack()

pantalla = tk.Tk()
pantalla.geometry("800x600")
pantalla.title("BIENVENIDOS")
pantalla.iconbitmap("images.ico")

image = PhotoImage(file = "images.gif")
image = image.subsample(1,1)
label=Label(image=image)
label.pack()
Label(text="ACCESO AL SISTEMA",  fg="navy",width="300",height="1", font=("calibri", 25)).pack()

Label(text="DEL GYM",  fg="navy",width="300",height="1", font=("calibri", 25)).pack()
Label(text="").pack()
Button(text="INICIAR SESION", width="30",height="3",command =inicio_sesion).pack()
Label(text="").pack()
Button(text="REGISTRAR", width="30",height="3").pack()

pantalla.mainloop()





