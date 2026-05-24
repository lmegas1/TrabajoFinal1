# 🧠 Wiki — Análisis de Salud Mental Estudiantil con Inteligencia Artificial

> **Trabajo Final** | Aplicación de IA que use librerías de software libre a través de herramientas colaborativas  
> **Plataforma:** Jupyter Lab | **Lenguaje:** Python 3.x

---

## Tabla de Contenidos

1. [Introducción](#1-introducción)
2. [Marco Teórico](#2-marco-teórico-de-las-tecnologíaslibrerías-usadas)
3. [Descripción del Dataset](#3-descripción-del-dataset-usado)
4. [Descripción de los Pasos Realizados](#4-descripción-de-los-pasos-realizados-en-el-proyecto)
   - 4.1 [Visualizaciones Generadas](#41-descripción-de-las-visualizaciones-generadas)
5. [Conclusiones](#5-conclusiones)
6. [Bibliografía](#6-bibliografía)

---

## 1. Introducción

La salud mental estudiantil representa una de las problemáticas de mayor relevancia en el contexto universitario contemporáneo. Investigaciones globales estiman que entre el 20% y el 45% de los estudiantes universitarios experimenta algún nivel de depresión, ansiedad o estrés crónico, afectando directamente su rendimiento académico, calidad de vida y desarrollo profesional.

Este proyecto aplica técnicas de **Inteligencia Artificial y Análisis de Datos** mediante herramientas de software libre para examinar, desde una perspectiva integral, la relación entre la salud mental estudiantil, el desempeño académico y el contexto socioeconómico universitario. La propuesta se distingue por el uso de **dos datasets complementarios** que comparten una clave de identificación común (`student_id`), lo que permite realizar un análisis más profundo que el que sería posible con una sola fuente de datos.

El **Dataset CSV** contiene información sobre salud mental individual de 5 000 estudiantes (síntomas de depresión, ansiedad, hábitos de sueño, estudio y actividad física). El **Dataset SQLite** complementa con datos del contexto socioeconómico y universitario de los mismos 5 000 estudiantes (carrera, universidad, financiamiento, nivel socioeconómico, horas de trabajo, satisfacción académica). La **unión de ambos** forma el dataset inicial de 32 columnas sobre el que se realiza todo el análisis.

### Objetivos del Proyecto

- **General:** Desarrollar una aplicación de IA que analice integralmente la salud mental estudiantil combinando datos individuales y contextuales, usando librerías de software libre.
- **Específicos:**
  - Combinar mediante JOIN dos datasets de 5 000 registros cada uno usando la ID compartida `student_id`.
  - Generar visualizaciones descriptivas e interactivas con Matplotlib, Bokeh y PygWalker.
  - Construir modelos predictivos de clasificación (Random Forest, Regresión Logística) y clustering (K-Means).
  - Identificar los factores contextuales y de hábitos con mayor influencia en la salud mental.

---

## 2. Marco Teórico de las Tecnologías/Librerías Usadas

### 2.1 Jupyter Lab

**JupyterLab** es un entorno de desarrollo interactivo basado en web, desarrollado por Project Jupyter. Permite trabajar con notebooks, editores, terminales y visualizadores en un espacio integrado.

- **Licencia:** BSD-3-Clause.
- **Uso en el proyecto:** Entorno principal de desarrollo. El notebook `analisis_salud_mental_IA.ipynb` integra código Python, visualizaciones y narrativa en 8 secciones estructuradas.

### 2.2 Pandas

**Pandas** es la librería estándar de manipulación y análisis de datos en Python, proporcionando estructuras de datos de alto rendimiento.

- **Funciones clave utilizadas:**
  - `read_csv()` : Carga del dataset CSV (5 000 × 15).
  - `read_sql()` : Lectura directa desde SQLite a DataFrame.
  - `merge(on='student_id', how='inner')` : JOIN entre CSV y SQLite generando el dataset inicial.
  - `groupby()`, `agg()` : Agregaciones estadísticas por carrera, universidad y nivel socioeconómico.
  - `describe()`, `info()`, `isnull().sum()` : Análisis exploratorio inicial.
- **Licencia:** BSD-3-Clause.

### 2.3 Matplotlib

**Matplotlib** es la librería de visualización más usada en Python, ofreciendo control total sobre cada elemento gráfico.

- **Tipos de gráficos generados:** Histogramas, gráficos de pastel, barras horizontales/verticales con barras de error, scatter plots, box plots, mapas de calor.
- **Características utilizadas:** `plt.subplots()` para cuadrículas multi-panel, `plt.cm` para paletas de colores, `tight_layout()` para espaciado automático, `savefig()` para exportar a PNG.
- **Licencia:** PSF License.

### 2.4 Bokeh

**Bokeh** es una librería de visualización interactiva para navegadores web, que genera gráficos con zoom, filtros y tooltips sin necesidad de JavaScript adicional.

- **Características utilizadas:**
  - `ColumnDataSource` : Estructura de datos central para gráficos interactivos.
  - `HoverTool` : Tooltips con información detallada al pasar el cursor.
  - `FactorRange` : Barras agrupadas por categorías.
  - `output_notebook()` : Renderizado directo en Jupyter.
  - `legend.click_policy = 'hide'` : Leyendas interactivas para filtrar series.
- **Licencia:** BSD-3-Clause.

### 2.5 PygWalker

**PygWalker** transforma DataFrames de Pandas en una interfaz drag-and-drop similar a Tableau, directamente dentro de Jupyter, sin necesidad de código adicional.

- **Corrección técnica aplicada:** Las columnas `int64` se convierten a `float64` antes de `pyg.walk()` para evitar el error `InvalidInputException: BIGINT -> BLOB` causado por incompatibilidad con DuckDB (motor interno). Se trabaja sobre una copia del DataFrame (`df.copy()`) para no afectar los modelos.
- **Licencia:** Apache-2.0.

### 2.6 Scikit-learn

**Scikit-learn** es la librería más completa de Machine Learning para Python, con implementaciones eficientes de decenas de algoritmos.

- **Algoritmos utilizados:**
  - `RandomForestClassifier` : Ensemble de 150 árboles de decisión con `class_weight='balanced'`. Accuracy: **65.6%**.
  - `LogisticRegression` : Modelo lineal de referencia. Accuracy: **65.1%**.
  - `KMeans` : Clustering no supervisado. k=4 seleccionado por método del codo.
  - `StandardScaler` : Normalización (media=0, std=1) para modelos sensibles a escala.
  - `train_test_split` : División 75/25 con `stratify=y`.
- **Licencia:** BSD-3-Clause.

### 2.7 SQLite

**SQLite** es un motor de base de datos relacional embebido sin servidor. Python lo incluye nativamente mediante el módulo `sqlite3`.

- **Uso en el proyecto:** Almacena el contexto socioeconómico y universitario de 5 000 estudiantes en la tabla `student_context`, compartiendo `student_id` con el CSV para permitir el JOIN.

---

## 3. Descripción del Dataset Usado

### 3.1 Dataset CSV — `student_mental_health.csv`

| Atributo | Valor |
|---|---|
| **Origen** | Dataset sintético generado con distribuciones basadas en literatura científica |
| **Formato** | CSV |
| **Registros** | 5 000 estudiantes |
| **Columnas** | 15 |
| **ID** | `student_id`: STU0001 – STU5000 |

| Variable | Tipo | Descripción |
|---|---|---|
| `student_id` | Texto | Clave primaria compartida con SQLite |
| `age` | Entero | Edad (18–24) |
| `gender` | Texto | Female / Male (50% c/u) |
| `year_of_study` | Entero | Año de carrera (1–4) |
| `cgpa` | Decimal | Promedio acumulado (1.5–4.0, media=3.75) |
| `depression` | Texto | Sí/No — 26.1% afirmativo |
| `anxiety` | Texto | Sí/No — 31.2% afirmativo |
| `panic_attack` | Texto | Sí/No |
| `sought_treatment` | Texto | Sí/No |
| `sleep_hours` | Entero | Horas de sueño/noche (3–9, media=6.31h) |
| `study_hours_per_day` | Entero | Horas de estudio diarias (1–9) |
| `social_media_hours` | Entero | Horas en redes sociales/día (1–12) |
| `physical_activity` | Texto | Low / Moderate / High |
| `academic_pressure` | Texto | Low / Moderate / High |
| `family_support` | Texto | Low / Moderate / High |

---

### 3.2 Dataset SQLite — `student_context.db`

| Atributo | Valor |
|---|---|
| **Origen** | Base de datos relacional creada para el proyecto |
| **Formato** | SQLite (.db) |
| **Tabla** | `student_context` |
| **Registros** | 5 000 |
| **Columnas** | 18 |
| **ID compartida** | `student_id`: STU0001 – STU5000 (mismo rango que el CSV) |

| Variable | Tipo | Descripción |
|---|---|---|
| `student_id` | Texto PK | Clave de relación con el CSV |
| `universidad` | Texto | 10 universidades ecuatorianas |
| `carrera` | Texto | 10 programas académicos |
| `semestre` | Entero | Semestre actual (1–8) |
| `modalidad` | Texto | Presencial / Semipresencial / Virtual |
| `financiamiento` | Texto | Beca completa / parcial / Recursos propios / Crédito |
| `residencia` | Texto | Con familia / Residencia / Arriendo / Solo |
| `nivel_socioeconomico` | Texto | Bajo / Medio-bajo / Medio / Medio-alto / Alto |
| `num_materias` | Entero | Materias cursadas este semestre (4–8) |
| `horas_trabajo_semanal` | Entero | 0 si no trabaja |
| `tiempo_desplazamiento` | Entero | Minutos/día ida y vuelta (5–150) |
| `extracurricular_hours` | Decimal | Horas semanales en actividades extracurriculares |
| `satisfaccion_carrera` | Decimal | Satisfacción con la carrera (1–10) |
| `calidad_suenio` | Entero | Calidad del sueño percibida (1–5) |
| `acceso_internet` | Texto | Excelente / Bueno / Regular / Malo |
| `participa_actividades` | Texto | Sí / No |
| `usa_servicios_sm` | Texto | Sí / No (servicios universitarios salud mental) |
| `promedio_previo` | Decimal | Promedio de calificaciones año anterior (4–10) |

---

### 3.3 Dataset Inicial — `student_mental_health_initial.csv`

El dataset inicial es la **unión (JOIN)** de los dos datasets anteriores usando `student_id` como clave común. Representa el punto de partida de todo el análisis.

| Atributo | Valor |
|---|---|
| **Operación** | `pd.merge(df_csv, df_db, on='student_id', how='inner')` |
| **Registros** | 5 000 (coincidencia total — mismo rango de IDs) |
| **Columnas** | 32 (15 del CSV + 17 del SQLite sin duplicar `student_id`) |
| **Nulos** | 0 |

---

### 3.4 Dataset Final — `student_mental_health_final.csv`

El dataset final incorpora todas las variables derivadas del preprocesamiento y los modelos de IA.

| Atributo | Valor |
|---|---|
| **Registros** | 5 000 |
| **Columnas** | 45 (32 originales + 13 derivadas) |

**Variables derivadas añadidas:**

| Variable | Descripción |
|---|---|
| `physical_activity_num` | Low=0, Moderate=1, High=2 |
| `academic_pressure_num` | Low=0, Moderate=1, High=2 |
| `family_support_num` | Low=0, Moderate=1, High=2 |
| `gender_num` | Female=0, Male=1 |
| `modalidad_num` | Virtual=0, Semipresencial=1, Presencial=2 |
| `acceso_internet_num` | Malo=0, Regular=1, Bueno=2, Excelente=3 |
| `nivel_socio_num` | Bajo=0 → Alto=4 |
| `participa_num` | No=0, Sí=1 |
| `usa_sm_num` | No=0, Sí=1 |
| `wellbeing_index` | Índice compuesto de bienestar (media=2.46) |
| `mental_health_issue` | Variable objetivo: 1 si depresión OR ansiedad (42.8%) |
| `mental_status` | 'Sin Problema' / 'Con Problema' |
| `cluster` | Perfil K-Means asignado (0–3) |

---

### 3.5 Estadísticas Descriptivas Clave

| Métrica | Valor |
|---|---|
| CGPA promedio | 3.75 |
| Tasa de depresión | 26.1% |
| Tasa de ansiedad | 31.2% |
| Estudiantes con ≥1 problema | 42.8% |
| Horas sueño promedio | 6.31 h |
| Wellbeing index media | 2.46 |
| Trabajan (part-time) | 32% |
| Usan servicios SM universidad | 22% |

---

## 4. Descripción de los Pasos Realizados en el Proyecto

### Paso 0: Configuración del Entorno

Instalación de librerías con pip y configuración de Jupyter Lab. Estructura del proyecto:

```
ai_project/
├── data/
│   ├── student_mental_health.csv         # Dataset CSV (5 000 × 15)
│   ├── student_context.db                # Base de datos SQLite (5 000 × 18)
│   ├── student_mental_health_initial.csv # Dataset inicial — JOIN (5 000 × 32)
│   ├── student_mental_health_final.csv   # Dataset final (5 000 × 45)
│   └── viz_0X_*.png                      # 5 visualizaciones Matplotlib
├── notebooks/
│   └── analisis_salud_mental_IA.ipynb    # Notebook principal (8 secciones)
└── sql/
    ├── create_database.sql               # Esquema SQL de la BD
    └── crear_base_datos.py               # Script generador del .db
```

### Paso 1: Carga de Datos (Sección 1 del notebook)

**1.1 — CSV:** `pd.read_csv()` carga `student_mental_health.csv` → 5 000 filas × 15 columnas, 0 nulos.

**1.2 — SQLite:** `sqlite3.connect()` + `pd.read_sql('SELECT * FROM student_context')` carga los datos complementarios → 5 000 filas × 18 columnas, 0 nulos.

**1.3 — Dataset inicial (JOIN):** `pd.merge(df_csv, df_db, on='student_id', how='inner')` combina ambas fuentes por la ID compartida → **5 000 filas × 32 columnas**. El resultado se guarda como `student_mental_health_initial.csv` — este es el dataset inicial del proyecto.

### Paso 2: Preprocesamiento (Sección 2)

1. **Codificación binaria:** Yes/No → 1/0 en `depression`, `anxiety`, `panic_attack`, `sought_treatment`.
2. **Codificación ordinal:** Low/Moderate/High → 0/1/2 en variables de actividad, presión y apoyo. También se codifican `modalidad`, `acceso_internet`, `nivel_socioeconomico`, `participa_actividades`, `usa_servicios_sm`.
3. **Índice de bienestar ampliado:** `wellbeing_index` combina 10 variables ponderadas: sueño (0.20), actividad física (0.15), apoyo familiar (0.15), satisfacción carrera (0.10), calidad sueño (0.10), horas extracurriculares (0.05), penalizando depresión, ansiedad, horas de trabajo y tiempo de desplazamiento.
4. **Variable objetivo:** `mental_health_issue` = 1 si `depression==1` OR `anxiety==1` → 42.8% afirmativo.

### Paso 3: Visualizaciones con Matplotlib (Sección 3)

Se generan 3 figuras multi-panel, 10 subgráficos totales.

### Paso 4: Visualizaciones con Bokeh (Sección 4)

Se generan 3 visualizaciones interactivas embebidas en el notebook.

### Paso 5: Exploración con PygWalker (Sección 5)

Dos exploradores drag-and-drop: uno sobre el dataset inicial completo (32 columnas) y otro sobre un resumen agregado por universidad y carrera.

### Paso 6: Modelos de IA (Sección 6)

**6.1 Clasificación:** 20 features, split 75/25 estratificado, `StandardScaler`, Random Forest (150 árboles) y Regresión Logística. Top 3 predictores: `extracurricular_hours`, `tiempo_desplazamiento`, `satisfaccion_carrera`.

**6.2 Clustering:** K-Means k=4 sobre 7 variables escaladas. 4 perfiles identificados:

| Perfil | CGPA | Sueño | Estudio | Trabajo | Bienestar | % con prob. mental |
|---|---|---|---|---|---|---|
| Perfil 1 | 3.71 | 5.93h | 4.33h | 20.16h | 2.02 | 50% |
| Perfil 2 | 3.88 | 7.24h | 2.79h | 3.26h | 2.77 | 28% |
| Perfil 3 | 3.83 | 6.44h | 5.00h | 1.36h | 2.70 | 37% |
| Perfil 4 | 3.54 | 5.33h | 4.73h | 0.69h | 2.20 | 61% |

### Paso 7: Exportación del Dataset Final (Sección 7)

Se exporta `student_mental_health_final.csv` con 5 000 registros y 45 columnas.

---

## 4.1 Descripción de las Visualizaciones Generadas

### Matplotlib — `viz_01_distribucion.png`
**Figura 1: Distribución General (cuadrícula 2×3)**

Seis subgráficos panorámicos. El histograma CGPA muestra concentración entre 3.5 y 4.0 con media 3.75. El pastel de género refleja distribución balanceada (50/50). Las barras horizontales de carreras muestran distribución uniforme entre los 10 programas. Las barras de salud mental exponen ansiedad (31.2%) superando a depresión (26.1%). El gráfico de nivel socioeconómico refleja predominancia del nivel Medio (38%). El scatter estudio-CGPA por modalidad muestra que la modalidad presencial concentra los CGPA más altos.

![Distribución General](https://raw.githubusercontent.com/lmegas1/TrabajoFinal1/main/data/viz_01_distribucion.png)

### Matplotlib — `viz_02_correlacion.png`
**Figura 2: Correlación y Box Plot (1×2)**

El mapa de calor de 14 variables numéricas revela: `satisfaccion_carrera` como predictor positivo del CGPA; `academic_pressure_num` y `social_media_hours` como predictores negativos; `family_support_num` con efecto protector sobre depresión y ansiedad. El box plot confirma CGPA mediano superior en estudiantes sin problema (≈3.8 vs ≈3.6).

![Distribución General](https://raw.githubusercontent.com/lmegas1/TrabajoFinal1/main/data/viz_02_correlacion.png)

### Matplotlib — `viz_03_carrera_contexto.png`
**Figura 3: Carrera y Contexto (2×2)**

CGPA con barras de error por carrera (Medicina y Enfermería lideran); tasa de problema mental por nivel socioeconómico (mayor prevalencia en niveles Bajo y Medio-bajo); scatter horas de trabajo vs CGPA (los estudiantes que trabajan más de 20h/semana tienen menor CGPA y más problemas de salud mental); satisfacción por financiamiento (Beca completa muestra mayor satisfacción).

![Distribución General](https://raw.githubusercontent.com/lmegas1/TrabajoFinal1/main/data/viz_03_carrera_contexto.png)

### Matplotlib — `viz_04_modelos.png`
**Figura 4: Modelos de IA (1×3)**

Importancia de 20 variables (top 3: horas extracurriculares, tiempo desplazamiento, satisfacción carrera), y matrices de confusión de Random Forest (Blues, Acc=65.6%) y Regresión Logística (Oranges, Acc=65.1%) sobre 1 250 estudiantes del conjunto de prueba.

![Distribución General](https://raw.githubusercontent.com/lmegas1/TrabajoFinal1/main/data/viz_04_modelos.png)

### Matplotlib — `viz_05_clustering.png`
**Figura 5: Clustering K-Means (1×2)**

Método del codo (k=2 a k=8) con quiebre visible en k=4, y scatter CGPA vs wellbeing_index con 4 colores (azul, verde, naranja, rosado) representando los 4 perfiles sobre 5 000 puntos. El Perfil 4 (menor bienestar, 61% problema mental) se separa claramente del Perfil 2 (mayor bienestar, 28%).

![Distribución General](https://raw.githubusercontent.com/lmegas1/TrabajoFinal1/main/data/viz_05_clustering.png)

---

## 5. Conclusiones

### 5.1 Sobre los Datos

1. **La integración de dos datasets amplía el poder analítico:** El JOIN entre el CSV (salud mental) y el SQLite (contexto socioeconómico) reveló relaciones que ninguna fuente por separado podría mostrar; es decir, los estudiantes de nivel socioeconómico bajo con alta carga laboral tienen el doble de riesgo de problema de salud mental que estudiantes de nivel alto.

2. **Alta prevalencia confirmada:** El 42.8% de los 5 000 estudiantes presenta al menos depresión o ansiedad, evidenciando una crisis de salud mental en el ámbito universitario ecuatoriano.

3. **El contexto importa tanto como los hábitos:** Las variables del SQLite (horas de trabajo, tiempo de desplazamiento, satisfacción con la carrera) resultaron ser los tres predictores más importantes del Random Forest, superando a variables clásicas como el CGPA o las horas de sueño.

4. **Perfil de mayor riesgo identificado:** El Perfil 4 del clustering (poco sueño, alta carga de trabajo y bajo bienestar) concentra un 61% de incidencia de problema de salud mental. Intervenir en este perfil tendría el mayor impacto significativo para el bienestar estudiantil.

5. **Brecha crítica en uso de servicios:** Solo el 22% de los estudiantes usa los servicios de salud mental universitarios, pese a que el 42.8% tiene indicadores de problema. Esta brecha del 20% representa miles de estudiantes sin atención.

6. **El financiamiento influye en el bienestar:** Los becados completos muestran mayor satisfacción con su carrera y mejores indicadores de bienestar, sugiriendo que reducir la presión económica es también una intervención de salud mental.

### 5.2 Sobre las Herramientas

7. **El JOIN con Pandas es la operación clave:** `pd.merge(on='student_id')` en una sola línea integra 32 columnas de dos fuentes heterogéneas sin pérdida de datos, demostrando el poder de compartir una ID entre datasets de distinto formato.

8. **Matplotlib y Bokeh cumplen roles distintos:** Matplotlib para figuras exportables de alta calidad (informes, publicaciones); Bokeh para exploración interactiva donde el usuario necesita filtrar y hacer zoom en tiempo real.

9. **PygWalker democratiza el análisis:** Permite a colaboradores sin conocimiento de Python explorar el dataset de 32 columnas visualmente, acelerando el descubrimiento de hipótesis.

10. **20 features mejoran la clasificación:** Al incluir variables del SQLite en los modelos (nivel socioeconómico, horas de trabajo, satisfacción), la accuracy subió respecto a modelos con solo las variables del CSV, validando el valor principal del JOIN.

---

## 6. Bibliografía

1. **McKinney, W.** (2010). *Data Structures for Statistical Computing in Python*. Proceedings SciPy 2010. https://pandas.pydata.org

2. **Hunter, J. D.** (2007). *Matplotlib: A 2D Graphics Environment*. Computing in Science & Engineering, 9(3), 90–95. https://doi.org/10.1109/MCSE.2007.55

3. **Bokeh Development Team** (2024). *Bokeh: Python library for interactive visualization*. https://bokeh.org

4. **Kanaries Team** (2023). *PyGWalker: Turn your pandas dataframe into a Tableau-style UI*. https://github.com/Kanaries/pygwalker

5. **Pedregosa, F., et al.** (2011). *Scikit-learn: Machine Learning in Python*. JMLR, 12, 2825–2830. https://scikit-learn.org

6. **SQLite Consortium** (2024). *SQLite Documentation*. https://sqlite.org

7. **Project Jupyter** (2024). *JupyterLab Documentation*. https://jupyterlab.readthedocs.io

8. **World Health Organization** (2022). *Mental health of adolescents*. https://www.who.int/news-room/fact-sheets/detail/adolescent-mental-health

9. **Eisenberg, D., Hunt, J., & Speer, N.** (2013). *Mental health in American colleges and universities*. Journal of Nervous and Mental Disease, 201(1), 60–67.

10. **Rotenstein, L. S., et al.** (2016). *Prevalence of Depression among Medical Students*. JAMA, 316(21), 2214–2236.

11. **Breiman, L.** (2001). *Random Forests*. Machine Learning, 45(1), 5–32.

12. **MacQueen, J.** (1967). *Some methods for classification and analysis of multivariate observations*. Proceedings 5th Berkeley Symposium, 1, 281–297.

13. **VanderPlas, J.** (2016). *Python Data Science Handbook*. O'Reilly. https://jakevdp.github.io/PythonDataScienceHandbook/

14. **Géron, A.** (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly.