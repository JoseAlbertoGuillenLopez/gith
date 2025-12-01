import tkinter

ventana=tkinter.Tk()
ventana.configure(background="skyblue")

nombre_var=tkinter.StringVar()
password_var=tkinter.StringVar()

def login():
    nombre=nombre_var.get()
    password=password_var.get()

    if nombre=="admin" and password=="123":
        mensaje_label.configure(text="Bienvenido")
    else:
        mensaje_label.configure(text="Usuario o Contraseña incorrecto")

def borrar():
    mensaje_label.configure(text="")
    entry_nombre.delete(0,tkinter.END)
    entry_contra.delete(0,tkinter.END)


nombre_label=tkinter.Label(ventana,text="Usuario:",font=("Calibri",20)).pack(padx=20, pady=20)
entry_nombre=tkinter.Entry(ventana,font=("Calibri",20),textvariable=nombre_var)
entry_nombre.pack(padx=20, pady=20)
contra_label=tkinter.Label(ventana,text="Password:",font=("Calibri",20)).pack(padx=20, pady=20)

entry_contra=tkinter.Entry(ventana,font=("Calibri",20),textvariable=password_var)
entry_contra.pack(padx=20, pady=20)
boton=tkinter.Button(ventana,text="Registro",font=("Arial",20),command=login)
boton.place(x=10, y=320) #en vez de pack puedo usar place para mover los objetos o grid

boton2=tkinter.Button(ventana,text="Borrar",font=("Arial",20),command=borrar)
boton2.place(x=200, y=320)


mensaje_label=tkinter.Label(ventana,text="",font=("Arial",20),background="skyblue")
mensaje_label.pack(padx=20,pady=90)




ventana.mainloop()