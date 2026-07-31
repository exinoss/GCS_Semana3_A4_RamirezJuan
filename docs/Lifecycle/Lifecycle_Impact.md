# Análisis de impacto en el ciclo de vida

## Cambio simulado

El cambio elegido es de trazabilidad, tal como quedó definido en RF-06 dentro de docs/SRS/SRS_v1.md. La regla dice que todo pedido debe registrar una referencia al requisito que lo origina y a la prueba que evidencia su comportamiento. Sin esta regla, un cambio en el código puede quedar sin relación documentada con el requisito de negocio que lo justificó, lo que dificulta auditar por qué existe cada parte del sistema.

## Impacto por fase

| Fase | Qué cambia | EC afectados | Riesgo si no se controla | Evidencia de validación |
| --- | --- | --- | --- | --- |
| Requisitos | Se agrega RF-06, que exige que cada pedido referencie el requisito de origen y su evidencia de prueba | docs/SRS/SRS_v1.md | El equipo implementa cambios sin justificación documentada y se pierde la relación entre negocio y código | Revisión del RF-06 por el analista de requisitos y su registro en CM_PLAN.md |
| Diseño | Se define que el pedido debe incluir un campo requirement_ref junto con sus datos actuales | docs/SRS/SRS_v1.md, CM_PLAN.md | Si el diseño no contempla el campo, la trazabilidad queda incompleta y no se puede auditar más adelante | Revisión de diseño que confirma el campo antes de tocar orders.py |
| Implementación | Se agrega el campo requirement_ref a la clase Order y se exige como parámetro obligatorio al crear un pedido | src/orders.py | Un pedido sin referencia impide saber qué requisito lo originó, lo que aumenta el costo de futuras auditorías | Commit posterior a la línea base v1.0 que agrega el campo y referencia RF-06 |
| Pruebas | Se agrega una prueba que confirma que un pedido queda creado con su requirement_ref y otra que rechaza un pedido sin ese dato | tests/test_orders.py | Sin la prueba, el campo podría quedar vacío en producción sin que nadie lo detecte a tiempo | Ejecución de test_orders.py mostrando los casos nuevos en verde |
| Despliegue y mantenimiento | El CHANGELOG registra el cambio con referencia al requisito RF-06 y al commit que agrega la prueba correspondiente | CHANGELOG.md | Sin este registro se pierde el historial de por qué se hizo el cambio, lo que encarece el mantenimiento futuro | Entrada en CHANGELOG.md posterior a la línea base v1.0 |

## Evidencia del cambio aplicado

Este análisis se documenta antes de crear la línea base v1.0. La implementación real de RF-06 se aplica después de esa línea base, mediante un commit propio que modifica src/orders.py y tests/test_orders.py. La captura de evidencia debe mostrar ese commit en el historial de Git, ubicado después del tag v1.0, junto con el mensaje que referencia RF-06.
