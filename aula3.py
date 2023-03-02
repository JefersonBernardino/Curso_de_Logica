# Encontre o maior entre 2 números

primeiro_valor = input('digite o 1°valor: ') # Variavel, com input para receber valor do cliente.
segundo_valor = input('digite o 2º valor:') # Variavel, com input para receber valor do cliente.

if int(primeiro_valor) > int(segundo_valor): # comparando o primeiro valor que for maior que o segundo valor. porém tem que transforma o numero de string para numero inteiro.
    print('O primeiro valor é maior') # imprimir  na tela caso o primeiro valor seja maior.
else:
    print('o segundo valor é  maior!') # imprimir na tela caso o IF Acima não seja executado.
