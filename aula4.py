# Laços de Repetição + Listas

print('carregando') # imprimindo a frase.
print('carregando') # imprimindo a frase.
print('carregando') # imprimindo a frase.

#existe uma maneira mas simples de fazer usando laço de repetição.

for palavra in range(1,4): # usando laço de repetição de 1 a 3.
    print('carregando') # imprimindo na tela a função acima.

'''
for item in coleção:
espressão
'''
for item in range(1,21): # usando laço de repetição de 1 a 20.
    print(item) # imprimindo na tela a função acima.

for item in range(1,20,2): # usando laço de repetição de 1 a 20, função pulando de 2 em 2.
    print(item) # imprimindo na tela a função acima.

    nomes = ['jhonatan , cristian , roberto , camila']
    for nome in nomes: # usando laço de repetição de nome,  obs: singular , e depois plural. podemos alterar apenas o nome como por exemplos, animal, aniversario, nomes e entre outros.
        print(nome) # imprimindo o na tela a função acima.
