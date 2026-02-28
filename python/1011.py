# beecrowd | 1011 | Esfera
#
# Entrada:
#   - Leia um número de ponto flutuante representando o raio da esfera.
#
# Lógica:
#   - Calcule o volume da esfera usando a fórmula:
#         volume = (4/3) * π * R³
#   - Considere π = 3.14159
#
# Saída:
#   - Imprima o resultado com 3 casas decimais, precedido do texto "VOLUME = ".

# Código:
r  = int(input())**3
pi = 3.14159
print(f"VOLUME = {((4/3)*pi*r):.3f}")