import os

restaurantes = []

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


def finalizar_app():
    os.system('clear')
    print('Saindo da Aplicação...\n')
    exit()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def cadastrar_novo_restaurante():
    print('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def opcao_invalida():
    print('Opção invalida\n')
    voltar_ao_menu_principal()
    
def escolher_opcoes():
    opcao_escolhida = int(input('Escolha uma opção:'))
    #opcao_escolhida = int(opcao_escolhida)
    match opcao_escolhida:
        case 1:
            cadastrar_novo_restaurante()
        case 2:
            print('Listar restaurantes')
        case 3:
            print('Ativar restaurantes')
        case 4:
            finalizar_app()
        case _:
            opcao_invalida()

def main():
    os.system('clear') # função que limpa a tela do terminal
    exibir_nome_do_programa() # função que controla o projeto
    exibir_opcoes()
    escolher_opcoes()

# .py posso informa que é o arquivo principal do programa
if __name__ == '__main__':
    main()