# beecrowd | 1011 | Esfera

# Entrada: Leia 1 número inteiro que representa o raio da esfera.
# Lógica:  Use a fórmula: ((4/3) * pi * R³). Mas considere (atribua) para pi o valor:
#          3.14159.
# Saída:   Imprima o valor total do cálculo com 3 casas decimais, precedido do texto:
#          "VOLUME = ".

# Código:
r  = int(input())**3
pi = 3.14159
print(f"VOLUME = {((4/3)*pi*r):.3f}")