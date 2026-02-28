# beecrowd | 1012 | Área
#
# Entrada:
#   - Leia uma linha contendo três números de ponto flutuante separados por espaço: A, B e C.
#
# Lógica:
#   - Separe a linha por espaços para obter os valores de A, B e C.
#   - Calcule as áreas conforme as fórmulas:
#       - Triângulo:   (A × C) / 2            → base = A, altura = C
#       - Círculo:     π × C²                 → raio = C, use π = 3.14159
#       - Trapézio:    ((A + B) × C) / 2      → base1 = A, base2 = B, altura = C
#       - Quadrado:    B²                     → lado = B
#       - Retângulo:   A × B                  → lados = A e B
#
# Saída:
#   - Imprima cada resultado com 3 casas decimais.
#   - Cada linha deve começar com o texto indicando a forma geométrica em **maiúsculas**, seguido de " = ".
#       - Exemplo: TRIANGULO = {resultado}

# Código:
string = input().split()
a,b,c  = float(string[0]),float(string[1]),float(string[2])
pi     = 3.14159
print(f"TRIANGULO: {((a*c)/2):.3f}\nCIRCULO: {(pi*(c**2)):.3f}\nTRAPEZIO: {(((a+b)*c)/2):.3f}\nQUADRADO: {(b**2):.3f}\nRETANGULO: {(a*b):.3f}")