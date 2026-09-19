import unittest

from comun.producto import Producto, ProductoSimple
from p4_composite.componente_producto import ComboProducto


class TestComboProducto(unittest.TestCase):
    def test_precio_suma_a_los_hijos(self):
        combo = ComboProducto("Combo Tecnología")
        combo.agregar(ProductoSimple("Laptop", 6500.0))
        combo.agregar(ProductoSimple("Mouse", 150.0))
        combo.agregar(ProductoSimple("Mochila", 300.0))
        self.assertEqual(combo.obtener_precio(), 6950.0)

    def test_agregar_y_eliminar(self):
        combo = ComboProducto("Combo Básico")
        mouse = ProductoSimple("Mouse", 150.0)
        combo.agregar(mouse)
        self.assertEqual(combo.obtener_precio(), 150.0)
        combo.eliminar(mouse)
        self.assertEqual(combo.obtener_precio(), 0.0)

    def test_combos_anidados_suman_recursivamente(self):
        combo_interno = ComboProducto("Accesorios")
        combo_interno.agregar(ProductoSimple("Mouse", 150.0))
        combo_interno.agregar(ProductoSimple("Cámara Web", 250.0))

        combo_externo = ComboProducto("Combo Tecnología")
        combo_externo.agregar(ProductoSimple("Laptop", 6500.0))
        combo_externo.agregar(combo_interno)

        self.assertEqual(combo_externo.obtener_precio(), 6900.0)

    def test_combo_es_producto(self):
        combo = ComboProducto("Combo Tecnología")
        self.assertIsInstance(combo, Producto)


if __name__ == "__main__":
    unittest.main()
