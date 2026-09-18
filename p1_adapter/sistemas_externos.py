"""Sistemas heredados del enunciado. NO se modifican (esa es la idea del Adapter)."""


class PayPalService:
    def makePayment(self, amount: float) -> None:
        print(f"[PayPal] Pago procesado por Q{amount:.2f}")


class BancoLocalPay:
    def realizarTransaccion(self, monto: float) -> None:
        print(f"[BancoLocalPay] Transacción realizada por Q{monto:.2f}")
