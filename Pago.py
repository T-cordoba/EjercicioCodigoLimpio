class Pago:
    def __init__(self, monto, cuotas, porcentaje_interes):
        self.monto = monto
        self.cuotas = cuotas
        self.porcentaje_interes = porcentaje_interes / 100

    def calcular_valor_cuotas_interes_incluido(self):
        if self.porcentaje_interes == 0:
            return self.monto / self.cuotas

        if self.cuotas == 1:
            return self.monto

        if self.cuotas == 0:
            raise Exception('Numero de cuotas invalido')

        return self.monto * (self.porcentaje_interes * (1 + self.porcentaje_interes) ** self.cuotas) \
               / ((1 + self.porcentaje_interes) ** self.cuotas - 1)

    def calcular_total(self):
        return self.calcular_valor_cuotas_interes_incluido() * self.cuotas

    def calcular_beneficio_banco(self):
        return self.calcular_total() - self.monto
