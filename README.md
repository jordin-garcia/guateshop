# GuateShop - Taller de Patrones Estructurales (Python 3.10+)

## Reparto

| Integrante | Carpeta(s) | Responsabilidad |
|---|---|---|
| 1 | `p1_adapter/`, `p5_proxy/` | Adapter y Proxy (con pruebas de lazy loading) |
| 2 | `p2_facade/` | Facade y sus cinco subsistemas |
| 3 | `p3_decorator/`, `p4_composite/` | Decorator y Composite |
| 4 | `main.py`, `tests/`, documentación | Parte I, UML integrado, Parte III, presentación e integración |

## Convenciones

- Nombres de clases y métodos en español (salvo `PaymentProcessor`, exigido por el enunciado).
- Con type hints y comentarios que expliquen el patrón.
- Cada patrón expone `demo()` en su carpeta; `main.py` las ejecuta todas.
- Una prueba `unittest` por patrón en `tests/test_<patron>.py`.
- `Producto` (`comun/producto.py`) es el único contrato de producto: decoradores, combos y Facade lo usan.

## Uso

    python main.py
    python -m unittest discover -s tests -v
