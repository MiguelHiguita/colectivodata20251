import pandas as pd

dataFrameAsistencias = pd.read_csv("./data/asistencia_estudiantes_completo.csv")

# print(dataFrameAsistencias)

# print(dataFrameAsistencias.head())
# print(dataFrameAsistencias.tail())
# print(dataFrameAsistencias.info())
# print(dataFrameAsistencias.describe())
print(dataFrameAsistencias['estrato'].value_counts().head(2))
# print(dataFrameAsistencias)
