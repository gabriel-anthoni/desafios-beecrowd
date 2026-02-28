# beecrowd | 1007 | Diferença
#
# Entrada:
#   - Leia uma linha contendo quatro números inteiros separados por espaço: A, B, C e D.
#
# Lógica:
#   - Calcule a diferença entre o produto de A e B e o produto de C e D:
#         diferenca = (A * B) - (C * D)
#
# Saída:
#   - Imprima o resultado do cálculo precedido do texto "DIFERENCA = ".

# Código:
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(f"DIFERENCA = {(( a * b ) - ( c * d ))}")