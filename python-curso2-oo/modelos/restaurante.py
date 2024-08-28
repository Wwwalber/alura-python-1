class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome # self self que está vindo. Referencia do self que está chamendo
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes: # somente restaurates
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')


restaurante_praca = Restaurante('Praça', 'Gourmet')

restaurante_pizza = Restaurante('Pizza', 'italiana')

Restaurante.listar_restaurantes()






