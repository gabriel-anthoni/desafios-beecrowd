# beecrowd | 1005 | Média 1
#
# Entrada:
#   - Leia uma linha contendo dois valores de ponto flutuante separados por espaço: A e B.
#     Cada valor representa a nota de um aluno.
#
# Lógica:
#   - Calcule a média ponderada das notas com os seguintes pesos:
#       - A: peso 3.5
#       - B: peso 7.5
#   - Fórmula:
#         MEDIA = ((A*3.5) + (B*7.5)) / 11
#
# Saída:
#   - Imprima o resultado da média com **5 casas decimais**, precedido do texto "MEDIA = ".

# Código:
a = float(input())*3.5
b = float(input())*7.5
print(f"MEDIA = {((a+b)/11):.5f}")