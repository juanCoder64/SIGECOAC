import tkinter as tk
from tkinter import ttk
import datos
class app(tk.Tk):
    def __init__(self):
        super().__init__()
        self._frame = None
        self.switch_frame(Login)

    def switch_frame(self, frame_class, *args):
        new_frame = frame_class(self, *args)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class Login(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root

        self.root.title("Sistema de Gestión de Consultas Académicas")
        tk.Label(self, text="Sistema de Gestión de Consultas Académicas").pack()
        tk.Label(self, text="Usuario").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()
        tk.Label(self, text="Contraseña").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()
        tk.Button(self, text="Iniciar sesión", command=self.login).pack()

    def login(self):
        usuario = self.username_entry.get()
        contrasena = self.password_entry.get()
        if (usuario, contrasena) in datos.estudiantes:
            print("Estudiante")
            self.result_label.config(text="Cuenta de tipo estudiante")
            self.root.switch_frame(Estudiante)
        elif (usuario, contrasena) in datos.profesores:
            print("Profesor")
            self.result_label.config(text="Cuenta de tipo profesor")
            self.root.switch_frame(Profesor)
        else:
            self.result_label.config(text="Usuario o contraseña incorrectos")

class Calendario(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.horasDisponibles = horasDisponibles

        self.root.title("Calendario")
        tk.Label(self, text="Calendario").pack()
        tk.Label(self, text="Horas disponibles").pack()
        self.horas_combobox = ttk.Combobox(self, values=self.horasDisponibles)
        self.horas_combobox.pack()
        tk.Button(self, text="Modificar", command=self.modificar).pack()
        tk.Button(self, text="Volver al login", command=lambda: root.switch_frame(Login)).pack()

    def modificar(self):
        hora = self.horas_combobox.get()
        print(f"Hora seleccionada: {hora}")

class Estudiante(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root

        self.root.title("Estudiante")
        tk.Label(self, text="Estudiante").pack()
        tk.Button(self, text="Programar consulta", command=self.programarConsulta).pack()
        tk.Button(self, text="Cancelar consulta", command=self.cancelarConsulta).pack()
        tk.Button(self, text="Mostrar consultas", command=self.mostrarConsultas).pack()
        tk.Button(self, text="Confirmar consulta", command=self.confirmarConsulta).pack()
        tk.Button(self, text="Visualizar horario", command=self.visualizarHorario).pack()

    def programarConsulta(self):

        self.root.switch_frame(seleccionaProfesor)
        print("Programar consulta")

    def cancelarConsulta(self):
        print("Cancelar consulta")

    def mostrarConsultas(self):
        print("Mostrar consultas")

    def confirmarConsulta(self):
        print("Confirmar consulta")

    def visualizarHorario(self):
        print("Visualizar horario")


class Profesor(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root

        self.root.title("Profesor")
        tk.Label(self, text="Profesor").pack()
        tk.Button(self, text="Actualizar disponibilidad", command=self.actualizarDisponibilidad).pack()


    def actualizarDisponibilidad(self):
        print("Actualizar disponibilidad")


class seleccionaProfesor(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root

        self.root.title("Selecciona Profesor")
        tk.Label(self, text="Selecciona Profesor").pack()
        tk.Label(self, text="Profesores disponibles").pack()
        self.profesores_combobox = ttk.Combobox(self, values=datos.profesDisponibles)
        self.profesores_combobox.pack()
        tk.Button(self, text="Seleccionar", command=self.seleccionar).pack()
        tk.Button(self, text="Volver al login", command=lambda: root.switch_frame(Login)).pack()

    def seleccionar(self):
        profesor = self.profesores_combobox.get()
        print(f"Profesor seleccionado: {profesor}")
class seleccionaDia(tk.Frame):
    def __init__(self, root, diasDisponibles):
        super().__init__(root)
        self.root = root

        self.root.title("Selecciona Día")
        tk.Label(self, text="Selecciona Día").pack()
        tk.Label(self, text="Días disponibles").pack()
        self.dias_combobox = ttk.Combobox(self, values=diasDisponibles)
        self.dias_combobox.pack()
        tk.Button(self, text="Seleccionar", command=self.seleccionar).pack()
        tk.Button(self, text="Volver al login", command=lambda: root.switch_frame(Login)).pack()

    def seleccionar(self):
        dia = self.dias_combobox.get()
        print(f"Día seleccionado: {dia}")