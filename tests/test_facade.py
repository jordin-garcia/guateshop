"""Pruebas unitarias para el proceso de compra mediante el patrón Facade."""

import unittest
from unittest.mock import create_autospec

from comun.producto import ProductoSimple
from p1_adapter.payment_processor import PaymentProcessor
from p2_facade.proceso_compra_facade import ProcesoCompraFacade
from p2_facade.subsistemas import (
    EnvioService,
    FacturaService,
    InventarioService,
    NotificacionService,
)


class TestProcesoCompraFacade(unittest.TestCase):
    """Verifica la coordinación de los subsistemas durante una compra."""

    CLIENTE = "ClienteTest"
    CANTIDAD = 3
    PRECIO_UNITARIO = 100.0
    TOTAL_ESPERADO = 300.0

    def setUp(self) -> None:
        """Crea dependencias aisladas antes de cada prueba."""
        self.inventario = create_autospec(InventarioService, instance=True)
        self.procesador_pago = create_autospec(PaymentProcessor, instance=True)
        self.factura = create_autospec(FacturaService, instance=True)
        self.envio = create_autospec(EnvioService, instance=True)
        self.notificacion = create_autospec(NotificacionService, instance=True)

        self.inventario.validar_stock.return_value = True
        self.procesador_pago.procesar_pago.return_value = True

        self.facade = ProcesoCompraFacade(
            inventario=self.inventario,
            procesador_pago=self.procesador_pago,
            factura=self.factura,
            envio=self.envio,
            notificacion=self.notificacion,
        )
        self.producto = ProductoSimple(
            "Producto de prueba",
            self.PRECIO_UNITARIO,
        )

    def test_realizar_compra_camino_feliz(self) -> None:
        """Completa la compra cuando existe stock y el pago es aprobado."""
        resultado = self.facade.realizar_compra(
            cliente=self.CLIENTE,
            producto=self.producto,
            cantidad=self.CANTIDAD,
        )

        self.assertTrue(resultado)
        self.inventario.validar_stock.assert_called_once_with(
            self.producto,
            self.CANTIDAD,
        )
        self.procesador_pago.procesar_pago.assert_called_once_with(
            self.TOTAL_ESPERADO,
        )
        self.factura.generar_factura.assert_called_once_with(
            cliente=self.CLIENTE,
            producto=self.producto,
            cantidad=self.CANTIDAD,
            total=self.TOTAL_ESPERADO,
        )
        self.envio.generar_envio.assert_called_once_with(
            cliente=self.CLIENTE,
            producto=self.producto,
            cantidad=self.CANTIDAD,
        )
        self.notificacion.notificar.assert_called_once_with(
            self.CLIENTE,
            ProcesoCompraFacade.MENSAJE_COMPRA_EXITOSA,
        )

    def test_no_procesar_pago_cuando_no_hay_stock(self) -> None:
        """Detiene la compra antes del pago cuando no existe stock."""
        self.inventario.validar_stock.return_value = False

        resultado = self.facade.realizar_compra(
            cliente=self.CLIENTE,
            producto=self.producto,
            cantidad=self.CANTIDAD,
        )

        self.assertFalse(resultado)
        self.procesador_pago.procesar_pago.assert_not_called()
        self.factura.generar_factura.assert_not_called()
        self.envio.generar_envio.assert_not_called()
        self.notificacion.notificar.assert_called_once_with(
            self.CLIENTE,
            ProcesoCompraFacade.MENSAJE_SIN_STOCK,
        )

    def test_no_generar_factura_cuando_el_pago_es_rechazado(self) -> None:
        """Detiene factura y envío cuando el procesador rechaza el pago."""
        self.procesador_pago.procesar_pago.return_value = False

        resultado = self.facade.realizar_compra(
            cliente=self.CLIENTE,
            producto=self.producto,
            cantidad=self.CANTIDAD,
        )

        self.assertFalse(resultado)
        self.factura.generar_factura.assert_not_called()
        self.envio.generar_envio.assert_not_called()
        self.notificacion.notificar.assert_called_once_with(
            self.CLIENTE,
            ProcesoCompraFacade.MENSAJE_PAGO_RECHAZADO,
        )

    def test_rechazar_cantidad_invalida(self) -> None:
        """Rechaza cantidades menores o iguales a cero."""
        with self.assertRaisesRegex(
            ValueError,
            "La cantidad debe ser mayor que cero",
        ):
            self.facade.realizar_compra(
                cliente=self.CLIENTE,
                producto=self.producto,
                cantidad=0,
            )

        self.inventario.validar_stock.assert_not_called()
        self.procesador_pago.procesar_pago.assert_not_called()


if __name__ == "__main__":
    unittest.main()
