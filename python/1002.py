# beecrowd | 1002 | Área do Círculo
#
# Entrada:
#   - Leia um valor de ponto flutuante representando o raio do círculo.
#
# Lógica:
#   - Calcule a área do círculo usando a fórmula:
#         área = π * R²
#   - Considere π = 3.14159
#
# Saída:
#   - Imprima o resultado da área com 4 casas decimais, precedido do texto "A=".

# Código:
raio = float(input())
pi   = 3.14159
area = pi*(raio**2)
print(f"A={area:.4f}")