# Control-de-Indicadores-de-Planta---Tintorer-a-de-Hilos
Este proyecto contiene la estructura inicial del backend para el sistema de indicadores de Tintorería de Hilos.

El objetivo es registrar mediciones físicas por lote, máquina y huso, permitiendo calcular indicadores como densidad de bobinas, dureza, promedio por lote, variabilidad y estado del proceso.

La lógica está organizada en módulos para separar responsabilidades:

- models: estructura de datos.
- core: reglas de cálculo, fórmulas físicas, máquinas, calidad y SPC.
- api: funciones o endpoints para registrar mediciones y cerrar lotes.
- services: conexión futura a base de datos.
- utils: funciones auxiliares.

Este backend servirá como base para conectar formularios del frontend, dashboards operativos y validaciones de planta.
