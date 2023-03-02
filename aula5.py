# Laços de Repetição + listas
# Problema 1a N - imprime os valores de 1 a N

'''
Input número maximo
valor inicial = 1
loop de valor_inicial a numero_maximo
print valor
'''

valor_maximo = int(input('Digite o valor máximo')) # solicitando ao CLiente um valor em String e convertendo para numero inteiro.
valor_inicial = 1 # valor inicial que vai iniciar a contagem.
for numero in range(valor_inicial,valor_maximo + 1): # laço de repetição usando a  função range que pode roda por uma quantidade de vezes e lembrando que para chegar no valor final precisamos colocar +1 no final.
    print(numero) # imprimindo o resultado.