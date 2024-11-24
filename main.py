estudiantes = [("estudiante", "contraseña")]
profesores = [("profesor", "contraseña")]


print("Sistema de gestión de consultas académicas")
usuario = input("Ingrese nombre de usuario:")
contrasena = input("ingrese contraseña:")
if (usuario, contrasena) in estudiantes:
    # se crea entidad de estudiate y se muestran opciones de estudiante
    print("Cuenta de tipo estudiante")
elif (usuario, contrasena) in profesores:
    # se crea entidad de profesor y se muestran opciones de profesor
    print("Cuenta de tipo profesor")
else:
    print("Usuario y/o contraseña no encontrado")
