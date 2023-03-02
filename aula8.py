# Crie um programa que recebe um número e imprime o seu fatorial.

# Método 5Q's para montar um algorítimo:

''' Analise criticamente o problema e descubra:
(tente explicar este problema para você comprrender completamente o problema.)

1- Quais são os Dados de entrada necessário?
R: número.

2- O que devo fazer com esses dados?
R: eu deveo calcular o fatorial do número que for passado para o meu programa  e o exibir na tela.

3- Quais são as Restrições deste problema?
R: - O Número deve ser um valor positivo.
   - O Número deve ser um valor inteiro.

4- Qual é o resultado esperado?
R: O resultado esperado é  que o fatorial do número providenciado seja exibido.

5- Qual é sequência de passos a ser feitas para chegar ao resultado esperado?
R:  -input numero
    -if numero > 0
    -if numero= inteiro
    fatorial = 1
    loop de 1 a numero
    fatorial = fatorial * número
    print(fatorial)
    '''

numero = int(input('Digite um Número'))# Numero digitado em string e ja convertendo ele em inteiro.
if numero > 0: # Número maior que 0, que no caso ja é numero inteiro.
    fatorial = 1 # O resultado da multiplicações vai iniciar com 1.
    for item in range(1,numero + 1): # laço iniciando do 1 até o numero digitado pelo usúario, e no final +1 para chegar ao valor que o usuario digitol.
        fatorial = fatorial * item # vai iniciar no fatorial 1 até o numero gerado no item.
print(fatorial) # Imprimindo o resultado da função acima.