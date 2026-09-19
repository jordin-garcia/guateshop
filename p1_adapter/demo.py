"""Cliente que procesa pagos con cualquier PaymentProcessor."""
from p1_adapter.payment_processor import PaymentProcessor
from p1_adapter.sistemas_externos import PayPalService, BancoLocalPay
from p1_adapter.adapters import PayPalAdapter, BancoLocalPayAdapter


def demo() -> None:
    procesadores: list[PaymentProcessor] = [
        PayPalAdapter(PayPalService()),
        BancoLocalPayAdapter(BancoLocalPay()),
    ]

    for procesador in procesadores:
        # El cliente solo conoce PaymentProcessor, no el proveedor concreto.
        exito = procesador.procesar_pago(150.0)
        print(f"Resultado del pago con {type(procesador).__name__}: {exito}")
