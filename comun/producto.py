"""Contrato común de producto.

Lo comparten Decorator, Composite y Facade. Tanto los decoradores como los combos deben heredar de
`Producto` para poder usarse en cualquier parte del sistema.
"""
from abc import ABC, abstractmethod


class Producto(ABC):
    @abstractmethod
    def obtener_descripcion(self) -> str:
        """Descripción legible del producto."""

    @abstractmethod
    def obtener_precio(self) -> float:
        """Precio total en quetzales (GTQ)."""


class ProductoSimple(Producto):
    """Producto concreto base (hoja para Composite, núcleo para Decorator)."""

    def __init__(self, nombre: str, precio: float) -> None:
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.nombre = nombre
        self.precio = precio

    def obtener_descripcion(self) -> str:
        return self.nombre

    def obtener_precio(self) -> float:
        return self.precio
