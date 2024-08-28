class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome # self objeto que está vindo. Referencia do objeto que está chamendo
        self.categoria = categoria
        self.ativo = False

    def __str__(self):
        return self.nome


restaurante_praca = Restaurante('Praça', 'Gourmet')

restaurante_pizza = Restaurante('Pizza', 'italiana')

restaurantes = [restaurante_praca, restaurante_pizza]

# mostra métdos especiais que todas as classes possuem

print(vars(restaurante_praca))
print(vars(restaurante_pizza))
print(restaurante_praca)






