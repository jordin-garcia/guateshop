"""Construye el "Combo Tecnología" y muestra su total y contenido."""
from comun.producto import Producto, ProductoSimple
from p4_composite.componente_producto import ComboProducto


def _imprimir_como_producto(producto: Producto) -> None:
    print(f"Tratado como Producto: {producto.obtener_descripcion()} -> Q{producto.obtener_precio():.2f}")


def demo() -> None:
    laptop = ProductoSimple("Laptop", 6500.0)
    mouse = ProductoSimple("Mouse", 150.0)
    mochila = ProductoSimple("Mochila", 300.0)
    camara_web = ProductoSimple("Cámara Web", 250.0)

    combo_tecnologia = ComboProducto("Combo Tecnología")
    combo_tecnologia.agregar(laptop)
    combo_tecnologia.agregar(mouse)
    combo_tecnologia.agregar(mochila)
    combo_tecnologia.agregar(camara_web)

    print(f"Precio total del combo: Q{combo_tecnologia.obtener_precio():.2f}")
    combo_tecnologia.mostrar_contenido()

    # Un ComboProducto se trata igual que un ProductoSimple: ambos son Producto.
    _imprimir_como_producto(combo_tecnologia)


if __name__ == "__main__":
    demo()
