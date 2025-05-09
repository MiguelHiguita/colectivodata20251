import pandas as pd

dataFrameAsistencia=pd.read_csv(r"C:\Users\aprendizps1\OneDrive - GCO\Escritorio\proyecto_juanjo\colectivodata20251\data\asistencia_estudiantes_completo.csv")

#ANTES DE FILTRAR COMO ANALISTAS DE DATOS DEBES CONOCER (EXPLORAR LA FUENTE PRIMARIA)
# print(f"Columnas del dataframe: \n\n{dataFrameAsistencia.columns}\n\n")

# print(f"Id de estudiantes unicos: \n\n{dataFrameAsistencia['id_estudiante'].unique()}\n\n")
# print(f"Id de grupos unicos: \n\n{dataFrameAsistencia['id_grupo'].unique()}\n\n")
# print(f"Fechas unicas: \n\n{dataFrameAsistencia['fecha'].unique()}\n\n")
# print(f"Estados unicos: \n\n{dataFrameAsistencia['estado'].unique()}\n\n")
# print(f"Estratos unicos: \n\n {dataFrameAsistencia['estrato'].unique()}\n\n")
# print(f"Medios de transporte unicos: \n\n{dataFrameAsistencia['medio_transporte'].unique()}\n\n")

#FILTROS Y CONDICIONES PARA TRANSOFRMAR DATOS

print('#1. Reportar todos los estudiantes que asistieron\n')
estudiantesQueAsistieron=dataFrameAsistencia.query('estado=="asistio"')
print(estudiantesQueAsistieron.head(20))

print('\n\n#2. Reportar todos los estudiantes que faltaron\n')
estudiantesQueNoAsistieron=dataFrameAsistencia.query('estado=="inasistencia"')
print(estudiantesQueNoAsistieron.head(20))

print('\n\n#3. Reportar todos los estudiantes que llegaron tarde(Justificado)\n')
estudiantesQueLLegaronTarde=dataFrameAsistencia.query('estado=="justificado"')
print(estudiantesQueLLegaronTarde.head(20))

print('\n\n#4. Reportar todos los estudiantes de estrato 1\n')
estudiantesEstratoUno=dataFrameAsistencia.query('estrato==1')
print(estudiantesEstratoUno.head(20))

print('\n\n#5. Reportar todos los estudiantes de estratos altos\n')
estudiantesEstratosAltos=dataFrameAsistencia.query('estrato>=4')
print(estudiantesEstratosAltos.head(20))

print('\n\n#6. Reportar todos los estudaintes que llegan en metro\n')
estudiantesQueUsanMetro=dataFrameAsistencia.query('medio_transporte=="metro"')
print(estudiantesQueUsanMetro[['id_estudiante', 'fecha', 'estado', 'estrato', 'medio_transporte']].head(20))

print('\n\n#7. Reportar todos los estudaintes que llegan en bicicleta\n')
estudiantesQueUsanBicicleta=dataFrameAsistencia.query('medio_transporte=="bicicleta"')
print(estudiantesQueUsanBicicleta.head(20))

print('\n\n#8. Reportar todos los estudiantes que no caminan para llegar a la u\n')
estudiantesQueNoCaminan=dataFrameAsistencia.query('medio_transporte!="a pie"')
print(estudiantesQueNoCaminan.head(20))

print('\n\n#9. Reportar todos los registros de asistencia del mes de junio\n')
asistenciaJunio=dataFrameAsistencia.query('fecha>="2025-06-01" and fecha<="2025-06-30"')
if not asistenciaJunio.empty:
    print(asistenciaJunio.head(20))
else:
    print("No hay registros de asistencia en junio")

print('\n\n#10. Reportar los estudaintes que faltaron y usan bus para llegar a la u\n')
estudiantesQueFaltanUsanBus=dataFrameAsistencia.query('medio_transporte=="bus" and estado=="inasistencia"')
print(estudiantesQueFaltanUsanBus[['id_estudiante', 'fecha', 'estado', 'estrato', 'medio_transporte']].head(20))

print('\n\n#11. Reportar estudiantes que usan bus y son de estratos altos\n')
estudiantesQueUsanBusEstratosAltos=dataFrameAsistencia.query('medio_transporte=="bus" and estrato>=4')
print(estudiantesQueUsanBusEstratosAltos[['id_estudiante', 'fecha', 'estado', 'estrato', 'medio_transporte']].head(20))

print('\n\n#12. Reportar estudiantes que usan bus y son de estratos bajos\n')
estudiantesQueUsanBusEstratosBajos=dataFrameAsistencia.query('medio_transporte=="bus" and estrato<=3')
print(estudiantesQueUsanBusEstratosBajos[['id_estudiante', 'fecha', 'estado', 'estrato', 'medio_transporte']].head(20))

print('\n\n#13. Reportar estudiantes que llegan tarde y son de estrato 3,4,5 o 6\n')
estudiantesQueLLegaronTardeEstratosAltos=dataFrameAsistencia.query('estado=="justificado" and estrato>=3')
print(estudiantesQueLLegaronTardeEstratosAltos.head(20))

print('\n\n#14. Reportar estudiantes que usan transportes ecologicos\n')
estudiantesQueUsanTransporteEcologico=dataFrameAsistencia.query('medio_transporte=="bicicleta" or medio_transporte=="a pie" or medio_transporte=="metro"')
print(estudiantesQueUsanTransporteEcologico.head(20))

