from modelos.avaliacao import Avaliacao
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title() # self self que está vindo. Referencia do self que está chamendo
        self.categoria = categoria.upper()
        self._ativo = False # _ infoma que o atributo está protegidom, embora não privado
        self._avaliacao = [] # para armazena várias
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self.categoria}'

    @classmethod    #indicar que é um método da classe
    def listar_restaurantes(cls):  # cls é a convenção para indicar que uaremos informaçõe referentes a esse método 
                                    # agora, em vez de 'Restaurante' usar 'cls'
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes: # somente restaurates
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante._ativo}')

    @property
    def ativo(self):
        return 'Ativo ❎' if self._ativo else 'Inativo ❎'

    # método para classe instanciada
    def alternar_estado(self): # informar a referencia > self
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property # par ser capaz de ler as informações
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas/quantidade_de_notas, 1) # exibir uma casa decimal
        return media


