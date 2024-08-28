class Restaurante:
    def __ini__(self, nome, categoria):
        self.nome = ''
        self.categoria = ''
        self.ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praca'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

# mostra métdos especiais que todas as classes possuem
print(dir(restaurante_praca))


restaurante_praca.categoria = 'Italiana'
print(vars(restaurante_praca))

print(restaurante_praca.categoria)
print(restaurante_praca.ativo)

restaurante_praca.nome = 'Bistro'
print(restaurante_praca.nome)

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = 'Ativo'
print(f'Restaurante:', {restaurante_pizza.nome})
print(f'Categoria:', {restaurante_pizza.categoria})
print(f'Ativo:', {restaurante_pizza.ativo})



