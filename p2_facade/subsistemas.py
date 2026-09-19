"""Subsistemas simples que el Facade orquesta.

Cada uno representa una parte del proceso de compra que, sin el Facade,
el cliente tendría que invocar manualmente y en el orden correcto.
"""
from comun.producto import Producto


class InventarioService:
    def validar_stock(self, producto: Producto, cantidad: int) -> bool:
        print(f"[Inventario] Validando stock de '{producto.obtener_descripcion()}' x{cantidad}...")
        return True


class FacturaService:
    def generar_factura(self, cliente: str, producto: Producto, cantidad: int) -> str:
        total = producto.obtener_precio() * cantidad
        factura = (
            f"Factura para {cliente}: {cantidad} x {producto.obtener_descripcion()} "
            f"= Q{total:.2f}"
        )
        print(f"[Factura] {factura}")
        return factura


class EnvioService:
    def generar_envio(self, cliente: str, producto: Producto) -> str:
        envio = f"Envio-{cliente}-{producto.obtener_descripcion()}"
        print(f"[Envio] Generado tracking '{envio}' para {cliente}")
        return envio


class NotificacionService:
    def notificar(self, cliente: str, mensaje: str) -> None:
        print(f"[Notificacion] Para {cliente}: {mensaje}")
