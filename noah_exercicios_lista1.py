# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)
lista1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("-" *70)

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
lista2 = ("roblox", "minecraft", "valorant", "brawhalla", "counter strike")
print(lista2)

print("-" *70)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
string1 = "Roblox eh "
string2 = "uma plataforma"
string3 = (string1 + string2)
print(string3)

print("-" *70)

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
tupla = (1, 2, 2, 3, 4, 4, 4, 5)
count = tupla.count(4)
print(count)

print("-" *70)

# Exercício 5 - Crie um dicionário vazio e imprima na tela
dict_vazio = {}
print(dict_vazio)

print("-" *70)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
idades = {"jose": 15, "enzo": 18, "maria": 20}
print(idades)

print("-" *70)

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
idades["bernardo"] =  16
print(idades)

print("-" *70)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.
lista = (1, 2)
objetos = {"carrinhos": 3, "bonecos": 4, "canetas": lista}
print(objetos)

print("-" *70)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.
string4 = "boa tarde"
tupla4 = (1,2)
dicionario4 = {"terra": 4, "marte": 5}
float = 4.2
lista4 = (string4, tupla4, dicionario4, float)
print(lista4)

print("-" *70)

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o melhor profissional do século XXI'
print(frase[1:18])