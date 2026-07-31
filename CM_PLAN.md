# Plan de gestión de configuración

## Propósito

Este documento identifica los elementos de configuración del sistema de comercio electrónico, define cómo se versionan, cómo se aprueban las líneas base y quién es responsable de cada artefacto. Su objetivo es que cualquier persona del equipo, o un auditor externo, pueda reconstruir el estado del sistema en cualquier momento y entender por qué cambió.

## Alcance del sistema

El caso trabajado es una tienda en línea con un flujo claro de tres etapas. En el registro, el cliente crea su cuenta. En la operación, el cliente explora el catálogo, arma un carrito y genera un pedido, mientras el sistema valida existencias y descuenta inventario. En el reporte, el equipo revisa el historial de pedidos y el estado del inventario. Ese flujo es el que da origen a los elementos de configuración listados abajo.

## Elementos de configuración

| EC | Ubicación | Por qué es EC | Quién lo modifica |
| --- | --- | --- | --- |
| SRS_v1.md | docs/SRS/ | Define los requisitos funcionales y no funcionales del sistema, un cambio aquí modifica el alcance y las pruebas de aceptación | Analista de requisitos |
| Quality_Model.md | docs/Quality/ | Traduce los atributos de calidad en métricas verificables que guían las pruebas y la aceptación del producto | Responsable de calidad |
| Lifecycle_Impact.md | docs/Lifecycle/ | Documenta el impacto de un cambio en cada fase del ciclo de vida y sirve de referencia para el control de cambios | Analista de requisitos |
| catalog.py | src/ | Contiene la lógica del catálogo de productos, un cambio aquí afecta directamente la búsqueda y la disponibilidad de productos | Desarrollador |
| cart.py | src/ | Contiene la lógica del carrito de compras, es un componente crítico del flujo de compra | Desarrollador |
| orders.py | src/ | Contiene la lógica de creación de pedidos, conecta el catálogo, el carrito y la trazabilidad hacia los requisitos | Desarrollador |
| tests | tests/ | Valida el comportamiento esperado de cada módulo y permite detectar regresiones antes de liberar una versión | QA y desarrollador |
| config.example.json | config/ | Parametriza variables de ejecución del sistema, como moneda o tiempos de expiración del carrito, y afecta el comportamiento en distintos entornos | DevOps y desarrollador |
| CM_PLAN.md | / | Define las reglas de versión, línea base y responsables, es la referencia para auditar el resto de los elementos de configuración | Gestor de configuración |
| CHANGELOG.md | / | Registra el historial de cambios relevantes de cada línea base y da trazabilidad de versiones en el tiempo | Todo el equipo, revisado por el gestor de configuración |

## Reglas de versionado

Los mensajes de commit siguen un prefijo que indica el tipo de cambio: docs para documentación, feat para funcionalidad nueva, test para pruebas, fix para corrección de errores y chore para tareas de mantenimiento como configuración o dependencias. El historial debe leerse como una narrativa del trabajo realizado, por lo que cada commit agrupa un cambio coherente y no mezcla propósitos distintos.

Las líneas base se identifican con un tag semántico, por ejemplo v1.0, y representan una versión aprobada del conjunto de elementos de configuración. Un elemento de configuración solo puede cambiar después de la línea base si el cambio queda registrado en el CHANGELOG y, cuando aplica, referencia el requisito que lo origina.

## Procedimiento de línea base

Antes de crear una línea base, el gestor de configuración revisa que todos los elementos de configuración estén completos y que las pruebas asociadas pasen. Con esa revisión hecha, se crea un tag anotado sobre el commit correspondiente y se publica en el repositorio remoto. A partir de ese punto, cualquier cambio posterior a un elemento ya congelado se trata como una nueva iteración controlada, con su propio commit y su propia justificación.

```bash
git tag -a v1.0 -m "Baseline v1.0, EC mas modelo de calidad y analisis de ciclo de vida"
git push origin v1.0
```

## Roles y responsabilidades

| Rol | Responsabilidad |
| --- | --- |
| Analista de requisitos | Mantiene actualizado el SRS y evalúa el impacto de un cambio en el alcance |
| Desarrollador | Implementa el código y actualiza las pruebas cuando cambia el comportamiento del sistema |
| Responsable de calidad | Define y revisa las métricas de calidad y verifica que se cumplan antes de una línea base |
| DevOps | Mantiene la configuración de ejecución y evita que datos sensibles queden expuestos |
| Gestor de configuración | Aprueba las líneas base, verifica que los EC estén completos y audita el historial de cambios |
