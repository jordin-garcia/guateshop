import unittest

from p5_proxy.imagenes import ImagenReal, ImagenProxy


class TestImagenProxy(unittest.TestCase):
    def test_no_carga_hasta_primer_mostrar(self):
        proxy = ImagenProxy("foto.jpg")
        self.assertIsNone(proxy._imagen_real)

        proxy.mostrar()
        self.assertIsNotNone(proxy._imagen_real)

    def test_reutiliza_misma_instancia(self):
        proxy = ImagenProxy("foto.jpg")

        proxy.mostrar()
        primera_instancia = proxy._imagen_real
        self.assertIsInstance(primera_instancia, ImagenReal)

        proxy.mostrar()
        self.assertIs(proxy._imagen_real, primera_instancia)


if __name__ == "__main__":
    unittest.main()
