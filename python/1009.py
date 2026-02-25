# beecrowd | 1009 | Salário com Bônus

# Entrada: Leia uma string que representa o primeiro nome do vendedor, e 2
#          valores de ponto flutuante, nos quais o primeiro é o salário fixo e o
#          segundo é o total de vendas.
# Lógica:  Multiplique o total de vendas por 0.15 para calcular os 15% de bônus, e
#          some esses 15% ao salário fixo para obter o salário total.
# Saída:   Imprima o valor do salário total com 2 casas decimais, precedido do texto: "TOTAL = R$ ".

# Código:
name   = input()
salary = float(input())
bonus  = float(input())*0.15
print(f"TOTAL = R$ {(salary+bonus):.2f}")