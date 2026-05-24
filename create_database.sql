-- ============================================================
-- Base de Datos: Contexto Socioeconómico y Universitario
-- Proyecto: Análisis de Salud Mental Estudiantil con IA
-- Registros: 5000
-- ID compartida: student_id (STU0001 – STU5000)
-- Relación: JOIN con student_mental_health.csv por student_id
-- ============================================================

CREATE TABLE IF NOT EXISTS student_context (
    student_id               TEXT    PRIMARY KEY,
    universidad              TEXT    NOT NULL,
    carrera                  TEXT    NOT NULL,
    semestre                 INTEGER NOT NULL,
    modalidad                TEXT    NOT NULL,   -- Presencial / Semipresencial / Virtual
    financiamiento           TEXT    NOT NULL,   -- Beca completa / parcial / Recursos propios / Crédito
    residencia               TEXT    NOT NULL,   -- Con familia / Residencia / Arriendo / Solo
    nivel_socioeconomico     TEXT    NOT NULL,   -- Bajo / Medio-bajo / Medio / Medio-alto / Alto
    num_materias             INTEGER NOT NULL,   -- Materias cursadas este semestre (4-8)
    horas_trabajo_semanal    INTEGER NOT NULL,   -- 0 si no trabaja
    tiempo_desplazamiento    INTEGER NOT NULL,   -- Minutos/día ida y vuelta
    extracurricular_hours    REAL    NOT NULL,   -- Horas semanales actividades extracurriculares
    satisfaccion_carrera     REAL    NOT NULL,   -- Escala 1-10
    calidad_suenio           INTEGER NOT NULL,   -- Escala 1-5
    acceso_internet          TEXT    NOT NULL,   -- Excelente / Bueno / Regular / Malo
    participa_actividades    TEXT    NOT NULL,   -- Sí / No
    usa_servicios_sm         TEXT    NOT NULL,   -- Sí / No (servicios salud mental universidad)
    promedio_previo          REAL    NOT NULL    -- Promedio calificaciones año anterior (4-10)
);
