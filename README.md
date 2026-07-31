# GCS semana 3, actividad 4, tienda en línea

Este repositorio contiene el paquete mínimo, auditable y trazable de gestión de la configuración de software para un mini sistema de comercio electrónico. El caso cubre el flujo completo del negocio, desde que un cliente se registra hasta que explora el catálogo, arma un carrito, genera un pedido y el equipo revisa reportes de ventas.

## Estructura del repositorio

- docs/SRS contiene la especificación de requisitos del sistema.
- docs/Quality contiene el modelo de calidad y las métricas verificables asociadas.
- docs/Lifecycle contiene el análisis de impacto de un cambio a lo largo del ciclo de vida.
- src contiene el código fuente mínimo del catálogo, el carrito y los pedidos.
- tests contiene las pruebas unitarias de cada módulo.
- config contiene un archivo de configuración de ejemplo, sin datos sensibles reales.
- CM_PLAN.md define los elementos de configuración, las reglas de versión y el procedimiento de línea base.
- CHANGELOG.md registra el historial de cambios relevantes del proyecto.

## Cómo ejecutar las pruebas

Desde la raíz del repositorio, con Python 3.12 instalado, ejecuta el siguiente comando.

```bash
python -m unittest discover -s tests
```

## Documentos relacionados

- Plan de gestión de configuración, ver CM_PLAN.md
- Especificación de requisitos, ver docs/SRS/SRS_v1.md
- Modelo de calidad, ver docs/Quality/Quality_Model.md
- Análisis de impacto en el ciclo de vida, ver docs/Lifecycle/Lifecycle_Impact.md
