from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def __str__(self):
        tipo = "esportiva" if self.tipo == 1 else "casual"
        return f"{self.marca} {self.modelo} - tipo: {tipo}"