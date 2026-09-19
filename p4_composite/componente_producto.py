"""Composite: permite tratar productos individuales y combos de productos de
forma uniforme. Las hojas del árbol son directamente comun.producto.ProductoSimple
(ya implementa Producto); los nodos internos son ComboProducto.
"""
from abc import ABC

from comun.producto import Producto


class ComponenteProducto(Producto, ABC):
    """Component del patrón Composite: mismo contrato que Producto."""


class ComboProducto(ComponenteProducto):
    """Nodo compuesto: agrupa ProductoSimple u otros ComboProducto (anidables)."""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self._hijos: list[Producto] = []

    def agregar(self, producto: Producto) -> None:
        self._hijos.append(producto)

    def eliminar(self, producto: Producto) -> None:
        self._hijos.remove(producto)

    def obtener_precio(self) -> float:
        return sum(hijo.obtener_precio() for hijo in self._hijos)

    def obtener_descripcion(self) -> str:
        descripciones = ", ".join(hijo.obtener_descripcion() for hijo in self._hijos)
        return f"{self.nombre} ({descripciones})"

    def mostrar_contenido(self, nivel: int = 0) -> None:
        indentacion = "  " * nivel
        print(f"{indentacion}- {self.nombre} (Q{self.obtener_precio():.2f})")
        for hijo in self._hijos:
            if isinstance(hijo, ComboProducto):
                hijo.mostrar_contenido(nivel + 1)
            else:
                print(f"{indentacion}  - {hijo.obtener_descripcion()} (Q{hijo.obtener_precio():.2f})")
