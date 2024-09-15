class Musica:
    def __init__(self, nome='', artista='', duracao=0,):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = Musica(nome='musica1', artista='artista1', duracao=50)
musica2 = Musica(nome='musica2', artista='artista2', duracao=45)

# Acessando os atributos de cada objeto
print(f'Nome: {musica1.nome}, Artista: {musica1.artista}, Duração: {musica1.duracao} minutos')
print(f'Nome: {musica2.nome}, Artista: {musica2.artista}, Duração: {musica2.duracao} minutos')
