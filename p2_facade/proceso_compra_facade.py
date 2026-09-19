"""Facade que coordina los pasos necesarios para completar una compra."""

from __future__ import annotations

from math import isfinite
from typing import Protocol

from comun.producto import Producto
from p1_adapter.payment_processor import PaymentProcessor


class ServicioInventario(Protocol):
    """Contrato requerido para consultar la disponibilidad de un producto."""

    def validar_stock(self, producto: Producto, cantidad: int) -> bool:
        """Indica si existe la cantidad solicitada del producto."""
        ...


class ServicioFactura(Protocol):
    """Contrato requerido para generar una factura."""

    def generar_factura(
        self,
        cliente: str,
        producto: Producto,
        cantidad: int,
        total: float,
    ) -> str:
        """Genera la factura y devuelve su representación."""
        ...


class ServicioEnvio(Protocol):
    """Contrato requerido para programar el envío de una compra."""

    def generar_envio(
        self,
        cliente: str,
        producto: Producto,
        cantidad: int,
    ) -> str:
        """Genera el envío y devuelve su código de seguimiento."""
        ...


class ServicioNotificacion(Protocol):
    """Contrato requerido para enviar mensajes al cliente."""

    def notificar(self, cliente: str, mensaje: str) -> None:
        """Envía un mensaje al cliente."""
        ...


class ProcesoCompraFacade:
    """Ofrece una interfaz simple para ejecutar el proceso de compra."""

    MENSAJE_COMPRA_EXITOSA = "Tu compra fue procesada con éxito."
    MENSAJE_SIN_STOCK = "No hay suficiente stock para completar la compra."
    MENSAJE_PAGO_RECHAZADO = "El pago fue rechazado. La compra no se completó."

    def __init__(
        self,
        inventario: ServicioInventario,
        procesador_pago: PaymentProcessor,
        factura: ServicioFactura,
        envio: ServicioEnvio,
        notificacion: ServicioNotificacion,
    ) -> None:
        self._inventario = inventario
        self._procesador_pago = procesador_pago
        self._factura = factura
        self._envio = envio
        self._notificacion = notificacion

    def realizar_compra(
        self,
        cliente: str,
        producto: Producto,
        cantidad: int,
    ) -> bool:
        """Coordina inventario, pago, factura, envío y notificación.

        Devuelve ``True`` cuando la compra se completa. La falta de stock o el
        rechazo del pago son resultados esperados y devuelven ``False``. Los
        datos inválidos generan una excepción para no ocultar errores de uso.
        """
        cliente_normalizado = self._normalizar_cliente(cliente)
        self._validar_cantidad(cantidad)
        total = self._calcular_total(producto, cantidad)

        if not self._inventario.validar_stock(producto, cantidad):
            self._notificacion.notificar(
                cliente_normalizado,
                self.MENSAJE_SIN_STOCK,
            )
            return False

        if not self._procesador_pago.procesar_pago(total):
            self._notificacion.notificar(
                cliente_normalizado,
                self.MENSAJE_PAGO_RECHAZADO,
            )
            return False

        self._factura.generar_factura(
            cliente=cliente_normalizado,
            producto=producto,
            cantidad=cantidad,
            total=total,
        )
        self._envio.generar_envio(
            cliente=cliente_normalizado,
            producto=producto,
            cantidad=cantidad,
        )
        self._notificacion.notificar(
            cliente_normalizado,
            self.MENSAJE_COMPRA_EXITOSA,
        )
        return True

    @staticmethod
    def _normalizar_cliente(cliente: str) -> str:
        if not isinstance(cliente, str):
            raise TypeError("El nombre del cliente debe ser una cadena de texto.")

        cliente_normalizado = cliente.strip()
        if not cliente_normalizado:
            raise ValueError("El nombre del cliente no puede estar vacío.")

        return cliente_normalizado

    @staticmethod
    def _validar_cantidad(cantidad: int) -> None:
        if isinstance(cantidad, bool) or not isinstance(cantidad, int):
            raise TypeError("La cantidad debe ser un número entero.")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

    @staticmethod
    def _calcular_total(producto: Producto, cantidad: int) -> float:
        if producto is None:
            raise ValueError("El producto es obligatorio.")

        try:
            precio = float(producto.obtener_precio())
        except (AttributeError, TypeError, ValueError) as error:
            raise TypeError("El producto debe proporcionar un precio válido.") from error

        if not isfinite(precio) or precio < 0:
            raise ValueError("El precio del producto debe ser un valor válido.")

        return round(precio * cantidad, 2)
