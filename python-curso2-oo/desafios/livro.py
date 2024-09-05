class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'- {self.titulo}, de {self.autor}, publicado em {self.ano_publicacao}'

    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
            print('Empréstimo efetuado')
        else:
            print('Emprestimo não disponível')

    def devolver(self):
        if self.disponivel == True:
            print('Livro já foi devolvido')
        else:
            print('Devolução efetuado')
            self.disponivel = True

    @property
    def status_livro(self):
        if self.disponivel == True:
            return 'Status - Disponível'
        else:
            return 'Status - Emprestado'
    
    @staticmethod
    def verificar_disponibilidade(publicado_em):
        #print(f'Relação de livros publicados em {publicado_em}:')
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == publicado_em and livro.disponivel]
        return livros_disponiveis 

