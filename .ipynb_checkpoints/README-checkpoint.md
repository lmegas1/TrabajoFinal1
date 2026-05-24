# 🧠 Análisis de Salud Mental Estudiantil con IA

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Lab-orange?logo=jupyter)](https://jupyter.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

> Proyecto Final Académico — Aplicación de IA con librerías de software libre.

## 📁 Estructura del Repositorio

```
├── data/
│   ├── student_mental_health.csv         # Dataset CSV — Salud mental (5 000 × 15)
│   ├── student_context.db                # Base de datos SQLite — Contexto (5 000 × 18)
│   ├── student_mental_health_initial.csv # Dataset inicial — JOIN de ambas fuentes (5 000 × 32)
│   └── student_mental_health_final.csv   # Dataset final enriquecido (5 000 × 45)
├── notebooks/
│   └── analisis_salud_mental_IA.ipynb    # Notebook principal
├── sql/
│   ├── create_database.sql               # Esquema SQL
│   └── crear_base_datos.py               # Generador de la BD
├── WIKI.md                               # Informe completo
└── README.md
```

## 🔑 Arquitectura del Dataset

Ambos datasets comparten `student_id` (STU0001–STU5000) para permitir el JOIN:

```
student_mental_health.csv   +   student_context.db
     (5 000 × 15)                  (5 000 × 18)
          │                              │
          └──── JOIN on student_id ──────┘
                        │
          student_mental_health_initial.csv
                  (5 000 × 32)
```

## 🚀 Cómo Ejecutar

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/ai-salud-mental.git
cd ai-salud-mental

# 2. Instalar dependencias
pip install pandas numpy matplotlib seaborn bokeh pygwalker scikit-learn jupyter

# 3. (Opcional) Regenerar la base de datos SQLite
cd sql && python crear_base_datos.py && cd ..

# 4. Abrir Jupyter Lab
jupyter lab notebooks/analisis_salud_mental_IA.ipynb
```

## 📊 Tecnologías

| Librería | Uso |
|---|---|
| **Pandas** | Carga CSV, lectura SQLite, JOIN por student_id |
| **Matplotlib + Seaborn** | 5 figuras multi-panel estáticas |
| **Bokeh** | 3 visualizaciones interactivas |
| **PygWalker** | Exploración drag-and-drop |
| **Scikit-learn** | Random Forest, Reg. Logística, K-Means |
| **SQLite** | Base de datos relacional embebida |

## 📖 Wiki

Consulta [WIKI.md](WIKI.md) para el informe completo (introducción, marco teórico, descripción de datasets, pasos, visualizaciones, conclusiones y bibliografía).
