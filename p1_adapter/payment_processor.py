"""Interfaz objetivo del Adapter (Integrante 1). Usada también por el Facade."""
from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def procesar_pago(self, monto: float) -> bool:
        """Procesa un pago. Devuelve True si fue exitoso."""
