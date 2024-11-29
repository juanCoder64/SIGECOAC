import tkinter as tk
from tkinter import ttk
import tkcalendar
import datos
import clases


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
            est = datos.objEst[datos.estudiantes.index((usuario, contrasena))]
            self.root.switch_frame(Estudiante, est)
        elif (usuario, contrasena) in datos.profesores:
            print("Profesor")
            self.result_label.config(text="Cuenta de tipo profesor")
            prof = datos.objProf[datos.profesores.index((usuario, contrasena))]
            self.root.switch_frame(Profesor, prof)
        else:
            self.result_label.config(text="Usuario o contraseña incorrectos")


class Estudiante(tk.Frame):
    def __init__(self, root, usuario):
        super().__init__(root)
        self.root = root
        self.usuario = usuario
        self.root.title("Estudiante")
        tk.Label(self, text="Estudiante").pack()
        tk.Button(self, text="Programar consulta", command=self.programarConsulta).pack()
        tk.Button(self, text="Cancelar consulta", command=self.cancelarConsulta).pack()
        tk.Button(self, text="Revisar consultas", command=self.mostrarConsultas).pack()
        tk.Button(self, text="Consultar horario", command=self.visualizarHorario).pack()
        tk.Button(self, text="Volver al login", command=lambda: root.switch_frame(Login)).pack()
        if usuario.notificaciones:
            tk.Label(self, text="Notificaciones").pack()
            for n in usuario.notificaciones:
                if n.estado == 0:
                    tk.Label(self, text=n.mensaje).pack()
                    n.leerNotificacion()

    def programarConsulta(self):
        print("Programar consulta")
        self.root.switch_frame(seleccionaProfesor, self.usuario)

    def cancelarConsulta(self):
        print("Cancelar consulta")
        self.root.switch_frame(CancelarConsulta, self.usuario)

    def mostrarConsultas(self):
        print("Mostrar consultas")
        self.root.switch_frame(RevisarConsultas, self.usuario)

    def visualizarHorario(self):
        print("Visualizar horario")
        self.root.switch_frame(ConsultarHorario, self.usuario)


