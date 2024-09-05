from desafios.livro import Livro

livro1 = Livro('A casa de Inverno','Walber Costa', 2024)
livro2 = Livro('Dançando na chuva','Stephen Charl', 2002)
livro3 = Livro('A Torre','Marcos Craveiro', 2000)
livro4 = Livro('Noites iluminadas','Marta Ferreira', 1999)
livro5 = Livro('Simplicidade','Rita Cruz', 2000)
livro6 = Livro('Menina do rio','Zarife Uchoa', 2000)
livro7 = Livro('Verdade','Walber Costa', 2024)
livro8 = Livro('Os trilhos Vermelhos','Gui Costa', 2024)

Livro.livros = [livro1, livro2, livro3, livro4, livro5, livro6, livro7, livro8]

def main():
    print(livro1)
    livro1.emprestar()
    print(livro1.status_livro)
    livro1.devolver()
    print(livro1.status_livro)

    ano_especifico = 2024
    livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
    print(f'Livros disponíveis em {ano_especifico}:')

    for livro in livros_disponiveis_ano:
        print(livro)

if __name__ == '__main__':
    main()
