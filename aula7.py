print('Curso Introdução a programação com python') # Estou escrevendo a introdução do curso na saida.

a= int(input('entre com o primeiro valor:')) #
b= int(input('entre com o segundo valor:'))
print(type(a))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

resultado= (f'soma: {soma}. \nsubtracao: {subtracao}. '
      f'\nmulticação: {multiplicacao}'
      f'\ndivisão: {divisao}'
      '\nresto: (resto)'.format(soma=soma,
                                sub=subtracao,
                                resto=resto,
                                multiplicacao=multiplicacao,
                                divisao=divisao))
print(resultado)