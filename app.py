import os

def exibir_nome_do_programa():
    print("""
╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━╮
┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭━━╯
┃╰━━┳━━┫╰━┳━━┳━╮┃╰━━┳╮╭┳━━┳━┳━━┳━━┳━━╮
╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯┃╭━━┻╋╋┫╭╮┃╭┫┃━┫━━┫━━┫
┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱┃╰━━┳╋╋┫╰╯┃┃┃┃━╋━━┣━━┃
╰━━━┻╯╰┻━━┻━━┻╯╱╰━━━┻╯╰┫╭━┻╯╰━━┻━━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
""")
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def opcao_invalida():
    print('Opção invalida\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()
    
def escolher_opcoes():
    opcao_escolhida = int(input('Escolha uma opção:'))
    #opcao_escolhida = int(opcao_escolhida)
    match opcao_escolhida:
        case 1:
            print('Cadastrar restaurantes')
        case 2:
            print('Listar restaurantes')
        case 3:
            print('Ativar restaurantes')
        case 4:
            finalizar_app()
        case _:
            opcao_invalida()

def finalizar_app():
    os.system('clear')
    print('Saindo da Aplicação...\n')
    exit()

def main():
    os.system('clear') # função que limpa a tela do terminal
    exibir_nome_do_programa() # função que controla o projeto
    exibir_opcoes()
    escolher_opcoes()

# .py posso informa que é o arquivo principal do programa
if __name__ == '__main__':
    main()