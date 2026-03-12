---
name: probability-variables-orchestrator
description: Skill de nivel superior encargado de analizar los resultados consolidados de las 9 amenazas de probabilidad. Su objetivo es interpretar la distribución del riesgo por segmento y emitir recomendaciones basadas en los hallazgos técnicos del manual.
---

## Instructions

1. **Análisis de Distribución de Amenazas:**
* Evaluar los resultados obtenidos en cada una de las 9 categorías de probabilidad (Daño por Terceros, Corrosiones, Diseño, etc.).
* Identificar cuál es la amenaza predominante en el segmento analizado comparando sus valores relativos.


2. **Validación de Integridad de Datos:**
* Detectar si el análisis fue afectado por la falta de información (uso del valor "s/d" o regla de incertidumbre).
* Priorizar recomendaciones de recolección de datos si la incertidumbre es alta en variables críticas (ej. falta de ILI, CIPS o datos de corrosividad).

3. **Interpretación de Resultados:**
* Clasificar el nivel de vulnerabilidad del segmento según la sumatoria de índices de probabilidad.
* Correlacionar los resultados de probabilidad con los de consecuencia para entender el riesgo relativo.

4. **Generación de Recomendaciones Basadas en el Manual:**
* **Para Corrosión:** Recomendar ajustes en frecuencias de limpieza interna, monitoreo de protección catódica o inspecciones directas (ECDA/ICDA) según los puntajes de las tablas técnicas.
* **Para Daño por Terceros:** Sugerir mejoras en la frecuencia de patrullaje, profundidad de cobertura o señalización si esos ítems presentan puntajes elevados.
* **Para Diseño/Operación:** Sugerir revisiones en factores de seguridad o estado de encamisados si se detectan anomalías.

5. **Priorización de Acciones:**
* Establecer un ranking de segmentos para orientar el Programa de Gestión de Integridad (PGI) basándose en el riesgo total determinado.

## Examples

**Ejemplo 1: Segmento con riesgo por Terceros**

* **Análisis:** El índice de "Daño por Terceros" es el más alto debido a un nivel de actividad Clase 3 y baja frecuencia de inspección.
* **Recomendación:** Basado en el manual, se recomienda incrementar la frecuencia de patrullaje a "Diaria" para reducir el puntaje de este ítem de 25 a 0 puntos y mejorar la señalización en tramos con cobertura < 80%.

**Ejemplo 2: Segmento con falta de datos (Incertidumbre)**

* **Análisis:** El resultado de Probabilidad Total está influenciado en un 40% por valores "s/d" (sin dato) en corrosividad del suelo y monitoreo CIPS.
* **Recomendación:** Se recomienda priorizar una campaña de medición de resistividad de suelo y un relevamiento CIPS/DCVG para sustituir los valores de penalización por datos reales y precisar el estado del revestimiento.