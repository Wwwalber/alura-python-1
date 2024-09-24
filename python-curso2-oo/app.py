from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida('Suco de melancia', 5.0, 'grande')
prato_paozinho = Prato('Paozinho', 2.0, 'O melhor pão da cidade')
# crie mais 10 pratos e bebidas


restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
# Create more pratos and bebidas
prato_lasanha = Prato('Lasanha', 15.0, 'Deliciosa lasanha ao molho de tomate')
prato_feijoada = Prato('Feijoada', 12.0, 'Feijoada caseira com arroz e feijão preto')
prato_strogonoff = Prato('Strogonoff de frango', 10.0, 'Strogonoff de frango com arroz branco')
prato_feijoada.aplicar_desconto()
prato_bife_acebolado = Prato('Bife acebolado', 18.0, 'Bife acebolado com batata frita')
prato_espaguete_a_bolonhesa = Prato('Espaguete à bolonhesa', 14.0, 'Espaguete à bolonhesa com molho de tomate')

bebida_refrigerante = Bebida('Refrigerante', 4.0, 'Refrigerante lata')
bebida_cerveja = Bebida('Cerveja', 6.0, 'Cerveja artesanal')
bebida_cerveja.aplicar_desconto()
bebida_vinho = Bebida('Vinho', 20.0, 'Vinho tinto seleção')
bebida_suco_laranja = Bebida('Suco de laranja', 3.0, 'Suco de laranja natural')
bebida_suco_laranja.aplicar_desconto()
bebida_agua = Bebida('Água', 1.5, 'Água mineral sem gás')

# Add more pratos and bebidas to the cardapio
restaurante_praca.adicionar_no_cardapio(prato_lasanha)
restaurante_praca.adicionar_no_cardapio(prato_feijoada)
restaurante_praca.adicionar_no_cardapio(prato_strogonoff)
restaurante_praca.adicionar_no_cardapio(prato_bife_acebolado)
restaurante_praca.adicionar_no_cardapio(prato_espaguete_a_bolonhesa)
restaurante_praca.adicionar_no_cardapio(bebida_refrigerante)
restaurante_praca.adicionar_no_cardapio(bebida_cerveja)
restaurante_praca.adicionar_no_cardapio(bebida_vinho)
restaurante_praca.adicionar_no_cardapio(bebida_suco_laranja)
restaurante_praca.adicionar_no_cardapio(bebida_agua)

def main():
    #print(restaurante_praca)
    #print(bebida_suco)
    #print(prato_paozinho)
    restaurante_praca.listar_restaurantes()
    restaurante_praca.exibir_cardapio
    

if __name__ == '__main__':
    main()
