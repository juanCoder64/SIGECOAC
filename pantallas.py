import tkinter as tk
from tkinter import ttk
import tkcalendar
import datos
import datetime


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
            self.root.switch_frame(Profesor,usuario)
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
    def __init__(self, root,name):
        self.name=name
        super().__init__(root)
        self.root = root

        self.root.title("Profesor")
        tk.Label(self, text="Profesor").pack()
        tk.Button(self, text="Actualizar disponibilidad", command=self.actualizarDisponibilidad).pack()

    def actualizarDisponibilidad(self):
        self.root.switch_frame(Calendario,self.name)
        print("Actualizar disponibilidad")


class Calendario(tk.Frame):
    # show days of the week and options to select hours for each day
    def __init__(self, root, profesor):
        super().__init__(root)
        self.profesor = profesor
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
        horario= [[], [], [], [], [], [], []]
        for i, var in enumerate(self.hours_selected):
            if var.get():
                print(self.days[i // len(self.hours)], self.hours[i % len(self.hours)])
                horario[i // len(self.hours)].append(self.hours[i % len(self.hours)])
        print(horario)
        # update profesor horarioDisponible
        for p in datos.objProf:
            if p.nombre == self.profesor:
                p.horarioDisponible = horario
                break
        # save selected hours
        # return to previous frame
        self.root.switch_frame(Estudiante)


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
        for p in datos.objProf:
            if p.nombre == profesor:
                self.root.switch_frame(seleccionaDia, p)
                break


class seleccionaDia(tk.Frame):
    #select day on a month calendar table
    def __init__(self, root, profesor):
        self.profesor = profesor
        super().__init__(root)
        self.root = root
        self.root.title("Selecciona Día")
        tk.Label(self, text="Selecciona Día").pack()
        self.cal = tkcalendar.Calendar(self)
        self.cal.pack()
        tk.Button(self, text="Seleccionar", command=self.seleccionar).pack()
        tk.Button(self, text="Volver a seleccionar profesor",
                  command=lambda: root.switch_frame(seleccionaProfesor)).pack()

    def seleccionar(self):
        dia = self.cal.selection_get()
        diaSem = dia.strftime("%A")
        print(f"Día seleccionado: {diaSem}")
        if diaSem == "Saturday" or diaSem == "Sunday":
            tk.Label(self, text="No hay consultas disponibles para este día").pack()
            self.root.switch_frame(seleccionaDia, self.profesor)
        else:
            if diaSem == "Monday":
                diaSem = 0
            elif diaSem == "Tuesday":
                diaSem = 1
            elif diaSem == "Wednesday":
                diaSem = 2
            elif diaSem == "Thursday":
                diaSem = 3
            elif diaSem == "Friday":
                diaSem = 4
        self.root.switch_frame(mostrarHorarioProfesor, self.profesor, diaSem)


class mostrarHorarioProfesor(tk.Frame):
    def __init__(self, root, profesor, diaSem):
        super().__init__(root)
        self.root = root
        self.profesor = profesor
        self.root.title("Horario Profesor")
        self.diaSem = diaSem
        self.profesor = profesor
        tk.Label(self, text=f"Horas disponibles para el profesor {profesor.nombre}").pack()
        print(diaSem)
        print(profesor.horarioDisponible)
        self.combobox = ttk.Combobox(self, values=profesor.horarioDisponible[diaSem])
        self.combobox.pack()
        tk.Button(self, text="Programar consulta", command=self.programarConsulta).pack()
        tk.Button(self, text="Volver a seleccionar profesor",
                  command=lambda: root.switch_frame(seleccionaProfesor)).pack()

    def programarConsulta(self):
        hora = self.combobox.get()
        print(self.profesor.horarioDisponible[self.diaSem])
        (self.profesor.horarioDisponible[self.diaSem]).remove(hora)
        print(self.profesor.horarioDisponible)
        print("dia: ", self.diaSem)
        print(f"Hora seleccionada: {hora}")
        print("Programar consulta")
        self.root.switch_frame(Estudiante)
