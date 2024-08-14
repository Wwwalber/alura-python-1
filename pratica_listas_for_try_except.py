# 1 - Crie uma lista para cada informação a seguir:

#Lista de números de 1 a 10;
numeros = []
for i in range(1, 11):
    numeros.append(i)
print(numeros)
# print em órdem decrescente
numeros.sort(reverse=True)
print(numeros)

#Lista com quatro nomes;
nome = []
nome.append('Maria')
nome.append('João')
nome.append('Pedro')
nome.append('Ana')
print(nome)

#Lista com o ano que você nasceu e o ano atual.
ano_nascimento = 1991
ano_atual = 2023
ano = []
ano.append(ano_nascimento)
ano.append(ano_atual)
print(ano)

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma_impares = 0
for i in range(1,11):
    if i % 2 != 0:
        soma_impares += i
print(f'Soma dos números ímpares de 1 a 10: {soma_impares}')

# 3b 
for i in range(10, 0, -1):
    print(i)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
numero = int(input('Digite um número: '))
for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
lista = [1, 2, 3, 4, 5]
soma = 0
try:
    for numero in lista:
        soma += numero
    print(f'Soma dos elementos da lista: {soma}')
except Exception as e:
    print(f"Ocorreu um erro: {e}")


# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
lista_valores = [1, 2, 3, 4, 5]
soma_valores = 0
try:
    for numero in lista_valores:
        soma_valores += numero
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print('A lista está vazia.')
except Exception as e:
    print(f"Ocorreu um erro: {e}")