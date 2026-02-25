# beecrowd | 1008 | Salário

# Entrada: Leia 2 valores inteiros, nos quais o primeiro representa o número do
#          funcionário e o outro a quantidade de horas trabalhadas, e 1 valor de
#          ponto flutuante que representa o ganho por hora trabalhada.
# Lógica:  Multiplique o ganho por hora trabalhada pela quantidade de horas
#          trabalhadas.
# Saída:   Imprima o número do funcionário, precedido do texto: "NUMBER = ", e o
#          resultado do cálculo de horas trabalhadas com 2 casas decimais, precedido do texto:
#          "SALARY = U$ ".

# Código:
number      = int(input())
hoursWorked = int(input())
salary      = float(input())*hoursWorked
print(f"NUMBER = {number}\nSALARY = U$ {salary:.2f}")