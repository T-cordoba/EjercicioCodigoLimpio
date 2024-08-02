import unittest
from Pago import Pago


class Prueba(unittest.TestCase):
    def test_probar_calculo_cuota_1(self):
        pago = Pago(200000, 36, 3.1)
        cuota = 9297.96
        resultado = pago.calcular_valor_cuotas_interes_incluido()
        self.assertEqual(cuota, round(resultado, 2))

    def test_probar_calculo_cuota_2(self):
        pago = Pago(850000, 24, 3.4)
        cuota = 52377.5
        resultado = pago.calcular_valor_cuotas_interes_incluido()
        self.assertEqual(cuota, round(resultado, 2))

    def test_probar_calculo_cuota_3(self):
        pago = Pago(480000, 48, 0)
        cuota = 10000
        resultado = pago.calcular_valor_cuotas_interes_incluido()
        self.assertEqual(cuota, round(resultado, 2))

    def test_probar_calculo_cuota_4(self):
        pago = Pago(90000, 1, 2.4)
        cuota = 90000
        resultado = pago.calcular_valor_cuotas_interes_incluido()
        self.assertEqual(cuota, round(resultado, 2))


if __name__ == '__main__':
    unittest.main()
