"""Ejecuta las demostraciones de los cinco patrones estructurales."""
import importlib

DEMOS = [
    ("Adapter - Sistemas de pago", "p1_adapter.demo"),
    ("Facade - Proceso de compra", "p2_facade.demo"),
    ("Decorator - Servicios adicionales", "p3_decorator.demo"),
    ("Composite - Combos de productos", "p4_composite.demo"),
    ("Proxy - Carga diferida de imágenes", "p5_proxy.demo"),
]


def main() -> None:
    for titulo, modulo in DEMOS:
        print(f"\n{'=' * 55}\n{titulo}\n{'=' * 55}")
        try:
            importlib.import_module(modulo).demo()
        except NotImplementedError:
            print("  [pendiente de implementar]")


if __name__ == "__main__":
    main()
