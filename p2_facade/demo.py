"""Ejemplo ejecutable del patrón Facade aplicado a una compra."""

from __future__ import annotations

import logging
import sys

from comun.producto import ProductoSimple
from p1_adapter.adapters import PayPalAdapter
from p1_adapter.payment_processor import PaymentProcessor
from p1_adapter.sistemas_externos import PayPalService
from p2_facade.proceso_compra_facade import ProcesoCompraFacade
from p2_facade.subsistemas import (
    EnvioService,
    FacturaService,
    InventarioService,
    NotificacionService,
)


def _crear_procesador_pago() -> PaymentProcessor:
    """Construye el adaptador de pago usado por la demostración."""
    return PayPalAdapter(PayPalService())


def _crear_facade() -> ProcesoCompraFacade:
    """Crea el Facade e inyecta todas sus dependencias."""
    return ProcesoCompraFacade(
        inventario=InventarioService(),
        procesador_pago=_crear_procesador_pago(),
        factura=FacturaService(),
        envio=EnvioService(),
        notificacion=NotificacionService(),
    )


def main() -> None:
    """Ejecuta una compra de ejemplo mediante una sola operación."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        stream=sys.stdout,
    )

    facade = _crear_facade()
    producto = ProductoSimple("Camisa típica", 150.0)

    print("=== Demo Facade: compra con una sola llamada ===")
    compra_exitosa = facade.realizar_compra(
        cliente="Jordin",
        producto=producto,
        cantidad=2,
    )

    resultado = "EXITOSA" if compra_exitosa else "FALLIDA"
    print(f"Resultado de la compra: {resultado}")


if __name__ == "__main__":
    main()
