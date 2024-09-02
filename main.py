class NumeroComplejo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def __str__(self):
        return f"{self.real} + {self.imaginario}i"

    def suma(self, otro):
        return NumeroComplejo(self.real + otro.real, self.imaginario + otro.imaginario)

    def resta(self, otro):
        return NumeroComplejo(self.real - otro.real, self.imaginario - otro.imaginario)

    def multiplicacion(self, otro):
        real = self.real * otro.real - self.imaginario * otro.imaginario
        imaginario = self.real * otro.imaginario + self.imaginario * otro.real
        return NumeroComplejo(real, imaginario)

    def division(self, otro):
        denominador = otro.real**2 + otro.imaginario**2
        if denominador == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        real = (self.real * otro.real + self.imaginario * otro.imaginario) / denominador
        imaginario = (self.imaginario * otro.real - self.real * otro.imaginario) / denominador
        return NumeroComplejo(real, imaginario)

# Ejemplo de uso
a = NumeroComplejo(2, 3)
b = NumeroComplejo(1, 4)

print("Número complejo a:", a)
print("Número complejo b:", b)

suma = a.suma(b)
print("Suma:", suma)

resta = a.resta(b)
print("Resta:", resta)

multiplicacion = a.multiplicacion(b)
print("Multiplicación:", multiplicacion)

division = a.division(b)
print("División:", division)
