# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade
pessoa = {'nome':'João', 'idade':45, 'cidade': 'Belém'}
print(pessoa)

pessoa['idade'] = 25

# Adicione um campo de profissão para essa pessoa;
pessoa['profissão'] = 'Garçon'
pessoa['e-mail'] = 'abc@abc.com'
print(pessoa)
# remova um intem, e-mail por exemplo
del pessoa['e-mail']

print(pessoa)

# 3 - Crie um dicionário utilizando para representar números e seus quadrados de
quadrado_de_numeros = {}
for numero in range(1,30):
    quadrado_de_numeros[numero] = numero**2
print(quadrado_de_numeros)

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário
chave_procurada = 'idade'
print(chave_procurada in pessoa)

chave2_procurada = 20
print(chave2_procurada in quadrado_de_numeros)

frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)