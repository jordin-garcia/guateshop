"""Demo del patron Facade: una sola llamada orquesta todo el proceso de compra."""
from comun.producto import ProductoSimple
from p1_adapter.payment_processor import PaymentProcessor
from p2_facade.proceso_compra_facade import ProcesoCompraFacade
from p2_facade.subsistemas import (
    EnvioService,
    FacturaService,
    InventarioService,
    NotificacionService,
)

try:
    from p1_adapter.adapters import PayPalAdapter
    from p1_adapter.sistemas_externos import PayPalService

    def _crear_procesador_pago() -> PaymentProcessor:
        return PayPalAdapter(PayPalService())

except ImportError:

    class _PaymentProcessorRespaldo(PaymentProcessor):
        """Respaldo minimo para que la demo funcione si el Adapter aun no existe."""

        def procesar_pago(self, monto: float) -> bool:
            print(f"[PagoRespaldo] Pago simulado por Q{monto:.2f}")
            return True

    def _crear_procesador_pago() -> PaymentProcessor:
        return _PaymentProcessorRespaldo()


def demo() -> None:
    facade = ProcesoCompraFacade(
        InventarioService(),
        FacturaService(),
        EnvioService(),
        NotificacionService(),
    )
    producto = ProductoSimple("Camisa tipica", 150.0)
    procesador_pago = _crear_procesador_pago()

    print("=== Demo Facade: compra con una sola llamada ===")
    exito = facade.realizar_compra("Jordin", producto, 2, procesador_pago)
    print(f"Resultado de la compra: {'EXITOSA' if exito else 'FALLIDA'}")


if __name__ == "__main__":
    demo()
