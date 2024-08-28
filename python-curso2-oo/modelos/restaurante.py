class Restaurante:
    def __init__(this, nome, categoria):
        this.nome = nome # this objeto que está vindo. Referencia do objeto que está chamendo
        this.categoria = categoria
        this.ativo = False

    def __str__(this):
        return f'{this.nome} | {this.categoria}'


restaurante_praca = Restaurante('Praça', 'Gourmet')

restaurante_pizza = Restaurante('Pizza', 'italiana')

restaurantes = [restaurante_praca, restaurante_pizza]

# mostra métdos especiais que todas as classes possuem

print(vars(restaurante_praca))
print(vars(restaurante_pizza))
print(restaurante_praca)






