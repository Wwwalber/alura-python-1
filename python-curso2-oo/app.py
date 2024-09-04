from modelos.restaurante import Restaurante

#restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican', 'mexicana')
#restaurante_japones = Restaurante('Japa', 'Japonesa')

def main():
    restaurante_mexicano.alternar_estado()
    restaurante_mexicano.receber_avaliacao('Walber', 8)
    restaurante_mexicano.receber_avaliacao('Elizâ', 9)
    restaurante_mexicano.receber_avaliacao('Israel', 7)
    restaurante_mexicano.receber_avaliacao('Israele', 5)
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
