class Restaurante:
    def __init__(self, nome, categoria, ativo):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        padrao = ''
        estacionamento = True

restaurante1 = Restaurante('Pavão','italiano',True)
restaurante1.padrao = '5 estrelas'
restaurante1.estacionamento = False

print(f'Detalhes do restaurante: {restaurante1.nome} | {restaurante1.categoria} | {restaurante1.ativo} | {restaurante1.padrao} | {restaurante1.estacionamento}')