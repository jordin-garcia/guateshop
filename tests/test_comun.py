import unittest

from comun.producto import Producto, ProductoSimple


class TestProductoSimple(unittest.TestCase):
    def test_es_producto(self):
        self.assertIsInstance(ProductoSimple("Mouse", 150.0), Producto)

    def test_precio_y_descripcion(self):
        p = ProductoSimple("Laptop", 6500.0)
        self.assertEqual(p.obtener_descripcion(), "Laptop")
        self.assertEqual(p.obtener_precio(), 6500.0)

    def test_precio_negativo(self):
        with self.assertRaises(ValueError):
            ProductoSimple("Error", -1)


if __name__ == "__main__":
    unittest.main()
