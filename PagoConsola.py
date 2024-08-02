from Pago import Pago


class Main:
    def __init__(self):
        self.monto = 0
        self.cuotas = 0
        self.porcentaje_interes = 0
        self.pago = None

    def mostrar_calculos(self):
        try:
            self.monto = float(input('Ingrese el monto del pago: '))
            self.cuotas = float(input('Ingrese el numero de cuotas que tiene el pago: '))
            self.porcentaje_interes = (float(input('Ingrese el porcentaje de interés que tiene su banco: ')))
            self.pago = Pago(self.monto, self.cuotas, self.porcentaje_interes)
        except Exception as err:
            return err

        try:
            valor_cuota = round(self.pago.calcular_valor_cuotas_interes_incluido(), 2)
            valor_total_interes = round(self.pago.calcular_total(), 2)
            beneficio_banco = round(self.pago.calcular_beneficio_banco(), 2)
        except Exception as err:
            return err

        return f'El análisis de los cobros de su pago es el siguiente: \n' \
               f'El valor de cada cuota con interés incluido ' \
               f'es de ${valor_cuota} \n' \
               f'El valor total de su pago con interés incluido es de ${valor_total_interes} \n' \
               f'El beneficio que obtiene su banco en intereses es de ' \
               f'${beneficio_banco} \n'


M = Main()

print(M.mostrar_calculos())
