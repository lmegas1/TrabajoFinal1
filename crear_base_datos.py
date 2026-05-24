"""
Script: crear_base_datos.py
Descripción: Genera la base de datos SQLite student_context.db con 5000 registros.
             Comparte student_id con student_mental_health.csv (STU0001-STU5000)
             para permitir JOIN entre ambos datasets.
Proyecto: Análisis de Salud Mental Estudiantil con IA
"""

import sqlite3
import numpy as np
import os

np.random.seed(99)

DB_PATH  = 'data/student_context.db'
SQL_PATH = 'create_database.sql'
N        = 5000

def crear_base_datos():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print(f"Base de datos anterior eliminada.")

    with open(SQL_PATH, 'r', encoding='utf-8') as f:
        sql_schema = f.read()

    # ── Generar datos ──────────────────────────────────────────
    student_ids = [f'STU{str(i).zfill(4)}' for i in range(1, N+1)]

    universidades = [
        'Universidad Técnica de Cotopaxi','Escuela Politécnica Nacional',
        'Universidad Central del Ecuador','Pontificia Universidad Católica del Ecuador',
        'Universidad San Francisco de Quito','Universidad de las Fuerzas Armadas',
        'Universidad Técnica de Ambato','Universidad de Cuenca',
        'Universidad Nacional de Loja','Universidad Técnica del Norte'
    ]
    carreras = [
        'Ingeniería en Sistemas','Medicina','Derecho','Psicología',
        'Administración de Empresas','Arquitectura','Enfermería',
        'Ingeniería Civil','Comunicación Social','Contabilidad'
    ]

    universidad   = np.random.choice(universidades, N).tolist()
    carrera       = np.random.choice(carreras, N).tolist()
    modalidad     = np.random.choice(['Presencial','Semipresencial','Virtual'],
                        N, p=[0.65,0.22,0.13]).tolist()
    financiamiento= np.random.choice(
                        ['Beca completa','Beca parcial','Recursos propios','Crédito educativo'],
                        N, p=[0.18,0.24,0.38,0.20]).tolist()
    residencia    = np.random.choice(
                        ['Con familia','Residencia universitaria','Arriendo compartido','Solo'],
                        N, p=[0.42,0.12,0.33,0.13]).tolist()
    nivel_socio   = np.random.choice(
                        ['Bajo','Medio-bajo','Medio','Medio-alto','Alto'],
                        N, p=[0.12,0.23,0.38,0.20,0.07]).tolist()
    acceso_int    = np.random.choice(['Excelente','Bueno','Regular','Malo'],
                        N, p=[0.35,0.38,0.20,0.07]).tolist()
    participa     = np.random.choice(['Sí','No'], N, p=[0.44,0.56]).tolist()
    usa_sm        = np.random.choice(['Sí','No'], N, p=[0.22,0.78]).tolist()

    # IMPORTANTE: usar int() explícito para evitar numpy int → BLOB en SQLite
    semestre      = [int(x) for x in np.random.choice([1,2,3,4,5,6,7,8], N,
                        p=[0.14,0.14,0.14,0.13,0.13,0.12,0.11,0.09])]
    num_materias  = [int(x) for x in np.random.choice(range(4,9), N,
                        p=[0.10,0.28,0.35,0.20,0.07])]
    trabaja       = np.random.choice([0,1], N, p=[0.68,0.32])
    horas_trabajo = [int(x) for x in np.where(
                        trabaja==1,
                        np.clip(np.round(np.random.normal(18,6,N)).astype(int), 4, 40),
                        0)]
    tiempo_despl  = [int(x) for x in np.clip(
                        np.round(np.random.normal(45,25,N)).astype(int), 5, 150)]
    calidad_sue   = [int(x) for x in np.clip(
                        np.round(np.random.normal(3.1,1.0,N)).astype(int), 1, 5)]

    # float() explícito para decimales
    extracurr     = [float(round(x,1)) for x in
                        np.clip(np.round(np.random.normal(3.5,1.8,N),1), 0, 10)]
    satisfaccion  = [float(round(x,1)) for x in
                        np.clip(np.round(np.random.normal(6.8,1.9,N),1), 1, 10)]
    prom_previo   = [float(round(x,1)) for x in
                        np.clip(np.round(np.random.normal(7.8,1.5,N),1), 4.0, 10.0)]

    rows = list(zip(
        student_ids, universidad, carrera,
        semestre, modalidad, financiamiento, residencia, nivel_socio,
        num_materias, horas_trabajo, tiempo_despl,
        extracurr, satisfaccion, calidad_sue,
        acceso_int, participa, usa_sm, prom_previo
    ))

    # ── Crear DB ───────────────────────────────────────────────
    conn   = sqlite3.connect(DB_PATH)
    conn.executescript(sql_schema)
    conn.executemany(
        "INSERT INTO student_context VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        rows
    )
    conn.commit()

    # ── Verificar tipos ────────────────────────────────────────
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM student_context")
    total = cur.fetchone()[0]

    cur.execute("""SELECT semestre, num_materias, horas_trabajo_semanal,
                          tiempo_desplazamiento, calidad_suenio
                   FROM student_context LIMIT 1""")
    muestra = cur.fetchone()
    tipos_ok = all(isinstance(v, int) for v in muestra)
    conn.close()

    print(f"\n✅ Base de datos creada exitosamente.")
    print(f"   Tabla: student_context — {total} registros")
    print(f"   IDs:   STU0001 – STU{N:04d}")
    print(f"   Tipos enteros OK: {'✅' if tipos_ok else '❌ REVISAR'}")
    print(f"   Archivo: {os.path.abspath(DB_PATH)}")


if __name__ == "__main__":
    crear_base_datos()
