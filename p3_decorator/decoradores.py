"""Decorator: agrega servicios adicionales a un Producto sin subclases por cada
combinación posible. Cada decorador envuelve otro Producto y añade su propio
costo y texto a la descripción.
"""
from abc import ABC

from comun.producto import Producto


class ProductoDecorator(Producto, ABC):
    """Base abstracta: envuelve un Producto y delega por defecto en él.

    Los decoradores se apilan: cada uno recibe el producto ya decorado por el
    anterior, así que el orden de aplicación determina el orden del texto en la
    descripción (el precio suma lo mismo sin importar el orden). También pueden
    envolver un ComboProducto, porque ambos cumplen el contrato Producto.
    """

    def __init__(self, producto: Producto) -> None:
        self._producto = producto

    def obtener_descripcion(self) -> str:
        return self._producto.obtener_descripcion()

    def obtener_precio(self) -> float:
        return self._producto.obtener_precio()


class GarantiaExtendida(ProductoDecorator):
    """Servicio adicional: garantía extendida (costo fijo en COSTO)."""

    COSTO = 150.0  # precio fijo arbitrario en GTQ

    def obtener_descripcion(self) -> str:
        return f"{self._producto.obtener_descripcion()} + Garantía extendida"

    def obtener_precio(self) -> float:
        return self._producto.obtener_precio() + self.COSTO


class EmpaqueRegalo(ProductoDecorator):
    """Servicio adicional: empaque de regalo (costo fijo en COSTO)."""

    COSTO = 50.0  # precio fijo arbitrario en GTQ

    def obtener_descripcion(self) -> str:
        return f"{self._producto.obtener_descripcion()} + Empaque de regalo"

    def obtener_precio(self) -> float:
        return self._producto.obtener_precio() + self.COSTO


class SeguroTransporte(ProductoDecorator):
    """Servicio adicional: seguro de transporte (costo fijo en COSTO)."""

    COSTO = 100.0  # precio fijo arbitrario en GTQ

    def obtener_descripcion(self) -> str:
        return f"{self._producto.obtener_descripcion()} + Seguro de transporte"

    def obtener_precio(self) -> float:
        return self._producto.obtener_precio() + self.COSTO


class InstalacionEspecializada(ProductoDecorator):
    """Servicio adicional: instalación especializada (costo fijo en COSTO)."""

    COSTO = 200.0  # precio fijo arbitrario en GTQ

    def obtener_descripcion(self) -> str:
        return f"{self._producto.obtener_descripcion()} + Instalación especializada"

    def obtener_precio(self) -> float:
        return self._producto.obtener_precio() + self.COSTO
