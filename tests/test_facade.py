import unittest

from comun.producto import ProductoSimple
from p1_adapter.payment_processor import PaymentProcessor
from p2_facade.proceso_compra_facade import ProcesoCompraFacade
from p2_facade.subsistemas import (
    EnvioService,
    FacturaService,
    InventarioService,
    NotificacionService,
)


class PaymentProcessorDePrueba(PaymentProcessor):
    """Implementacion minima aislada, sin depender de p1_adapter."""

    def procesar_pago(self, monto: float) -> bool:
        return True


class TestFacade(unittest.TestCase):
    def setUp(self) -> None:
        self.facade = ProcesoCompraFacade(
            InventarioService(),
            FacturaService(),
            EnvioService(),
            NotificacionService(),
        )
        self.producto = ProductoSimple("Producto de prueba", 100.0)

    def test_realizar_compra_camino_feliz(self) -> None:
        resultado = self.facade.realizar_compra(
            "ClienteTest", self.producto, 3, PaymentProcessorDePrueba()
        )
        self.assertTrue(resultado)


if __name__ == "__main__":
    unittest.main()
