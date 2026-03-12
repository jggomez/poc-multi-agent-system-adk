---

name: evaluate-internal-inspection-tool-ili
description: Analiza la confiabilidad y los hallazgos de las herramientas de inspección en línea (ILI) para determinar la precisión del estado del ducto y emitir recomendaciones de integridad basadas en la calidad de los datos recopilados.

---

## Instructions

1. **Evaluación de la Tecnología Utilizada:**
* Identificar el tipo de herramienta empleada (MFL - Pérdida de Flujo Magnético, UT - Ultrasonido, TFI, etc.).
* Determinar si la tecnología es la adecuada para las amenazas identificadas en el segmento (ej: MFL para corrosión general, UT para fisuras o medición de espesores precisa).


2. **Análisis de Calidad de Datos y Antigüedad:**
* Verificar la fecha de la última inspección. Según el manual, la vigencia de los datos degrada la confianza en el índice.
* Evaluar si hubo pasajes fallidos, pérdida de datos por velocidad excesiva del pig o sensores dañados. Si los datos son mediocres o nulos, aplicar la **Regla del 70%** sobre el factor de incertidumbre de inspección.


3. **Interpretación de Hallazgos Críticos:**
* Analizar la densidad de anomalías reportadas por kilómetro.
* Correlacionar los resultados de la ILI con las mediciones de campo (excavaciones de validación/verificación) para determinar el Factor de Error del reporte.


4. **Generación de Recomendaciones Basadas en el Manual:**
* **Si el reporte detecta anomalías severas (FER > límite permitido):** Recomendar reparaciones inmediatas mediante camisas de refuerzo o reemplazo de tramos.
* **Si los datos son antiguos (> 5 años):** Sugerir la programación de una nueva corrida de ILI en el Plan de Gestión de Integridad (PGI).
* **Si hay discrepancia entre ILI y campo:** Recomendar un re-post-procesamiento de los datos crudos por parte del proveedor del servicio.


5. **Priorización:**
* Utilizar los resultados de la ILI para recategorizar la probabilidad de falla de los segmentos, moviendo a "Alta Prioridad" aquellos con indicaciones de corrosión activa o pérdida de metal progresiva.



## Examples

**Ejemplo 1: Inspección ILI con hallazgos de corrosión**

* **Análisis:** La herramienta MFL de alta resolución detectó una pérdida de metal del 45% en la posición horaria 6:00 en un tramo Clase 3.
* **Recomendación:** Basado en el manual de riesgo, se recomienda realizar una excavación de verificación en un plazo no mayor a 90 días para validar la profundidad de la anomalía y aplicar una camisa de material compuesto si se confirma la dimensión.

**Ejemplo 2: Incertidumbre por inspección obsoleta**

* **Análisis:** El último registro de inspección interna data de hace 8 años.
* **Recomendación:** El nivel de incertidumbre es inaceptable para la gestión de integridad actual (se aplica penalización del 70% en el factor de confianza). Se recomienda incluir de forma mandatoria la corrida de un Intelligent Pig (MFL + Geometría) en el presupuesto del próximo ejercicio operativo para actualizar el estado real de la pared del ducto.