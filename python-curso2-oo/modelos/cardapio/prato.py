from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):  # informa que vai herdar métodos, atributos de uma outra classe
    def __init__(self, nome, preco, descricao):
        