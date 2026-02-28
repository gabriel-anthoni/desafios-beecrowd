# beecrowd | 1005 | Média 2
#
# Entrada:
#   - Leia uma linha contendo três valores de ponto flutuante separados por espaço: A, B e C.
#     Cada valor representa a nota de um aluno.
#
# Lógica:
#   - Calcule a média ponderada das notas com os seguintes pesos:
#       - A: peso 2
#       - B: peso 3
#       - C: peso 5
#   - Fórmula:
#         MEDIA = ((A*2) + (B*3) + (C*5)) / 10
#
# Saída:
#   - Imprima o resultado da média com **uma casa decimal**, precedido do texto "MEDIA = ".

# Código:
a = float(input())*2
b = float(input())*3
c = float(input())*5
print(f"MEDIA = {((a+b+c)/10):.1f}")