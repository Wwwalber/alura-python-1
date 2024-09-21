from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida('Suco de melancia', 5.0, 'grande')
prato_paozinho = Prato('Paozinho', 2.0, 'O melhor pão da cidade')
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
    #print(restaurante_praca)
    #print(bebida_suco)
    #print(prato_paozinho)
    restaurante_praca.listar_restaurantes()
    restaurante_praca.exibir_cardapio
    

if __name__ == '__main__':
    main()
