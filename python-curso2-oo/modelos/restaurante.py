class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome # self self que está vindo. Referencia do self que está chamendo
        self.categoria = categoria
        self._ativo = False # _ infoma que o atributo está protegidom, embora não privado
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    def listar_restaurantes():
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in Restaurante.restaurantes: # somente restaurates
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante._ativo}')

    @property
    def ativo(self):
        return 'Ativo ❎' if self._ativo else 'Inativo ❎'

restaurante_praca = Restaurante('Praça', 'Gourmet')

restaurante_pizza = Restaurante('Pizza', 'italiana')

Restaurante.listar_restaurantes()






