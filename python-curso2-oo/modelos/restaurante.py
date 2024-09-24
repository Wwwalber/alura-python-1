from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
class Restaurante:
    """ representa um restaurante e suas características """

    restaurantes = []

    def __init__(self, nome, categoria):

        """
        Inicializa uma instância de restaurante.

        Parâmetros:
            - nome (str): O nome do restaurante.
            - categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title() # self self que está vindo. Referencia do self que está chamendo
        self.categoria = categoria.upper()
        self._ativo = False # _ infoma que o atributo está protegidom, embora não privado
        self._avaliacao = [] # para armazena várias
        Restaurante.restaurantes.append(self)
        self._cardapio = []  # Initialize cardapio as an empty list


    def __str__(self):
        """ Retorna uma representação string do restaurante """
        return f'{self._nome} | {self.categoria}'

    @classmethod    #indicar que é um método da classe
    def listar_restaurantes(cls):  # cls é a convenção para indicar que uaremos informaçõe referentes a esse método 
                                    # agora, em vez de 'Restaurante' usar 'cls'
        """ Exibe uma lista formatada de todos os restaurantes """                                    
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes: # somente restaurates
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante._ativo}')

    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return 'Ativo ❎' if self._ativo else 'Inativo ❎'

    # método para classe instanciada
    def alternar_estado(self): # informar a referencia > self
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Registra as avaliações de um restaurante 

        Parâmetros:
        - Cliente (str): o nome do cliente que fez a avaliação
        - nota (float): a nota atribuida ao restaurante (entre 1 e 5)

        """
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        else:
            self.nota = int(input('Informe uma nota de 0 a 5\n'))

    @property # par ser capaz de ler as informações
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacao:
            return 'Sem avaliação'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas/quantidade_de_notas, 1) # exibir uma casa decimal
        return media

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
    
    @property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}\n')
        """ exibir a lista usando enumeração """
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. {item._nome} | Preço: R$ {item._preco} | Descricao: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. {item._nome} | Preço: R$ {item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)
