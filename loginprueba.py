import tkinter 
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

def inserta_datos():
    conexion1=pymysql.connect(host='localhost',
                                user='root',
                                passwd='',
                                db='bd3')
    cursor1=conexion1.cursor()
    sql="INSERT INTO login (usuario, contrasena) VALUES (%s,%s)"
    datos=(nusuario2_entrar.get(),contr2_entrar.get())
    
    try:
        cursor1.execute(sql,datos)
        conexion1.commit()
        messagebox.showinfo("AVISO","REGISTRO EXITOSO")
        
    except:
        conexion1.rollback()
        messagebox.showinfo("AVISO","NO REGISTRADO")
    conexion1.close()

def inicio_sesion():
    global pantalla1
    pantalla1=Toplevel(pantalla)
    pantalla1.geometry("800x600")
    pantalla1.title("INICIO DE SESION")
    pantalla1.iconbitmap("images.ico")
    
    Label(pantalla1, text="POR FAVOR INGRESE SU USUARIO Y CONTRASEÑA",fg="navy",width="300",height="3", font=("calibri", 25)).pack()
    Label(pantalla1,text="").pack()
    
    global nusuario_entrar
    global contr_entrar

    Label(pantalla1, text="USUARIO").pack()
    Label(pantalla1,text="").pack()
    nusuario_entrar = Entry(pantalla1)
    nusuario_entrar.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="CONTRASEÑA").pack()
    Label(pantalla1,text="").pack()
    contr_entrar = Entry(pantalla1,show="*")
    contr_entrar.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text = "INICIAR SESION", command=validacion_datos).pack()

def registrar():
    global pantalla2
    pantalla2 =Toplevel(pantalla)
    pantalla2.geometry("800x600")
    pantalla2.title("REGISTRO")
    pantalla2.iconbitmap("images.ico")

    global nusuario2_entrar
    global contr2_entrar

    nusuario2_entrar=StringVar()
    contr2_entrar=StringVar()
    Label(pantalla2).pack()
    Label(pantalla2, text="POR FAVOR INGRESE UN USUARIO Y \n CONTRASEÑA PARA REGISTRARSE",fg="navy",width="300",height="3", font=("calibri", 25)).pack()
    Label(pantalla2,text="").pack()
    
    Label(pantalla2, text="USUARIO").pack()
    Label(pantalla2,text="").pack()
    nusuario2_entrar = Entry(pantalla2)
    nusuario2_entrar.pack()
    Label(pantalla2).pack()
    Label(pantalla2, text="CONTRASEÑA").pack()
    Label(pantalla2,text="").pack()
    contr2_entrar = Entry(pantalla2, show="*")
    contr2_entrar.pack()
    Label(pantalla2).pack()

    Button(pantalla2, text = "REGISTRAR", command=inserta_datos).pack()

def validacion_datos():
    conexion1=pymysql.connect(host='localhost',
                                user='root',
                                passwd='',
                                db='bd3')
    cursor1=conexion1.cursor()
    sql="select * from login where usuario=%s and contrasena=%s"
    datos=(nusuario_entrar.get(),contr_entrar.get())
    global result 
    result=cursor1.execute(sql,datos)
    if (result)>0:
            
        messagebox.showinfo("Información", "INGRESO EXITOSO")
    else:
            messagebox.showinfo("Información", "USUARIO Y CONTRASEÑA INCORRECTO")
    conexion1.close()
    


pantalla = tk.Tk()
pantalla.geometry("800x600")
pantalla.title("BIENVENIDOS")
pantalla.iconbitmap("images.ico")
Label(text="").pack()
image = PhotoImage(file = "images.gif")
image = image.subsample(1,1)
label=Label(image=image)
label.pack()
Label(text="").pack()
Label(text="ACCESO AL SISTEMA",  fg="navy",width="300",height="1", font=("calibri", 25)).pack()

Label(text="DEL GYM",  fg="navy",width="300",height="1", font=("calibri", 25)).pack()
Label(text="").pack()
Button(text="INICIAR SESION", width="30",height="3",command =inicio_sesion).pack()
Label(text="").pack()
Button(text="REGISTRAR", width="30",height="3",command=registrar).pack()

pantalla.mainloop()





