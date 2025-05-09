import pandas as pd

dataFrameUsuarios=pd.read_excel(r"C:\Users\aprendizps1\OneDrive - GCO\Escritorio\proyecto_juanjo\colectivodata20251\data\usuarios_sistema_completo.xlsx")

# print(f"Columnas del dataframe: \n\n{dataFrameUsuarios.columns}\n\n")

# print(f"Id unicos: \n\n{dataFrameUsuarios['id'].unique()}\n\n")
# print(f"Nombres de usuarios unicos: \n\n{dataFrameUsuarios['nombre_usuario'].unique()}\n\n")
# print(f"Contrasenas unicas: \n\n{dataFrameUsuarios['contrasena'].unique()}\n\n")
# print(f"Telefonos unicos: \n\n{dataFrameUsuarios['telefono_movil'].unique()}\n\n")
# print(f"Tipos de usuario unicos: \n\n{dataFrameUsuarios['tipo_usuario'].unique()}\n\n")
# print(f"Direcciones unicas: \n\n{dataFrameUsuarios['direccion'].unique()}\n\n")
# print(f"Fechas de nacimiento unicas: \n\n{dataFrameUsuarios['fecha_nacimiento'].unique()}\n\n")
# print(f"Especialidades unicas: \n\n{dataFrameUsuarios['especialidad'].unique()}\n\n")

print('#1. Solo estudiantes\n')
usuariosEstudiantes=dataFrameUsuarios.query('tipo_usuario=="estudiante"')
print(usuariosEstudiantes[['id', 'nombre_usuario', 'tipo_usuario', 'especialidad']].head(20))

print('\n\n#2. Solo profesores\n')
usuariosProfesores=dataFrameUsuarios.query('tipo_usuario=="docente"')
print(usuariosProfesores[['id', 'nombre_usuario', 'tipo_usuario', 'especialidad']].head(20))

print('\n\n#3. Todos excepto estudiantes\n')
usuariosNoEstudiantes=dataFrameUsuarios.query('tipo_usuario!="estudiante"')
print(usuariosNoEstudiantes[['id', 'nombre_usuario', 'tipo_usuario', 'especialidad']].head(20))

print('\n\n#4. Filtrar por especialidad\n')
usuariosFiltradosPorEspecialidad=dataFrameUsuarios.query('especialidad=="Ingenieria de Sistemas"')
print(usuariosFiltradosPorEspecialidad[['id', 'nombre_usuario', 'tipo_usuario', 'especialidad']].head(20))

print('\n\n#5. Excluir una especialidad\n')
usuariosSinIngenieriaSistemas=dataFrameUsuarios.query('especialidad!="Ingenieria de Sistemas"')
print(usuariosSinIngenieriaSistemas[['id', 'nombre_usuario', 'tipo_usuario', 'especialidad']].head(20))

print('\n\n#6. Excluir administrativos\n')
usuariosAdministrativos = dataFrameUsuarios.query('tipo_usuario=="administrativo"')
if usuariosAdministrativos.empty:
    print("No hay registros de usuarios administrativos\n")
UsuariosNoAdministrativos=dataFrameUsuarios.query('tipo_usuario!="administraivo"')
print(UsuariosNoAdministrativos[['id', 'nombre_usuario', 'tipo_usuario', 'especialidad']].head(20))

print('\n\n#7. Direcciones en medellin\n')
usuariosMedellin = dataFrameUsuarios.query('direccion.str.contains("Medellín", case=False, na=False)', engine='python')
if not usuariosMedellin.empty:
    print(usuariosMedellin[['id', 'nombre_usuario', 'direccion']].head(20))
else:
    print("No hay registros de usuarios de Medellin")

print('\n\n#8. Direcciones terminadas en sur\n')
usuariosSur = dataFrameUsuarios.query('direccion.str.contains("sur$", case=False, na=False, regex=True)', engine='python')
if not usuariosSur.empty:
    print(usuariosSur[['id', 'nombre_usuario', 'direccion']].head(20))
else:
    print("No hay registros de usuarios con direcciones que terminen en sur")

