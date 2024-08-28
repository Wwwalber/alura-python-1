class Musica:
    nome = ''
    artista = ''
    duracao = int

musica1 = Musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.artista = 'Queen'
musica1.duracao = 45

musica2 = Musica()
musica2.nome = 'Jazz'
musica2.artista = 'Beatles'
musica2.duracao = 30

# Acessando os atributos de cada objeto
print(f'Nome: {musica1.nome}, Artista: {musica1.artista}, Duração: {musica1.duracao} minutos')
print(f'Nome: {musica2.nome}, Artista: {musica2.artista}, Duração: {musica2.duracao} minutos')