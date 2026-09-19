"""Facade: punto de entrada único para realizar una compra completa."""
from comun.producto import Producto
from p1_adapter.payment_processor import PaymentProcessor
from p2_facade.subsistemas import (
    EnvioService,
    FacturaService,
    InventarioService,
    NotificacionService,
)


class ProcesoCompraFacade:
    def __init__(
        self,
        inventario: InventarioService,
        factura: FacturaService,
        envio: EnvioService,
        notificacion: NotificacionService,
    ) -> None:
        self._inventario = inventario
        self._factura = factura
        self._envio = envio
        self._notificacion = notificacion

    def realizar_compra(
        self,
        cliente: str,
        producto: Producto,
        cantidad: int,
        procesador_pago: PaymentProcessor,
    ) -> bool:
        if not self._inventario.validar_stock(producto, cantidad):
            return False

        monto = producto.obtener_precio() * cantidad
        if not procesador_pago.procesar_pago(monto):
            return False

        self._factura.generar_factura(cliente, producto, cantidad)
        self._envio.generar_envio(cliente, producto)
        self._notificacion.notificar(cliente, "Tu compra fue procesada con exito.")
        return True
