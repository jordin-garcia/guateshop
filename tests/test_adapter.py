import unittest

from p1_adapter.payment_processor import PaymentProcessor
from p1_adapter.sistemas_externos import PayPalService, BancoLocalPay
from p1_adapter.adapters import PayPalAdapter, BancoLocalPayAdapter


class TestPayPalAdapter(unittest.TestCase):
    def test_es_payment_processor(self):
        self.assertIsInstance(PayPalAdapter(PayPalService()), PaymentProcessor)

    def test_procesar_pago_exitoso(self):
        adaptador = PayPalAdapter(PayPalService())
        self.assertTrue(adaptador.procesar_pago(100.0))


class TestBancoLocalPayAdapter(unittest.TestCase):
    def test_es_payment_processor(self):
        self.assertIsInstance(BancoLocalPayAdapter(BancoLocalPay()), PaymentProcessor)

    def test_procesar_pago_exitoso(self):
        adaptador = BancoLocalPayAdapter(BancoLocalPay())
        self.assertTrue(adaptador.procesar_pago(100.0))


if __name__ == "__main__":
    unittest.main()
