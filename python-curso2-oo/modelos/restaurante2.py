class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.padrao = ''
        self.estacionamento = True

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

restaurante1 = Restaurante('Pavão','italiano')
restaurante1.padrao = '5 estrelas'
restaurante1.estacionamento = False

print(f'Detalhes do restaurante: {restaurante1.nome} | {restaurante1.categoria} | {restaurante1.ativo} | {restaurante1.padrao} | {restaurante1.estacionamento}')

print(restaurante1)

class Cliente:
    def __init__(self, nome='', idade=0, email='', telefone=''):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
    
    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.email} | {self.telefone}'

# Instanciando três objetos da classe Cliente e atribuindo valores aos seus atributos através do construtor
cliente1 = Cliente(nome='Alice', idade=25, email='alice@gmail.com', telefone='123-456-7890')
cliente2 = Cliente(nome='Bob', idade=30, email='bob@gmail.com', telefone='987-654-3210')
cliente3 = Cliente(nome='Charlie', idade=22, email='charlie@gmail.com', telefone='555-123-4567')

print(cliente1)