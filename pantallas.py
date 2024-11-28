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
        self.root.switch_frame(Calendario)
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

class Calendario(tk.Frame):
    # show days of the week and options to select hours for each day
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Calendario")
        self.days = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
        self.hours = ['8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00']
        self.day_labels = []
        self.hour_labels = []
        self.hour_checkbuttons = []
        self.hours_selected = []

        for day in self.days:
            day_frame = tk.Frame(self)
            day_frame.pack(side=tk.LEFT, padx=5, pady=5)
            label = tk.Label(day_frame, text=day)
            label.pack()
            self.day_labels.append(label)
            for hour in self.hours:
                hour_frame = tk.Frame(day_frame)
                hour_frame.pack()
                label = tk.Label(hour_frame, text=hour)
                label.pack(side=tk.LEFT)
                self.hour_labels.append(label)
                var = tk.IntVar()
                checkbutton = tk.Checkbutton(hour_frame, variable=var)
                checkbutton.pack(side=tk.LEFT)
                self.hour_checkbuttons.append(checkbutton)
                self.hours_selected.append(var)

        tk.Button(self, text="Confirmar", command=self.confirmar).pack()

    def confirmar(self):
        print("Horas seleccionadas:")
        for i, var in enumerate(self.hours_selected):
            if var.get():
                print(self.days[i // len(self.hours)], self.hours[i % len(self.hours)])
        # save selected hours
        # return to previous frame
        self.root.switch_frame(Estudiante)