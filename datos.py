import clases

estudiantes = [("e", "co")]
profesores = [("profesor", "contraseña"), ("daniel", "contraseña"), ("jose", "contraseña"), ("luis", "contraseña"),
              ("jorge", "contraseña"),
              ("javier", "contraseña")]
profesDisponibles = []
objProf = []
objEst = []
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
for profe in profesores:
    profesDisponibles.append(profe[0])
    p = clases.profesor(profe[0], profe[1])
    p.horarioDisponible = [["10:00","12:00", "13:00", "14:00", "15:00", "16:00"]for _ in range(5)]
    objProf.append(p)


for es in estudiantes:
    e = clases.estudiante(es[0], es[1])
    objEst.append(e)