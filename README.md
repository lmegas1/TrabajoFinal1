# 🧠 Análisis de Salud Mental Estudiantil con IA

> Trabajo Final: Aplicación de IA con librerías de software libre.

## Estructura del Repositorio

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

## Arquitectura del Dataset

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

## Tecnologías

| Librería | Uso |
|---|---|
| **Pandas** | Carga CSV, lectura SQLite, JOIN por student_id |
| **Matplotlib + Seaborn** | 5 figuras multi-panel estáticas |
| **Bokeh** | 3 visualizaciones interactivas |
| **PygWalker** | Exploración drag-and-drop |
| **Scikit-learn** | Random Forest, Reg. Logística, K-Means |
| **SQLite** | Base de datos relacional embebida |

## Wiki

Consultar el Wiki para el informe completo (introducción, marco teórico, descripción de datasets, pasos, visualizaciones, conclusiones y bibliografía).
