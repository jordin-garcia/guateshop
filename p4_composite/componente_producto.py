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

    def _contiene(self, otro: Producto) -> bool:
        """True si `otro` está en cualquier nivel del árbol bajo este combo."""
        return any(
            hijo is otro or (isinstance(hijo, ComboProducto) and hijo._contiene(otro))
            for hijo in self._hijos
        )

    def agregar(self, producto: Producto) -> None:
        # Un combo que se contiene a sí mismo (directa o indirectamente) haría que
        # obtener_precio y obtener_descripcion recursen sin fin.
        if producto is self or (
            isinstance(producto, ComboProducto) and producto._contiene(self)
        ):
            raise ValueError("No se puede agregar un combo dentro de sí mismo.")
        self._hijos.append(producto)

    def eliminar(self, producto: Producto) -> None:
        """Quita el producto; lanza ValueError si no está en este combo."""
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
