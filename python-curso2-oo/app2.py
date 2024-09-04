from desafios.livro import Livro

livro1 = Livro('A casa de Inverno','Walber Costa', 2024)

def main():
    print(livro1)
    livro1.emprestar()
    print(livro1.status_livro)
    livro1.devolver()
    print(livro1.status_livro)


if __name__ == '__main__':
    main()
