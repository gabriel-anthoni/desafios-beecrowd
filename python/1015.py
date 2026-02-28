# beecrowd | 1015 | Distância Entre Dois Pontos
#
# Entrada:
#   - Leia duas linhas contendo números de ponto flutuante:
#       1. Linha A: x1 y1
#       2. Linha B: x2 y2
#
# Lógica:
#   - Separe cada linha por espaços para obter os números correspondentes.
#       - Na linha A: x1 e y1
#       - Na linha B: x2 e y2
#   - Calcule a distância entre os dois pontos usando a fórmula da distância euclidiana:
#         distância = √((x2 - x1)² + (y2 - y1)²)
#
# Saída:
#   - Imprima a distância com 4 casas decimais.

# Código:
A     = input().split()
B     = input().split()
x1,y1 = float(A[0]),float(A[1])
x2,y2 = float(B[0]),float(B[1])
print(f"{pow(((x2-x1)**2)+((y2-y1)**2),0.5):.4f}")