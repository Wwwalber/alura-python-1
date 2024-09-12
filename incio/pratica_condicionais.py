# prática: condicionais
#
#
    # 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura 
    # if else para determinar se o número é par ou ímpar.
def testa_número():
    numero_inserido = int(input('Insira um número: '))
    if numero_inserido % 2 == 0:
        print(f'{numero_inserido} é par')
    else:
        print(f'{numero_inserido} é ímpar')

def verifica_idade():
    # 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura 
    # if elif else para classificar a idade em categorias de acordo com as seguintes 
    # condições:
    # - Criança: 0 a 12 anos: criança
    # - Adolescente: 13 a 18 anos
    # - Adulto: acima de 18 anos.
    idade = int(input('Qual sua idade? '))
    if idade <= 12:
        print('Você é uma criança')
    elif idade <= 18:
        print('Você é um adolescente')
    else:
        print('Você é um adulto')

def logar():
        # 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar 
        # se o nome de usuário e a senha fornecidos correspondem aos valores esperados 
        # determinados por você.
    print('Seu usuário é: ironman')
    print('Sua senha é: 123456')
    print('******* Vamos tentar logar *******')
    usuario = input('Forneça o nome de usuário: ')
    senha = input('Forneça a senha: ')
    if usuario == 'ironman' and senha == '123456':
        print('Login efetuado com sucesso!')
    else:
        print('Login inválido!')
def determina_quadrante():
        # Solicita ao usuário as coordenadas (x, y) do ponto
    x = float(input("Digite a coordenada x: "))
    y = float(input("Digite a coordenada y: "))

    # Determina em qual quadrante o ponto se encontra
    if x > 0 and y > 0:
        print("O ponto está no Primeiro Quadrante.")
    elif x < 0 and y > 0:
        print("O ponto está no Segundo Quadrante.")
    elif x < 0 and y < 0:
        print("O ponto está no Terceiro Quadrante.")
    elif x > 0 and y < 0:
        print("O ponto está no Quarto Quadrante.")
    else:
        print("O ponto está localizado no eixo ou na origem.")


def main():
    #testa_número()
    #verifica_idade()
    #logar()
    determina_quadrante()

if __name__ == '__main__':
    main()