print('\n\n#15. Reportar estudiantes que faltan y usan carro para transportarse\n')
estudiantesQueFaltanUsanCarro=dataFrameAsistencia.query('estado=="inasistencia" and medio_transporte=="carro"')
print(estudiantesQueFaltanUsanCarro[['id_estudiante', 'fecha', 'estado', 'estrato', 'medio_transporte']].head(20))

print('\n\n#16. Reportar estudiantes que asisten son estratos altos y caminan\n')
estudiantesAsistenEstratosAltosCaminan=dataFrameAsistencia.query('estado=="asistio" and estrato>=4 and medio_transporte=="a pie"')
print(estudiantesAsistenEstratosAltosCaminan.head(20))

print('\n\n#17. Reportar estudiantes que son estratos bajos y justifican su iniasistencia\n')
estudiantesEstratosBajosJustificanInasistencia=dataFrameAsistencia.query('estado=="justificado" and estrato<=3')
print(estudiantesEstratosBajosJustificanInasistencia.head(20))

print('\n\n#18. Reportar estudiantes que son estratos altos y justifican su iniasistencia\n')
estudiantesEstratosAltosJustificanInasistencia=dataFrameAsistencia.query('estado=="justificado" and estrato>=4')
print(estudiantesEstratosAltosJustificanInasistencia.head(20))

print('\n\n#19. Reportar estudiantes que usan carro y justifican su inasistencia\n')
estudiantesUsanCarroJustificanInasistencia=dataFrameAsistencia.query('medio_transporte=="carro" and estado=="justificado"')
print(estudiantesUsanCarroJustificanInasistencia.head(20))

print('\n\n#20. Reportar estudiantes que faltan y usan metro y son estratos medios\n')
estudiantesFaltanUsanMetroEstratosMedios=dataFrameAsistencia.query('estado=="inasistencia" and medio_transporte=="metro" and estrato==3')
print(estudiantesFaltanUsanMetroEstratosMedios[['id_estudiante', 'fecha', 'estado', 'estrato', 'medio_transporte']].head(20))

#AGRUPACIONES Y CONTEOS SOBRE LOS DATOS

print('\n\n#1. Contar cada registro de asistencia por cada estado\n')
conteoRegistrosPorEstado=dataFrameAsistencia.groupby('estado').size()
print(conteoRegistrosPorEstado)

print('\n\n# 2. Numero de registros por estrato\n')
conteoRegistrosPorEstrato=dataFrameAsistencia.groupby('estrato').size()
print(conteoRegistrosPorEstrato)

print('\n\n#3. Cantidad de estudiantes por medio de transporte\n')
conteoRegistrosPorTransporte=dataFrameAsistencia.groupby('medio_transporte').size()
print(conteoRegistrosPorTransporte)

print('\n\n#4. Cantidad de registros por grupo\n')
conteoRegistrosPorGrupo=dataFrameAsistencia.groupby('id_grupo').size()
print(conteoRegistrosPorGrupo)

print('\n\n#5. Cruce entre estado y medio de transporte\n')
cruceEstadoMedioTransporte=dataFrameAsistencia.groupby(['estado','medio_transporte']).size()
print(cruceEstadoMedioTransporte)

print('\n\n#6. Promedio de estrato por estado de asistencia\n')
promedioEstratoPorEstado=dataFrameAsistencia.groupby('estado')['estrato'].mean()
print(promedioEstratoPorEstado)

print('\n\n#7. Estrato promedio por medio de transporte\n')
promedioEstratoPorTransporte=dataFrameAsistencia.groupby('medio_transporte')['estrato'].mean()
print(promedioEstratoPorTransporte)

print('\n\n#8. Maximo estrato por estado de asistencia\n')
maximoEstratoPorEstado=dataFrameAsistencia.groupby('estado')['estrato'].max()
print(maximoEstratoPorEstado)

print('\n\n#9. Minimo estrato por estado de asistencia\n')
minimoEstratoPorEstado=dataFrameAsistencia.groupby('estado')['estrato'].min()
print(minimoEstratoPorEstado)

print('\n\n#10.Conteo de asistencias por grupo y por estado\n')
conteoAsistenciasPorGrupoYEstado=dataFrameAsistencia.groupby(['id_grupo','estado']).size()
print(conteoAsistenciasPorGrupoYEstado.head(27))

print('\n\n#11. Transporte usado por cada grupo\n')
transporteUsadoPorGrupo=dataFrameAsistencia.groupby(['id_grupo','medio_transporte']).size()
print(transporteUsadoPorGrupo)

print('\n\n#12. cuantos grupos distintos registraron asistencia por fecha\n')
asistenciaGruposPorFecha=dataFrameAsistencia.groupby(['fecha','id_grupo']).size()
print(asistenciaGruposPorFecha)

print('\n\n#13. Promedio de estrato por fecha\n')
promedioEstratoPorFecha=dataFrameAsistencia.groupby('fecha')['estrato'].mean()
print(promedioEstratoPorFecha)

print('\n\n#14. Numero de tipos de estado por transporte\n')
conteoTiposEstadoPorTransporte=dataFrameAsistencia.groupby(['medio_transporte', 'estado']).size()
print(conteoTiposEstadoPorTransporte)

print('\n\n#15. Primer Registro de cada grupo\n')
primerRegistroPorGrupo=dataFrameAsistencia.groupby('id_grupo').first()
print(primerRegistroPorGrupo)