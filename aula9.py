'''
1- Quais são os Dados de entrada necessário?
R: valor aleatorio de 1 a 10
   chute do usuário
2- O que devo fazer com esses dados?
R: Eu devo comparar o chute do usúario com o valor aleatório que foi gerado no início do programa e dizer se o chute foi maior, menor ou igual ao valor que foi gerado no inicio do programa.

3- Quais são as Restrições deste problema?
R: O valor aleátorio de 1 a 10

4- Qual é o resultado esperado?
R: O resultado esperado é que o programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa.

5- Qual é sequência de passos a ser feitas para chegar ao resultado esperado?
R:  input valor_aleatório de 1 a 10
    input chute
    if chute > valor aleatorio
    print ''chute foi maior que o valor gerado''
    if chute < valor aleatório
    print ''chute foi menor que o valor gerado''
    if chute = valor_aleatorio
    print ''você acertou!''
'''

# import random fazer importação da biblioteca no python.

# Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuário
# chute o número até  que o valor aleatório gerado no inicio do programa seja chutado corretamente.

'''
import random # Para fazer um valor Aleatório no python, Precisamos importa da biblioteca.

valor_aleatorio = random.randint (1,10) #Variavel com o numero inteiro gerado na biblioteca.
chute = int(input('Chute um Valor de 1 a 10')) # String com o Chute do usúario, e convertido para número inteiro.
if chute > valor_aleatorio: # chute do usúario maior que o valor_aleatorio gerado na biblioteca.
    print('chute foi maior que o valor gerado') # imprimir resposta acima.
elif chute < valor_aleatorio: # chute do usúario menor que o valor_aleatorio gerado na biblioteca.
    print('Chute foi menor que o valor gerado') # imprimir resposta acima.
elif chute == valor_aleatorio: # Valor igual do valor aleatório.
    print('Você acertou!') # Imprimir você Acertou!
'''
# Laço While - Erro Infinito

'''
import random

valor_aleatorio = random.randint (1,10 )
chute = int(input('Chute um Valor de 1 a 10'))
acertou = False
while acertou == False:
    if chute > valor_aleatorio:
        print('chute foi maior que o valor gerado')
    elif chute < valor_aleatorio:
        print('Chute foi menor que o valor gerado')
    elif chute == valor_aleatorio:
        acertou = True
        print('Você acertou!')
'''
# Para evitar esse Bug inifito

import random

valor_aleatorio = random.randint (1,10)
acertou = False
while acertou == False:
    chute = int(input('Chute um Valor de 1 a 10: '))# Tira ela de cima e colocar ela dentro do seu laço de repetição.
    if chute > valor_aleatorio:
        print('chute foi maior que o valor gerado')
    elif chute < valor_aleatorio:
        print('Chute foi menor que o valor gerado')
    elif chute == valor_aleatorio:
        acertou = True
        print('Você acertou!')