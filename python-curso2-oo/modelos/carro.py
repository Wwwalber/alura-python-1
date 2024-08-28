class Carro():
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro1 = Carro('Ranger', 'azul', 2023)

print(f'carro1: %s' % carro1.modelo) #  ou melhor
print(f'carro1: {carro1.modelo}') 