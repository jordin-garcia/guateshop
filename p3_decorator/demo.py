"""Ejemplos con combinaciones de varios decoradores."""
from comun.producto import ProductoSimple
from p3_decorator.decoradores import (
    EmpaqueRegalo,
    GarantiaExtendida,
    InstalacionEspecializada,
    SeguroTransporte,
)


def demo() -> None:
    laptop = ProductoSimple("Laptop", 6500.0)

    laptop_con_extras = GarantiaExtendida(EmpaqueRegalo(laptop))
    print(f"{laptop_con_extras.obtener_descripcion()} -> Q{laptop_con_extras.obtener_precio():.2f}")

    laptop_completa = InstalacionEspecializada(
        SeguroTransporte(GarantiaExtendida(EmpaqueRegalo(laptop)))
    )
    print(f"{laptop_completa.obtener_descripcion()} -> Q{laptop_completa.obtener_precio():.2f}")


if __name__ == "__main__":
    demo()
