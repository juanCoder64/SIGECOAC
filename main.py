import tkinter as tk

class usuario:
    def __init__(self, nombre, correo, contrasena):
        self.nombre = nombre
        self.correo = correo
        self.contrasena= contrasena
    def cancelarConsulta(self):
        pass
    def mostrarConsultas(self):
        pass
    def confirmarConsulta(self):
        pass
    def visualizarHorario(self):
        pass
    def iniciarSesion(self):
        pass

class estudiante(usuario):
    def programarConsulta(self):
        pass
class profesor (usuario):
    def actualizarDisponibilidad(self):
        pass

class calendario:
    def __init__(self, horasDisponibles):
        self.horasDisponibles=horasDisponibles;
    def mostrarHorario(self):
        pass
    def modificaHorarioDisponible(self):
        pass

class Notificacion:
    def __init__(self, estado, destinatario): #generar notificacion
        self.estado=estado
        self.destinatario=destinatario
    def enviarNotificacion(self):
        pass

class consulta:
    def __init__(self, estudiante, profesor, fecha, notas, estado):#Generar consulta
        self.estudiante=estudiante
        self.profesor=profesor
        self.fecha=fecha
        self.notas=notas
        self.estado=estado

estudiantes = [("estudiante", "contraseña")]
profesores = [("profesor", "contraseña")]
root = tk.Tk()
root.title("Sistema de Gestión de Consultas Académicas")
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
