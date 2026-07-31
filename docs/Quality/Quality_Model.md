# Modelo de calidad

Este documento traduce seis atributos del modelo ISO IEC 25010 en métricas verificables para el sistema de comercio electrónico. Cada métrica se redacta de forma que se pueda comprobar con una medición concreta, no como una intención general.

| Atributo | Definición | Métrica verificable | EC que lo soporta |
| --- | --- | --- | --- |
| Eficiencia de desempeño | Capacidad del sistema de usar los recursos de forma adecuada bajo condiciones normales de uso | Las búsquedas de productos en el catálogo deben responder en 2 segundos o menos en el 95% de los casos, según RNF-01 | src/catalog.py, tests/test_catalog.py |
| Seguridad | Protección de la información y de los datos de pago frente a acceso no autorizado | El sistema no debe almacenar contraseñas ni datos de tarjeta en texto plano, verificado con 0 ocurrencias durante la revisión de código y de config.example.json | src/orders.py, config/config.example.json |
| Fiabilidad | Capacidad del sistema de mantener su nivel de desempeño bajo condiciones específicas | El proceso de creación de pedidos debe completarse sin errores en el 100% de las ejecuciones de las pruebas definidas en test_orders.py | src/orders.py, tests/test_orders.py |
| Mantenibilidad | Facilidad para modificar el sistema sin introducir defectos ni afectar otras partes | Los módulos de catálogo, carrito y pedidos deben mantener una cobertura de pruebas de al menos 60%, según RNF-03 | src/, tests/ |
| Usabilidad | Facilidad con la que un usuario logra completar sus tareas de forma efectiva | Un cliente nuevo debe poder agregar un producto al carrito y generar un pedido en menos de 5 pasos, sin ayuda externa | docs/SRS/SRS_v1.md |
| Compatibilidad | Capacidad del sistema de intercambiar información con otros componentes o entornos | El sistema debe operar con los parámetros definidos en config.example.json sin requerir cambios en el código del cliente | config/config.example.json |

## Métricas estrella

Para este caso, las dos métricas más importantes son la de eficiencia de desempeño y la de seguridad. La primera importa porque una búsqueda lenta en el catálogo es el punto donde más clientes abandonan una compra antes de llegar al carrito. La segunda importa porque el sistema maneja datos de pago, y cualquier dato sensible almacenado en texto plano representa un riesgo directo para el cliente y para el negocio, más allá de si el resto del sistema funciona bien.
