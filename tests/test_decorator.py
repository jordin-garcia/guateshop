import unittest

from comun.producto import Producto, ProductoSimple
from p3_decorator.decoradores import (
    EmpaqueRegalo,
    GarantiaExtendida,
    InstalacionEspecializada,
    SeguroTransporte,
)


class TestDecoradores(unittest.TestCase):
    def test_apilar_decoradores_suma_precios(self):
        base = ProductoSimple("Laptop", 6500.0)
        decorado = GarantiaExtendida(EmpaqueRegalo(base))
        precio_esperado = 6500.0 + EmpaqueRegalo.COSTO + GarantiaExtendida.COSTO
        self.assertEqual(decorado.obtener_precio(), precio_esperado)

    def test_apilar_todos_los_decoradores(self):
        base = ProductoSimple("Laptop", 6500.0)
        decorado = InstalacionEspecializada(
            SeguroTransporte(GarantiaExtendida(EmpaqueRegalo(base)))
        )
        precio_esperado = (
            6500.0
            + EmpaqueRegalo.COSTO
            + GarantiaExtendida.COSTO
            + SeguroTransporte.COSTO
            + InstalacionEspecializada.COSTO
        )
        self.assertEqual(decorado.obtener_precio(), precio_esperado)

    def test_descripcion_incluye_texto_de_cada_decorador(self):
        base = ProductoSimple("Mouse", 150.0)
        decorado = SeguroTransporte(GarantiaExtendida(base))
        descripcion = decorado.obtener_descripcion()
        self.assertIn("Mouse", descripcion)
        self.assertIn("Garantía extendida", descripcion)
        self.assertIn("Seguro de transporte", descripcion)

    def test_producto_decorado_sigue_siendo_producto(self):
        base = ProductoSimple("Mochila", 300.0)
        decorado = EmpaqueRegalo(base)
        self.assertIsInstance(decorado, Producto)


if __name__ == "__main__":
    unittest.main()
