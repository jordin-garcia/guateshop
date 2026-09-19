"""Imagen real (costosa) y su proxy con carga perezosa."""
from p5_proxy.imagen_producto import ImagenProducto


class ImagenReal(ImagenProducto):
    def __init__(self, nombre_archivo: str) -> None:
        self._nombre_archivo = nombre_archivo
        print(f"Cargando imagen pesada desde disco: {self._nombre_archivo}")

    def mostrar(self) -> None:
        print(f"Mostrando imagen ya cargada: {self._nombre_archivo}")


class ImagenProxy(ImagenProducto):
    def __init__(self, nombre_archivo: str) -> None:
        self._nombre_archivo = nombre_archivo
        self._imagen_real: ImagenReal | None = None

    def mostrar(self) -> None:
        if self._imagen_real is None:
            self._imagen_real = ImagenReal(self._nombre_archivo)
        self._imagen_real.mostrar()
