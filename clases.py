import datos


class usuario:
    def __init__(self, nombre, contrasena):  #iniciar sesion
        self.nombre = nombre
        self.contrasena = contrasena
        self.consultasVigentes = []
        self.notificaciones = []

    def cancelarConsulta(self, consulta):
        notificacion = Notificacion(0,consulta.profesor,f"La consulta con {consulta.estudiante.nombre} ha sido cancelada")
        notificacion.enviarNotificacion()
        diaSemana = consulta.fecha[0].weekday()
        consulta.profesor.horarioDisponible[diaSemana].append(consulta.fecha[1]).sort()
        consulta.estado = 0

    def revisarConsultas(self):
        return self.consultasVigentes

    def confirmarConsulta(self, consulta):
        consulta.estado = 1
        notificacion = Notificacion(0,consulta.estudiante,f"La consulta con {consulta.profesor.nombre} ha sido confirmada")
        notificacion.enviarNotificacion()

    def visualizarHorario(self, profesor):
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

    def cancelarConsulta(self, consulta):
        notificacion = Notificacion(0,consulta.estudiante,f"La consulta con {consulta.profesor.nombre} ha sido cancelada")
        notificacion.enviarNotificacion()
        diaSemana = consulta.fecha[0].weekday()
        consulta.profesor.horarioDisponible[diaSemana].append(consulta.fecha[1])
        consulta.profesor.horarioDisponible[diaSemana].sort()
        consulta.estado = 0

    def confirmarConsulta(self, consulta):
        consulta.estado = 1
        notificacion = Notificacion(0,consulta.estudiante,f"La consulta con {consulta.profesor.nombre} ha sido confirmada")
        notificacion.enviarNotificacion()
class calendario:
    def __init__(self, horasDisponibles):
        self.horasDisponibles = horasDisponibles

    def mostrarHorario(self):
        pass

    def modificaHorarioDisponible(self):
        pass


class Notificacion:
    def __init__(self, estado, destinatario, mensaje):  #generar notificacion
        self.estado = estado
        self.destinatario = destinatario
        self.mensaje = mensaje

    def enviarNotificacion(self):
        self.destinatario.notificaciones.append(self)
    def leerNotificacion(self):
        self.estado = 1

class consulta:
    def __init__(self, estudiante, profesor, fecha, notas, estado):  #Generar consulta
        self.estudiante = estudiante
        self.profesor = profesor
        self.fecha = fecha
        self.notas = notas
        self.estado = estado
