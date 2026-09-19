"""Adaptadores que permiten usar los sistemas externos como un PaymentProcessor."""
from p1_adapter.payment_processor import PaymentProcessor
from p1_adapter.sistemas_externos import PayPalService, BancoLocalPay


class PayPalAdapter(PaymentProcessor):
    def __init__(self, servicio: PayPalService) -> None:
        self._servicio = servicio

    def procesar_pago(self, monto: float) -> bool:
        self._servicio.makePayment(monto)
        return True


class BancoLocalPayAdapter(PaymentProcessor):
    def __init__(self, servicio: BancoLocalPay) -> None:
        self._servicio = servicio

    def procesar_pago(self, monto: float) -> bool:
        self._servicio.realizarTransaccion(monto)
        return True
