# condicionais
# If - Condicional que controla se algo deve ou não ser feito.
# Elif - Só é executado caso o IF acima deles não seja executado.
# Else - cláusula a ser executada caso nenhuma condicional IF seja executada.
#''' - Blocos de notas
'''
E ae jhonatan, bora dar uma saida hoje?
se eu terminar meu trabalho aqui, eu consigo.
'''

# Cenario verdadeiro.
trabalho_terminado = True # variavel atendida como True 'verdadeira'
if trabalho_terminado == True: # if comparado usando dois iguais, vai compara a situação True e False.
    print('Opa! Bora dar uma saida.') # Imprimir resultado caso for verdadeira
else: # cláusula a ser executada caso nenhuma condicional IF seja executada, mas nesse caso ela foi.
    print('Não posso sair agora.') # imprimir resultado caso fosse False.

# Cenario Falso
trabalho_terminado = False # Variavel atendida como False 'falsa'
if trabalho_terminado == True: # if comparado usado dois iguais, vai compara a situação True e False.
    print('Opa! Bora dar uma saida.') # Imprimir resultado caso fosse verdadeira.
else: # cláusula a ser executada caso nenhuma condicional IF seja executada
    print('Não posso sair agora.') # Imprimir a frase porque foi falso.

'''
Ei, você consegue me ajudar a mover essas caixas lá para fora hoje a tarde?
se eu estiver livre, sim. Mas, se não der pede  meu irmão para te ajudar
'''
# Cenario peça ao meu irmão te ajudar
estou_livre = False # variavel False
if estou_livre == True: # compara if com a variavel Estou_livre para saber se é verdadeira ou falsa.
    print('Ok, posso ajudar hoje sim') # imprimir a frase caso a variavel batesse com a comparação.
else: # cláusula foi executada porque o IF era verdadeiro
    print('peça o meu irmão para te ajudar') # imprimir a frase porque foi executada a cláusula ELSE

# Cenario estou livre, posso te ajudar hoje sim.
estou_livre = True # Variavel estou livre
if estou_livre == True: # comparando variavel_livre e são verdadeira.
    print('Ok, posso ajudar hoje sim') # Imprimir frase porque a variavel bate com a comparação.
else: # cláusula não foi executada porque o IF foi verdadeiro.
    print('peça o meu irmão para te ajudar') # Imprimir caso a Variavel esou_livre fosse Falsa.

'''
Eu cheguei atrasado na aula, ainda posso entrar?
se  essa nao for sua terceira vez chegando atrasado, então pode sim, caso contrario irá tomar uma suspensão.
'''
numero_de_atrasos = 2 # Variavel numero_de_atrasos
if numero_de_atrasos >= 3:
    print('Você está suspenso') # imprimir  comparado com a linha acima IF
elif numero_de_atrasos ==1:
    print('pode entrar, porém caso tome 2 faltas, irá ser suspenso') # imprimir  comparado com a linha acima IF
elif numero_de_atrasos ==2:
    print('pode entrar, porém caso tome mais 1 falta, irá ser suspenso') # imprimir  comparado com a linha acima IF, no caso ele vai imprimir essa frase.
else:
    print('pode entrar') # cláusula a ser executada caso nenhuma condicional IF e ELIF seja executada.
    




