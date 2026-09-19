# GuateShop - Taller de Patrones Estructurales (Python 3.10+)

Implementación completa de los 5 patrones de diseño estructurales (Adapter, Facade,
Decorator, Composite, Proxy) aplicados al caso GuateShop.

## Reparto

| Integrante | Carpeta(s) | Responsabilidad | Estado |
|---|---|---|---|
| Jordin García | `p1_adapter/`, `p5_proxy/` | Adapter y Proxy (con pruebas de lazy loading) | ✅ Implementado |
| Pablo Zúñiga | `p2_facade/` | Facade y sus cuatro subsistemas | ✅ Implementado |
| Emilio Méndez | `p3_decorator/`, `p4_composite/` | Decorator y Composite | ✅ Implementado |
| Dominique Contreras | Documento técnico, presentación, integración | Análisis, UML, arquitectura integrada | ✅ Implementado |

## Estructura del proyecto

```
comun/producto.py        Contrato compartido: Producto / ProductoSimple
p1_adapter/               Adapter — integración de PayPal y BancoLocalPay
p2_facade/                Facade — orquestación del proceso de compra
p3_decorator/             Decorator — servicios adicionales combinables
p4_composite/             Composite — combos de productos
p5_proxy/                 Proxy — carga diferida de imágenes de producto
tests/                    Una suite unittest por patrón (test_<patron>.py)
main.py                   Ejecuta el demo() de los 5 patrones
```

## Convenciones

- Nombres de clases y métodos en español (salvo `PaymentProcessor`, exigido por el enunciado).
- Con type hints y comentarios solo donde el razonamiento no es obvio.
- Cada patrón expone `demo()` en su carpeta; `main.py` las ejecuta todas.
- Una prueba `unittest` por patrón en `tests/test_<patron>.py` (18 pruebas en total).
- `Producto` (`comun/producto.py`) es el único contrato de producto: decoradores, combos y Facade lo usan.

## Uso

    python main.py
    python -m unittest discover -s tests -v