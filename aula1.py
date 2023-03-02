# Métodos 5Q´s para montar um algoritimos:

#1° quais os dados de entrada necessario?
# R:salario mensal
#   horas trabalhadas

#2° o que devo fazer com estes dados?
#R: fazer uma divisão, salario mensal dividido pelo horas trabalhadas no mês.

#3° quais são as restrições deste problema?
#R: os valores devem ser entregues somente em formato de salarios por hora.

#4° Qual é o resultado esperado?
#R: O valor hora que o funcionario vai recebe.

#5° Qual e a sequência de passos a ser feitas para chegar ao resultado esperado?
#R: -pergunta quanto a pessoa ganha por mês
#   -guarda essa informação
#   -pergunta quantas horas elas trabalha por mes
#   -guarda essa informação
# calcular o valor hora da pessoa( salario mensal/horas trabalhadas)
#exibir o valor hora daquela pessoa.

#Escreva um programa que retorna o valor hora de um funcionario com base no seu salario mensal e horas trabalhadas por mês.

salario_mensal = input('qual é seu salario mensal?')# para o usuario colocar o valor
horas_trabalhadas_por_mes = input('quantas horas trabalha por mês?')# para o usuario colocar o valor
valor_hora = int(salario_mensal) / int(horas_trabalhadas_por_mes)# valor que o usuario digitou, porém feito a conversão para o numeró inteiro. pq nao da para soma 2 string.
print(valor_hora)# imprimir o resultado para o cliente.