# beecrowd | 1010 | Salário com Bônus
#
# Entrada:
#   - Leia duas linhas, cada uma representando um produto:
#       1. Cada linha contém três valores separados por espaço:
#          - Código do produto (inteiro)
#          - Quantidade do produto (inteiro)
#          - Valor unitário do produto (ponto flutuante)
#
# Lógica:
#   - Para cada produto, multiplique a quantidade pelo valor unitário.
#   - Some o valor total dos dois produtos para obter o valor final a pagar.
#
# Saída:
#   - Imprima o valor total, precedido do texto "VALOR A PAGAR: R$ ".
#   - Formate o valor com duas casas decimais.

# Código:
a = input().split()
b = input().split()
a[0],a[1],a[2] = int(a[0]),int(a[1]),float(a[2])
b[0],b[1],b[2] = int(b[0]),int(b[1]),float(b[2])
print(f"VALOR A PAGAR: R$ {(a[1]*a[2])+(b[1]*b[2]):.2f}")