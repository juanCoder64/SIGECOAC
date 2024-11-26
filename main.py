import tkinter as tk

estudiantes = [("estudiante", "contraseña")]
profesores = [("profesor", "contraseña")]
root = tk.Tk()
root.geometry("300x300")
a = tk.Label(root, text="Sistema de Gestión de Consultas Académicas")
a.pack()

username_label = tk.Label(root, text="Usuario")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Contraseña")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

result_label = tk.Label(root, text="")
result_label.pack()


def login():
    usuario = username_entry.get()
    contrasena = password_entry.get()
    if (usuario, contrasena) in estudiantes:
        result_label.config(text="Cuenta de tipo estudiante")
    elif (usuario, contrasena) in profesores:
        result_label.config(text="Cuenta de tipo profesor")
    else:
        result_label.config(text="Usuario o contraseña incorrectos")


login_button = tk.Button(root, text="Iniciar sesión", command=login)
login_button.pack()
root.mainloop()
