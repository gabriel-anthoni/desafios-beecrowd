# beecrowd | 1009 | Salário com Bônus
#
# Entrada:
#   - Leia uma linha contendo três valores separados por espaço:
#       1. Nome do vendedor (string)
#       2. Salário fixo (ponto flutuante)
#       3. Total de vendas realizadas (ponto flutuante)
#
# Lógica:
#   - Calcule 15% do total de vendas para obter o bônus.
#   - Some o bônus ao salário fixo para obter o salário total.
#
# Saída:
#   - Imprima o salário total com 2 casas decimais, precedido do texto "TOTAL = R$ ".

# Código:
name   = input()
salary = float(input())
bonus  = float(input())*0.15
print(f"TOTAL = R$ {(salary+bonus):.2f}")