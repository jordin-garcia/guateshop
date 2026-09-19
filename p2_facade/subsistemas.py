"""Implementaciones sencillas de los subsistemas del proceso de compra."""

from __future__ import annotations

import logging
from uuid import uuid4

from comun.producto import Producto


LOGGER = logging.getLogger(__name__)


class InventarioService:
    """Simula la consulta de existencias de un producto."""

    def validar_stock(self, producto: Producto, cantidad: int) -> bool:
        descripcion = producto.obtener_descripcion()
        LOGGER.info(
            "[Inventario] Validando stock de '%s' x%d...",
            descripcion,
            cantidad,
        )

        # En una aplicación real, aquí se consultaría la base de datos.
        return True


class FacturaService:
    """Genera una representación sencilla de la factura de compra."""

    def generar_factura(
        self,
        cliente: str,
        producto: Producto,
        cantidad: int,
        total: float,
    ) -> str:
        descripcion = producto.obtener_descripcion()
        factura = f"Factura para {cliente}: {cantidad} x {descripcion} = Q{total:.2f}"
        LOGGER.info("[Factura] %s", factura)
        return factura


class EnvioService:
    """Crea un código de seguimiento para el envío de la compra."""

    def generar_envio(
        self,
        cliente: str,
        producto: Producto,
        cantidad: int,
    ) -> str:
        codigo_seguimiento = f"ENV-{uuid4().hex[:8].upper()}"
        LOGGER.info(
            "[Envío] Código '%s' generado para %s: %d x %s.",
            codigo_seguimiento,
            cliente,
            cantidad,
            producto.obtener_descripcion(),
        )
        return codigo_seguimiento


class NotificacionService:
    """Envía mensajes relacionados con el resultado de una compra."""

    def notificar(self, cliente: str, mensaje: str) -> None:
        LOGGER.info("[Notificación] Para %s: %s", cliente, mensaje)
