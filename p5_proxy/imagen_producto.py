"""Interfaz del Proxy (Integrante 1)."""
from abc import ABC, abstractmethod


class ImagenProducto(ABC):
    @abstractmethod
    def mostrar(self) -> None:
        """Muestra la imagen del producto."""
