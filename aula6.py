# Coleções (lista)

preco_1 = 20
preco_2 = 50
preco_3 = 200
#lista
precos = [20,50,200]
#         0, 1 , 2
print(precos[0])
print(precos.index(200)) # solicito para o python descobrir e ir para lista de indice de algum projeto.

#diversidades
diversidades = [15 , ' Jeferson ' , True]
print(diversidades[0]) # imprimindo individualmente
print(diversidades[1]) # imprimindo individualmente
print(diversidades[2]) # imprimindo individualmente

#Laçocs iteráveis

for preco in precos: # imprimindo em coleção.
    print(preco)# imprimindo a função acima.

# Exemplo 5 - Some  os valores Dados uma coleção de dados 'idades' [15,46,75,34,23], imprima na tela a soma deste valores.

idades = [15,46,75,34,23]
total = 0
for idade in idades:
    total = total + idade
print(total)