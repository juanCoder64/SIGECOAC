class usuario:
    def __init__(self, nombre, contrasena):
        self.nombre = nombre
        self.contrasena = contrasena
        self.consultasVigentes = []
        self.notificaciones = []

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
    def programarConsulta(self, e, p, fecha,notas, estado, objProfesor):
        con= consulta(e, p, fecha, notas, estado)
        objProfesor.consultasVigentes.append(con)
        self.consultasVigentes.append(con)
        pass


class profesor(usuario):
    horarioDisponible = [[], [], [], [], [], [], []]
    def actualizarDisponibilidad(self, horario):
        self.horarioDisponible = horario
        pass


class calendario:
    def __init__(self, horasDisponibles):
        self.horasDisponibles = horasDisponibles;

    def mostrarHorario(self):
        pass

    def modificaHorarioDisponible(self):
        pass


class Notificacion:
    def __init__(self, estado, destinatario):  #generar notificacion
        self.estado = estado
        self.destinatario = destinatario

    def enviarNotificacion(self):
        pass


class consulta:
    def __init__(self, estudiante, profesor, fecha, notas, estado):  #Generar consulta
        self.estudiante = estudiante
        self.profesor = profesor
        self.fecha = fecha
        self.notas = notas
        self.estado = estado
