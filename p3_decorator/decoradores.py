"""Decorator: agrega servicios adicionales a un Producto sin subclases por cada
combinación posible. Cada decorador envuelve otro Producto y añade su propio
costo y texto a la descripción.
"""
from abc import ABC

from comun.producto import Producto


class ProductoDecorator(Producto, ABC):
    """Base abstracta: envuelve un Producto y delega por defecto en él."""

    def __init__(self, producto: Producto) -> None:
        self._producto = producto

    def obtener_descripcion(self) -> str:
        return self._producto.obtener_descripcion()

    def obtener_precio(self) -> float:
        return self._producto.obtener_precio()


class GarantiaExtendida(ProductoDecorator):
    COSTO = 150.0  # precio fijo arbitrario en GTQ

    def obtener_descripcion(self) -> str:
        return f"{self._producto.obtener_descripcion()} + Garantía extendida"

    def obtener_precio(self) -> float:
        return self._producto.obtener_precio() + self.COSTO


class EmpaqueRegalo(ProductoDecorator):
    COSTO = 50.0  # precio fijo arbitrario en GTQ

    def obtener_descripcion(self) -> str:
        return f"{self._producto.obtener_descripcion()} + Empaque de regalo"

    def obtener_precio(self) -> float:
        return self._producto.obtener_precio() + self.COSTO


class SeguroTransporte(ProductoDecorator):
    COSTO = 100.0  # precio fijo arbitrario en GTQ

    def obtener_descripcion(self) -> str:
        return f"{self._producto.obtener_descripcion()} + Seguro de transporte"

    def obtener_precio(self) -> float:
        return self._producto.obtener_precio() + self.COSTO


class InstalacionEspecializada(ProductoDecorator):
    COSTO = 200.0  # precio fijo arbitrario en GTQ

    def obtener_descripcion(self) -> str:
        return f"{self._producto.obtener_descripcion()} + Instalación especializada"

    def obtener_precio(self) -> float:
        return self._producto.obtener_precio() + self.COSTO