print('\n\n#9. Direcciones que inician con calle\n')
usuariosCalle = dataFrameUsuarios.query('direccion.str.contains("^calle ", case=False, na=False, regex=True)', engine = 'python')
if not usuariosCalle.empty:
    print(usuariosCalle[['id', 'nombre_usuario', 'direccion']].head(20))
else:
    print("No hay registros de usuarios con direcciones que inicien con calle")

print('\n\n#10.Especialidades que contienen la palabra datos\n')
usuariosDatos = dataFrameUsuarios.query('especialidad.str.contains("datos", case=False, na=False, regex=True)', engine='python')
if not usuariosDatos.empty:
    print(usuariosDatos[['id', 'nombre_usuario', 'tipo_usuario', 'especialidad']].head(20))
else:
    print("No hay registros de especialidades que empiecen con datos")

print('\n\n#11. instructores en itagui\n')
instructoresItagui = dataFrameUsuarios.query("tipo_usuario=='docente' and direccion.str.contains('itagui', case=False, na=False, regex=True)", engine='python')
if not instructoresItagui.empty:
    print(instructoresItagui[['id', 'nombre_usuario', 'tipo_usuario', 'direccion', 'especialidad']].head(20))
else:
    print("No hay registros de docentes de itagui")

print('\n\n#12. nacidos despues de 2000\n')
usuariosMayores = dataFrameUsuarios.query('fecha_nacimiento>="01/01/2001"')
print(usuariosMayores[['id', 'nombre_usuario', 'tipo_usuario', 'fecha_nacimiento','especialidad']].head(20))

print('\n\n#13. nacidos en los 90\n')
usuariosDeLosNoventas = dataFrameUsuarios.query('fecha_nacimiento >= "01/01/1990" and fecha_nacimiento <= "31/10/1999"')
print(usuariosDeLosNoventas[['id', 'nombre_usuario', 'tipo_usuario', 'fecha_nacimiento','especialidad']].head(20))

print('\n\n#14. direcciones en envigado\n')
usuariosEnvigado = dataFrameUsuarios.query('direccion.str.contains("envigado", case=False, na=False, regex=True)', engine='python')
if not usuariosEnvigado.empty:
    print([['id', 'nombre_usuario', 'tipo_usuario', 'direccion','especialidad']].head(20))
else:
    print("No hay registros de usuarios de envigado")

print('\n\n#15. especialdiades que empizan por I\n')
especialidadesPorI = dataFrameUsuarios.query('especialidad.str.contains("^i", case=False, na=False, regex=True)', engine='python')
print(especialidadesPorI[['id', 'nombre_usuario', 'tipo_usuario', 'especialidad']].head(20))

print('\n\n#16. usuarios sin direccion\n')
usuariosSinDireccion = dataFrameUsuarios.query('direccion.isna() or direccion=="" or direccion==" "')
if not usuariosSinDireccion.empty:
    print(usuariosSinDireccion[['id', 'nombre_usuario', 'tipo_usuario', 'direccion', 'especialidad']].head(20))
else:
    print("No hay registros de usuarios sin dirección")

print('\n\n#17. usuarios sin especialidad\n')
usuariosSinEspecialidad = dataFrameUsuarios.query('especialidad.isna() or direccion=="" or direccion==" "')
if not usuariosSinEspecialidad.empty:
    print(usuariosSinEspecialidad[['id', 'nombre_usuario', 'tipo_usuario', 'especialidad']].head(20))
else:
    print("No hay registros de usuarios sin especialidad")

print('\n\n#18. profesores que viven en sabaneta\n')
profesoresSabaneta = dataFrameUsuarios.query('tipo_usuario == "docente" and direccion.str.contains("sabaneta", case=False, na=False, regex=True)', engine='python')
if not profesoresSabaneta.empty:
    print(profesoresSabaneta[['id', 'nombre_usuario', 'tipo_usuario', 'especialidad']].head(20))
else:
    print("No hay registros de profesores de sabaneta")

print('\n\n#19. aprendices que viven en bello\n')
estudiantesBello = dataFrameUsuarios.query('tipo_usuario == "estudiante" and direccion.str.contains("bello", case=False, na=False, regex=False)')
if not profesoresSabaneta.empty:
    print(profesoresSabaneta[['id', 'nombre_usuario', 'tipo_usuario', 'especialidad']].head(20))
