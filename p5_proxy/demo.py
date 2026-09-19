"""Demuestra con mensajes cuándo se carga realmente la imagen."""
from p5_proxy.imagenes import ImagenProxy


def demo() -> None:
    imagen = ImagenProxy("producto_zapato.jpg")

    print("Proxy creado. La imagen real todavía no se ha cargado.")

    print("Primera llamada a mostrar():")
    imagen.mostrar()

    print("Segunda llamada a mostrar():")
    imagen.mostrar()
