# beecrowd | 1008 | Salário
#
# Entrada:
#   - Leia três valores separados por espaço:
#       1. Número do funcionário (inteiro)
#       2. Quantidade de horas trabalhadas (inteiro)
#       3. Valor ganho por hora (ponto flutuante)
#
# Lógica:
#   - Calcule o salário multiplicando a quantidade de horas pelo valor ganho por hora.
#
# Saída:
#   - Imprima duas linhas:
#       1. "NUMBER = {numero_do_funcionario}"
#       2. "SALARY = U$ {salario:.2f}"
#   - O salário deve ser formatado com 2 casas decimais.

# Código:
number      = int(input())
hoursWorked = int(input())
salary      = float(input())*hoursWorked
print(f"NUMBER = {number}\nSALARY = U$ {salary:.2f}")