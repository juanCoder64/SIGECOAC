import datos


class usuario:
    def __init__(self, nombre, contrasena):  #iniciar sesion
        self.nombre = nombre
        self.contrasena = contrasena
        self.consultasVigentes = []
        self.notificaciones = []

    def cancelarConsulta(self, consulta):
        consulta.estado = 0

    def revisarConsultas(self):
        return self.consultasVigentes

    def confirmarConsulta(self, consulta):
        consulta.estado = 1

    def visualizarHorario(self):
        for p in datos.objProf:
            if p.nombre == profesor:
                return p


class estudiante(usuario):
    def programarConsulta(self, e, p, fecha, notas, estado, objProfesor):
        con = consulta(e, p, fecha, notas, estado)
        objProfesor.consultasVigentes.append(con)
        self.consultasVigentes.append(con)


class profesor(usuario):
    horarioDisponible = [[], [], [], [], [], [], []]

    def actualizarDisponibilidad(self, horario):
        self.horarioDisponible = horario
        pass


class calendario:
    def __init__(self, horasDisponibles):
        self.horasDisponibles = horasDisponibles

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
