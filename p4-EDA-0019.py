import pandas as pd
import matplotlib.pyplot as plt

## Jesus Arriaga NC 0019 
# 1. Crear diccionario con datos de consultas de laboratorio
consultas_laboratorio = {
    'id_estudio': [401, 402, 403, 404, 405, 406],
    'paciente': ['Laura', 'Pedro', 'Sofia', 'Miguel', 'Elena', 'Jorge'],
    'tipo_estudio': ['Hemograma', 'Glucosa', 'Perfil lipidico', 'Hemoglobina Glicosilada', 'Prueba alergia', 'Coproparasitoscopia'],
    'fecha_toma': ['2024-01-10', '2024-01-10', '2024-01-11', '2024-01-12', '2024-01-12', '2024-01-13'],
    'ayuno_horas': [8, 12, 12, 12, 0, 0],
    'resultado_numerico': [14.2, 105, 180, 6.8, 0, 0],
    'unidad_medida': ['g/dL', 'mg/dL', 'mg/dL', '%', 'N/A', 'N/A'],
    'rango_normal': ['12-16', '70-100', '<200', '<5.7', 'Negativo', 'Negativo'],
    'estatus': ['Normal', 'Alto', 'Alto', 'Alto', 'Negativo', 'Negativo'],
    'tecnico_laboratorio': ['Ana', 'Luis', 'Ana', 'Luis', 'Carmen', 'Carmen']
}

print('Análisis Exploratorio de Datos EDA ')
print('Exploratory Data Analysis Jesus Arriaga NC 0019')
print('📝 5. Crear el diccionario con 10 listas y 6 elementos (Consultas de laboratorio)')

# 2. Convertir diccionario en DataFrame
df = pd.DataFrame(consultas_laboratorio)
print("\n--- TABLA ORIGINAL DE CONSULTAS DE LABORATORIO ---")
print(df)

# 3. Exportar los datos a CSV
print('+-+-+-+-💾 7. Convertir el DataFrame en archivo CSV+-+-+-+-')
df.to_csv(
    'consultas_laboratorio_0019.csv',
    index=False,
    encoding='utf-8-sig'
)
print("\n✅ Archivo CSV creado correctamente")
print('+-+-📂 8. Leer los datos desde el archivo CSV+-+-')
print('consultas_laboratorio_0019.csv')

# 4. Leer el archivo CSV
df = pd.read_csv('consultas_laboratorio_0019.csv')
print("\n--- DATOS LEÍDOS DESDE CSV ---")
print(df)

print('🔍+-+- 9. Análisis Exploratorio de Datos (EDA)-+-+')
# 5. Primeros y últimos registros
print("+-+-\n1. PRIMEROS REGISTROS (Head):-+-+")
print(df.head(3)) # Muestra los primeros 3
print("+-+-\n2. ÚLTIMOS REGISTROS (Tail):-+-+")
print(df.tail(2)) # Muestra los últimos 2

# 6. Dimensiones y estructura
print("+-+- Dimensiones y estructura -+-+")
print(df) # mostrar tabla o matriz 
print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)
print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)
print("\n5. TIPOS DE DATOS:\n", df.dtypes)
print("\n6. INFORMACIÓN GENERAL:")
df.info() 

# 7. Estadísticas y limpieza
print("\n7.+-+-+-+-+ ESTADÍSTICAS DESCRIPTIVAS:-+-+--+")
print(df.describe())
print("\n8. VALORES FALTANTES (Nulls):")
print(df.isnull().sum())
print("\n9. REGISTROS DUPLICADOS:")
print(df.duplicated().sum())
print("\n10. VALORES ÚNICOS POR COLUMNA:")
print(df.nunique())
print("Técnicos únicos:", df['tecnico_laboratorio'].unique())

# 8. Análisis específico
print(df)
print('----------------------------------------------')
print("\n11. ESTUDIOS POR TÉCNICO DE LABORATORIO:")
print(df['tecnico_laboratorio'].value_counts())

print("\n12. PROMEDIO DE RESULTADO NUMÉRICO:", df['resultado_numerico'].mean())
print("13. RESULTADO NUMÉRICO MÁXIMO:", df['resultado_numerico'].max())
print("14. RESULTADO NUMÉRICO MÍNIMO:", df['resultado_numerico'].min())

# 9. Ordenamiento, filtrado y agrupación
print("\n15. ESTUDIOS ORDENADOS POR RESULTADO NUMÉRICO (Mayor a menor):")
print(df.sort_values(by='resultado_numerico', ascending=False))

print("\n16. ESTUDIOS CON AYUNO MAYOR A 8 HORAS:")
filtro = df[df['ayuno_horas'] > 8]
print(filtro)

print("\n17. RESUMEN POR TÉCNICO DE LABORATORIO:")
resumen = df.groupby('tecnico_laboratorio').agg(
    estudios=('id_estudio', 'count'),
    ayuno_promedio=('ayuno_horas', 'mean'),
    resultado_maximo=('resultado_numerico', 'max')
)
print(resumen)

# 18. Gráfica de barras: Estudios por técnico de laboratorio
print('18. Gráfica de barras: Estudios por técnico de laboratorio')
conteo = df['tecnico_laboratorio'].value_counts()
plt.figure(figsize=(8, 5))
plt.bar(conteo.index, conteo.values, color='skyblue')
plt.title('Estudios por técnico de laboratorio Jesus 0019')
plt.xlabel('Técnico de laboratorio')
plt.ylabel('Cantidad de estudios')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 19. Gráfica de barras: Resultado numérico por paciente
plt.figure(figsize=(8, 5))
plt.bar(df['paciente'], df['resultado_numerico'], color='lightgreen')
plt.title('Resultado numérico por paciente EDA por Jesus 0019')
plt.xlabel('Paciente')
plt.ylabel('Resultado numérico')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 20. Histograma: Distribución de horas de ayuno
plt.figure(figsize=(8, 5))
plt.hist(df['ayuno_horas'], bins=5, color='orange', edgecolor='black')
plt.title('Distribución de horas de ayuno EDA Jesus 0019')
plt.xlabel('Horas de ayuno')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 21. Gráfica de dispersión: Horas de ayuno vs Resultado numérico
plt.figure(figsize=(8, 5))
plt.scatter(df['ayuno_horas'], df['resultado_numerico'], color='red', s=100)
plt.title('Relación entre horas de ayuno y resultado EDA por Jesus 0019')
plt.xlabel('Horas de ayuno')
plt.ylabel('Resultado numérico')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 22. Diagrama de caja: Distribución de resultados numéricos
plt.figure(figsize=(7, 5))
plt.boxplot(df['resultado_numerico'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Distribución de resultados numéricos (Boxplot) EDA Jesus 0019')
plt.ylabel('Resultado numérico')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 23. Matriz de correlación
correlacion = df.corr(numeric_only=True)
print("\n--- MATRIZ DE CORRELACIÓN ---")
print(correlacion)
plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlacion.columns)), correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion.columns)), correlacion.columns)
plt.title('Matriz de correlación de variables numéricas EDA Jesus 0019')
plt.tight_layout()
plt.show()