class Profesor(tk.Frame):
    def __init__(self, root, user):
        self.user = user
        super().__init__(root)
        self.root = root

        self.root.title("Profesor")
        tk.Label(self, text="Profesor").pack()
        tk.Button(self, text="Ingresar Horario", command=self.actualizarDisponibilidad).pack()
        tk.Button(self, text="Revisar Consultas", command=self.revisarConsultas).pack()
        tk.Button(self, text="Consultar Horario", command=self.consultarHorario).pack()
        tk.Button(self, text="Cancelar Consultas", command=self.cancelarConsultas).pack()
        tk.Button(self, text="Confirmar Consultas", command=self.confirmarConsultas).pack()
        tk.Button(self, text="Volver al login", command=lambda: root.switch_frame(Login)).pack()
        if user.notificaciones:
            tk.Label(self, text="Notificaciones").pack()
            for n in user.notificaciones:
                if n.estado == 0:
                    tk.Label(self, text=n.mensaje).pack()
                    n.leerNotificacion()

    def actualizarDisponibilidad(self):
        self.root.switch_frame(Calendario, self.user)
        print("Actualizar disponibilidad")

    def revisarConsultas(self):
        print("Revisar consultas")
        self.root.switch_frame(RevisarConsultas, self.user)

    def consultarHorario(self):
        print("Consultar horario")
        self.root.switch_frame(MostrarHorario, self.user, 0)

    def cancelarConsultas(self):
        print("Cancelar consultas")
        self.root.switch_frame(CancelarConsulta, self.user)

    def confirmarConsultas(self):
        print("Confirmar consultas")
        self.root.switch_frame(ConfirmarConsulta, self.user)


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
        horario = [[], [], [], [], []]
        for i, var in enumerate(self.hours_selected):
            if var.get():
                print(self.days[i // len(self.hours)], self.hours[i % len(self.hours)])
                horario[i // len(self.hours)].append(self.hours[i % len(self.hours)])
        print(horario)
        self.profesor.horarioDisponible = horario
        self.root.switch_frame(Profesor, self.profesor)


class seleccionaProfesor(tk.Frame):
    def __init__(self, root, usuario):
        super().__init__(root)
        self.root = root
        self.usuario = usuario
        self.root.title("Selecciona Profesor")
        tk.Label(self, text="Selecciona Profesor").pack()
        tk.Label(self, text="Profesores disponibles").pack()
        self.profesores_combobox = ttk.Combobox(self, values=datos.profesDisponibles)
        self.profesores_combobox.pack()
        tk.Button(self, text="Seleccionar", command=self.seleccionar).pack()

    def seleccionar(self):
        profesor = self.profesores_combobox.get()
        print(f"Profesor seleccionado: {profesor}")
        for p in datos.objProf:
            if p.nombre == profesor:
                self.root.switch_frame(seleccionaDia, p, self.usuario)
                break


class seleccionaDia(tk.Frame):
    #select day on a month calendar table
    def __init__(self, root, profesor, usuario):
        self.profesor = profesor
        self.usuario = usuario
        super().__init__(root)
        self.root = root
        self.root.title("Selecciona Día")
        tk.Label(self, text="Selecciona Día").pack()
        self.cal = tkcalendar.Calendar(self)
        self.cal.pack()
        tk.Button(self, text="Seleccionar", command=self.seleccionar).pack()

    def seleccionar(self):
        dia = self.cal.selection_get()
        print(dia)
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
        self.root.switch_frame(mostrarHorarioProfesor, self.profesor, diaSem, dia, self.usuario)


class mostrarHorarioProfesor(tk.Frame):
    def __init__(self, root, profesor, diaSem, dia, estudiante):
        super().__init__(root)
        self.estudiante = estudiante
        self.root = root
        self.profesor = profesor
        self.root.title("Horario Profesor")
        self.diaSem = diaSem
        self.dia = dia
        self.profesor = profesor
        tk.Label(self, text=f"Horas disponibles para el profesor {profesor.nombre}").pack()
        print(diaSem)
        print(profesor.horarioDisponible)
        self.combobox = ttk.Combobox(self, values=profesor.horarioDisponible[diaSem])
        self.combobox.pack()
        tk.Label(self, text="Notas").pack()
        self.notas = tk.Entry(self)
        self.notas.pack()

        tk.Button(self, text="Programar consulta", command=self.programarConsulta).pack()

    def programarConsulta(self):
        hora = self.combobox.get()
        if hora not in self.profesor.horarioDisponible[self.diaSem]:
            self.root.switch_frame(seleccionaDia, self.profesor, self.estudiante)
            return
        self.estudiante.programarConsulta(self.profesor, self.estudiante, self.diaSem, hora, self.dia, self.notas.get(), 2)
        self.root.switch_frame(Estudiante, self.estudiante)


class RevisarConsultas(tk.Frame):
    def __init__(self, root, usuario):
        super().__init__(root)
        self.root = root
        self.root.title("Mostrar Consultas")
        tk.Label(self, text="Mostrar Consultas").pack()
        self.usuario = usuario
        self.consultas = []
        for c in self.usuario.revisarConsultas():
            if c.estado != 0:
                self.consultas.append(c)
        if len(self.consultas) == 0:
            tk.Label(self, text="No hay consultas disponibles").pack()
        else:
            for c in self.consultas:
                tk.Label(self, text=f"Consulta con {c.profesor.nombre} el {c.fecha[0]} a las {c.fecha[1]}").pack()
                tk.Label(self, text=f"Notas: {c.notas}").pack()
                estado = "Pendiente"
                if c.estado == 1:
                    estado = "Confirmada"
                tk.Label(self, text=f"Estado: {estado}").pack()

        tk.Button(self, text="Volver", command=self.volver).pack()

    def volver(self):
        if isinstance(self.usuario, clases.estudiante):
            self.root.switch_frame(Estudiante, self.usuario)
        else:
            self.root.switch_frame(Profesor, self.usuario)


class CancelarConsulta(tk.Frame):
    def __init__(self, root, usuario):
        super().__init__(root)
        self.root = root
        self.root.title("Cancelar Consulta")
        tk.Label(self, text="Cancelar Consulta").pack()
        self.usuario = usuario
        self.consultas = []
        for c in self.usuario.consultasVigentes:
            if c.estado != 0:
                self.consultas.append(c)
        if len(self.consultas) == 0:
            tk.Label(self, text="No hay consultas disponibles").pack()
        else:
            for c in self.consultas:
                if self.usuario == c.estudiante:
                    tk.Label(self, text=f"Consulta con {c.profesor.nombre} el {c.fecha[0]} a las {c.fecha[1]}").pack()
                else:
                    tk.Label(self, text=f"Consulta con {c.estudiante.nombre} el {c.fecha[0]} a las {c.fecha[1]}").pack()
                tk.Label(self, text=f"Notas: {c.notas}").pack()
                estado = "Pendiente"
                if c.estado == 1:
                    estado = "Confirmada"
                tk.Label(self, text=f"Estado: {estado}").pack()
                tk.Button(self, text="Cancelar consulta", command=lambda: self.cancelarConsulta(c)).pack()

        tk.Button(self, text="Volver", command=self.volver).pack()

    def volver(self):
        if isinstance(self.usuario, clases.estudiante):
            self.root.switch_frame(Estudiante, self.usuario)
        else:
            self.root.switch_frame(Profesor, self.usuario)

    def cancelarConsulta(self, consulta):
        print("Cancelar consulta")
        self.usuario.cancelarConsulta(consulta)
        self.volver()


class ConfirmarConsulta(tk.Frame):
    def __init__(self, root, usuario):
        super().__init__(root)
        self.root = root
        self.root.title("Confirmar Consulta")
        tk.Label(self, text="Confirmar Consulta").pack()
        self.usuario = usuario
        self.consultas = []
        for c in self.usuario.consultasVigentes:
            if c.estado == 2:
                self.consultas.append(c)
        if len(self.consultas) == 0:
            tk.Label(self, text="No hay consultas disponibles").pack()
        else:
            for c in self.consultas:
                tk.Label(self, text=f"Consulta con {c.profesor.nombre} el {c.fecha[0]} a las {c.fecha[1]}").pack()
                tk.Label(self, text=f"Notas: {c.notas}").pack()
                estado = "Pendiente"
                if c.estado == 1:
                    estado = "Confirmada"
                tk.Label(self, text=f"Estado: {estado}").pack()
                tk.Button(self, text="Confirmar consulta", command=lambda: self.confirmarConsulta(c)).pack()

        tk.Button(self, text="Volver", command=self.volver).pack()

    def volver(self):
        if isinstance(self.usuario, clases.estudiante):
            self.root.switch_frame(Estudiante, self.usuario)
        else:
            self.root.switch_frame(Profesor, self.usuario)

    def confirmarConsulta(self, consulta):
        print("Confirmar consulta")
        self.usuario.confirmarConsulta(consulta)
        self.root.switch_frame(Profesor, self.usuario)


class ConsultarHorario(tk.Frame):
    def __init__(self, root, usuario):
        super().__init__(root)
        self.root = root
        self.root.title("Consultar Horario")
        tk.Label(self, text="Consultar Horario").pack()
        self.usuario = usuario
        tk.Label(self, text="Seleccione profesor").pack()
        self.profesores_combobox = ttk.Combobox(self, values=datos.profesDisponibles)
        self.profesores_combobox.pack()
        tk.Button(self, text="Seleccionar", command=self.seleccionar).pack()
        tk.Button(self, text="Volver", command=self.volver).pack()

    def volver(self):
        if isinstance(self.usuario, clases.estudiante):
            self.root.switch_frame(Estudiante, self.usuario)
        else:
            self.root.switch_frame(Profesor, self.usuario)

    def seleccionar(self):
        profesor = self.profesores_combobox.get()
        print(f"Profesor seleccionado: {profesor}")
        p = self.usuario.visualizarHorario(profesor)
        self.root.switch_frame(MostrarHorario, p,1)


class MostrarHorario(tk.Frame):
    def __init__(self, root, usuario, estudiante):
        super().__init__(root)
        self.root = root
        self.root.title("Mostrar Horario")
        tk.Label(self, text="Mostrar Horario").pack()
        self.usuario = usuario
        self.estudiante = estudiante
        self.horario = usuario.horarioDisponible
        frame = tk.Frame(self)
        frame.pack()
        for i, dia in enumerate(self.horario):
            day_frame = tk.Frame(frame)
            day_frame.pack(side=tk.LEFT, padx=5, pady=5)
            tk.Label(day_frame, text=datos.dias[i]).pack()
            for hora in dia:
                tk.Label(day_frame, text=hora).pack()
        tk.Button(self, text="Volver", command= self.volver).pack()

    def volver(self):
        if self.estudiante:
            self.root.switch_frame(Estudiante, self.usuario)
        else:
            self.root.switch_frame(Profesor, self.usuario)
