'''
Função 1:
Escreva uma função que recebe do usuário
um valor por parâmetro  e printa no console
o tipo desse valor recebido.
'''

def check_inputed_type(value):
    value_type = type(value)
    print(value_type)
    # This function always return string

inputed_value = input('Insira alguma coisa:')
check_inputed_type(inputed_value)

'''
    Função 2:
    Escreva um array com números sequenciais
    e uma função que retorna o elemento do array
    com index 3.
'''

def index_return():
    sequence = [1, 2, 3, 4, 5, 6]
    print(sequence[3])

index_return()

'''
    Função 3:
    Escreva um algoritmo que possua um
    array shackle= [150, 250, 500, 750, 1000]
    e uma função que recebe do usuário um
    valor de capacidade e que esse valor
    seja removido do array shackle.
    Retorne o novo array com o item escolhido
    removido e caso o valor escolhido pelo usuário
    não esteja no array informe ao usuário!
'''

def remove_item():
    shackle = [150, 250, 500, 750, 1000]
    try:
        inputed_value = input('Digite um valor:')
        shackle.remove(inputed_value)
        print(shackle)
    except ValueError:
        print('Este valor não está no array')

remove_item()

'''
    Função 4:
    Escreva um algoritmo que possui dois
    arrays, um chamado amount e outro expenses.
    Solicite ao usuário a inserção de valores,
    podendo ser eles positivos ou negativos de forma
    que os valores positivos representem entradas e os
    valores negativos despesas. Exemplo:

    -35 #Despesas 
    1000 ou +1000 #Receitas

    Depois escreva uma função que faça com que valores
    positivos seja inseridos no array amount e valores
    negativos sejam inseridos no array expenses.
'''

amount = []
expenses = []

def wallet():
    finantial_value = eval(input('Insira valores:'))
    if finantial_value > 0:
        amount.append(finantial_value)
    elif finantial_value < 0:
        expenses.append(finantial_value)
    else:
        print('Digite um valor positivo ou negativo')

    print('Amount:', amount)
    print('Expenses:', expenses)
    
    wallet()

wallet()

'''
    Função 5:
    Uma faculdade com nota mínima de 70, armazena em uma lista linear as notas de uma turma de 30 alunos.
    tests_results = [100,70,65,85,89,95,99,30,20,10,35,67,55,59,54,78,84,97,60,50,49,25,80,75,96,100,74,80,60,78]

    Base:
    1 - Escreva um algorítimo que retorne a média geral da classe.
    2 - Retorne em novos arrays as notas que estão abaixo e acima do valor
    mínimo da faculdade assim como o numero de alunos em cada uma dessas listas.

    Desafio:
    3 - Retorne um novo array com as notas mínimas necessárias para que a média
    entre esse novos valores e o array de notas abaixo de 70 alcansem o esperado para passar.
'''

from functools import reduce
tests_results = [100,70,65,85,89,95,99,30,20,10,35,67,55,59,54,78,84,97,60,50,49,25,80,75,96,100,74,80,60,78]
minimum_grade = 70

#Helper Functions
def lower_range(item):
    return item < minimum_grade

def uper_range(item):
    return item > minimum_grade

def average_reducer(value, acumulator):
    return value + acumulator

def grade_compensation(lower_list):
    def map_function(item):
        return (minimum_grade * 2 ) - item

    minimal_point = list(map(map_function, lower_list))
    return minimal_point


#Main Function
def summarize_test():
    average_grade = (reduce(average_reducer, tests_results))/len(tests_results)
    print(f'[---Média da Turma: {average_grade}---]')

    uper_sample = list(filter(uper_range, tests_results))
    print(f'[---Alunos Acima da Mínima: {len(uper_sample)}---]')
    print(uper_sample)  

    lower_sample = list(filter(lower_range, tests_results))
    print(f'[---Alunos Abaixo da Mínima: {len(lower_sample)}---]')
    print(lower_sample)

    compensation_list = grade_compensation(lower_sample)
    print('[---Nota Mínima:---]')
    print(compensation_list)

summarize_test()