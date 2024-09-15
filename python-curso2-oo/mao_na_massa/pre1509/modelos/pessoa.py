class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'


    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        return f'Olá {self.nome}, parabéns por ser {self.profissao}'

pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
print("Informações Iniciais:")
print(pessoa1)
pessoa1.aniversario()
print(pessoa1.saudacao)
print("Informações após aniversário:")
print(pessoa1)