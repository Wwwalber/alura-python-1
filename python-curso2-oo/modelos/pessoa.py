class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}'

    @classmethod
    def aniversario(cls):
        self.idade += 1

    @property
    def saudacao(self):
        return f'Olá {self.nome}, parabéns por ser {self.profissao}'

pessoa1 = Pessoa('Walber', 39,'Programador')
pessoa1.aniversario()
pessoa1.saudacao()