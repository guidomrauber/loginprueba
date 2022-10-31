import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import articulos

class FormularioArticulos:
    def __init__(self):
        self.articulo1=articulos.Articulos()
        self.ventana1=tk.Tk()
        self.ventana1.title("INICIO DE SESION")
        self.cuaderno1 = ttk.Notebook(self.ventana1)        
        
        self.consulta_por_codigo()
        
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    
    def consulta_por_codigo(self):
        
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="")
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="LOGIN")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe2, text="USUARIO")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe2, text="CONTRASEÑA")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcion=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe2, textvariable=self.descripcion,show="*")
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
        
        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    def consultar(self):
        datos=(self.codigo.get(), self.descripcion.get())
        respuesta=self.articulo1.consulta(datos)
        if len(respuesta)>0:
            
            mb.showinfo("Información", "INGRESO EXITOSO")
        else:
            mb.showinfo("Información", "USUARIO Y CONTRASEÑA INCORRECTO")

    
aplicacion1=FormularioArticulos()
