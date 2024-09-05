from desafios.livro import Livro

livro1 = Livro('A casa de Inverno','Walber Costa', 2024)
livro1 = Livro('Dançando na chuva','Stephen Charl', 2002)
livro1 = Livro('A Torre','Marcos Craveiro', 2000)
livro1 = Livro('Noites iluminadas','Marta Ferreira', 1999)
livro1 = Livro('Simplicidade','Rita Cruz', 2000)
livro1 = Livro('Menina do rio','Zarife Uchoa', 2000)
livro1 = Livro('Verdade','Walber Costa', 2024)
livro1 = Livro('Os trilhos Vermelhos','Gui Costa', 2024)


def main():
    print(livro1)
    livro1.emprestar()
    print(livro1.status_livro)
    livro1.devolver()
    print(livro1.status_livro)
    livro1.verificar_disponibilidade(2024)


if __name__ == '__main__':
    main()