else:
    print("No hay registros de estudiantes de bello")

print('\n\n#20. nacidos en el nuevo milenio\n')
usuariosNuevoMilenio = dataFrameUsuarios.query('fecha_nacimiento >= "01/01/2000"')
if not usuariosNuevoMilenio.empty:
    print(usuariosNuevoMilenio[['id', 'nombre_usuario', 'tipo_usuario', 'fecha_nacimiento', 'especialidad']].head(20))
else:
    print("No hay registros de usuarios nacidos en el nuevo milenio")

print('\n\n#1. total por tipo\n')
totalPorTipo = dataFrameUsuarios.groupby('tipo_usuario').size()
print(totalPorTipo)

print('\n\n#2. total por especialidad\n')
totalPorEspecialidad = dataFrameUsuarios.groupby('especialidad').size()
print(totalPorEspecialidad)

print('\n\n#3. cantidad de especialidades distintas\n')
cantidadEspecialidades = dataFrameUsuarios['especialidad'].nunique()
print(f"Número de especialidades: {cantidadEspecialidades}")

print('\n\n#4. tipos de usuario por especialidad\n')
usuarioPorEspecialidad = dataFrameUsuarios.groupby(['especialidad', 'tipo_usuario']).size()
print(usuarioPorEspecialidad)

print('\n\n#5. usuario mas antiguo por tipo\n')
usuarioMasAntiguoPorTipo = dataFrameUsuarios.groupby('tipo_usuario')['fecha_nacimiento'].min()
print(usuarioMasAntiguoPorTipo)

print('\n\n#6. usuario mas joven por tipo\n')
usuarioMasJovenPorTipo = dataFrameUsuarios.groupby('tipo_usuario')['fecha_nacimiento'].max()
print(usuarioMasJovenPorTipo)

print('\n\n#7. primer registro por tipo\n')
primerRegistroPorTipo = dataFrameUsuarios.groupby('tipo_usuario').first()
print(primerRegistroPorTipo[['id', 'nombre_usuario', 'telefono_movil', 'especialidad']])

print('\n\n#8. ultimo registro por tipo\n')
ultimoRegistroPorTipo = dataFrameUsuarios.groupby('tipo_usuario').last()
print(ultimoRegistroPorTipo[['id', 'nombre_usuario', 'telefono_movil', 'especialidad']])

print('\n\n#9. combinacion tipo por especialidad\n')
tipoPorEspecialidad = dataFrameUsuarios.groupby(['especialidad', 'tipo_usuario']).size()
print(tipoPorEspecialidad)

print('\n\n#10. el mas viejo por especialidad\n')
masViejoPorEspecialidad = dataFrameUsuarios.groupby('especialidad')['fecha_nacimiento'].min()
print(masViejoPorEspecialidad)

print('\n\n#11. cuantos de cada especialidad por tipo\n')
cantidadEspecialidadPorTipo = dataFrameUsuarios.groupby(['tipo_usuario', 'especialidad']).size()
print(cantidadEspecialidadPorTipo)

print('\n\n#12. edad promedio por tipo\n')
edadPromedioPorTipo = dataFrameUsuarios.groupby('tipo_usuario')['fecha_nacimiento'].mean()
print(edadPromedioPorTipo)

print('\n\n#13. años de nacimeinto mas frecuente por especialidad\n')
añosMasFrecuentesPorEspecialidad = dataFrameUsuarios.groupby('especialidad')['fecha_nacimiento'].mean()
print(añosMasFrecuentesPorEspecialidad)

print('\n\n#14. mes de nacimiento mas frecuente por tipo\n')
mesNacimientoFrecuente = dataFrameUsuarios.groupby('tipo_usuario')['fecha_nacimiento'].mean()
print(mesNacimientoFrecuente)

print('\n\n#15. solo los usuarios que tengan una especialidad\n')
usuariosConEspecialidad = dataFrameUsuarios.query('especialidad.notna() and direccion!="" and direccion!=" "')
print(usuariosConEspecialidad[['id', 'nombre_usuario', 'tipo_usuario', 'especialidad']].head(20))