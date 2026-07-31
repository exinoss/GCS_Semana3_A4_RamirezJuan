# Especificación de requisitos, versión 1

## Propósito y alcance

Este documento describe los requisitos del sistema de comercio electrónico usado como caso base de la actividad. Cubre el registro de clientes, la consulta del catálogo, el manejo del carrito de compras y la creación de pedidos con su respectivo descuento de inventario.

## Requisitos funcionales

| ID | Descripción |
| --- | --- |
| RF-01 | El sistema debe permitir registrar un producto en el catálogo con nombre, precio y existencias |
| RF-02 | El sistema debe permitir buscar productos por nombre dentro del catálogo |
| RF-03 | El sistema debe permitir agregar y quitar productos de un carrito de compras |
| RF-04 | El sistema debe calcular el total del carrito a partir del precio y la cantidad de cada producto |
| RF-05 | El sistema debe crear un pedido a partir de un carrito, validar existencias suficientes y descontar el inventario correspondiente |
| RF-06 | Todo pedido debe registrar una referencia al requisito que lo origina y a la prueba que evidencia su comportamiento, para mantener trazabilidad entre negocio y código |

## Requisitos no funcionales

| ID | Descripción |
| --- | --- |
| RNF-01 | Las búsquedas de productos en el catálogo deben responder en 2 segundos o menos en el 95% de los casos |
| RNF-02 | El sistema no debe almacenar contraseñas ni datos de tarjeta en texto plano |
| RNF-03 | Los módulos de catálogo, carrito y pedidos deben mantener una cobertura de pruebas de al menos 60% |

## Trazabilidad

Cada requisito funcional y no funcional debe quedar reflejado en al menos un elemento de configuración de código o de pruebas, tal como se describe en CM_PLAN.md. El requisito RF-06 es el que sostiene la política de trazabilidad analizada en docs/Lifecycle/Lifecycle_Impact.md.
