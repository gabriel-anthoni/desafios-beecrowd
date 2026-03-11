# beecrowd | 1025 | Onde está o Mármore?

# Entrada:
#   - Leia uma string.
#   - Leia alguns números inteiros que vão representar:
#     1. O tamanho de cada mármore
#     2. E o tamanho que se busca nos mármores.
#
# Lógica:
#   - Separe a string por espaços para obter dois números inteiros que representam:
#     1. quantos mármores o programa vai ler
#     2. quantos mármores o programa vai buscar
#   - Se na primeira string ambos os números forem 0, pare a execução do programa.
#   - Para cada mármore que o programa vai ler, receba o tamanho dele como um número inteiro e guarde
#     em uma lista.
#   - Organize a lista em ordem crescente (do menor para o maior).
#   - Para cada mármore que o programa vai buscar, procure na lista e retorne a posição
#     (leve em conta que a lista começa na posição 1).
#   - OBS: Utilize a biblioteca 'bisect' para analisar a lista a fim de evitar "Time Limit Exceeded".
#
# Saída:
#   - Imprima "CASE# X:", onde X é o caso da vez (1, 2, 3, ...).
#   - Para cada busca, o programa irá imprimir a posição do mármore encontrado
#     (leve em conta que a lista começa na posição 1)..

# Código:
import bisect

loop = 1
while True:
    marbles = []
    numbers = input().split()
    if numbers[0] == "0" and numbers[1] == "0":
        break
    for _ in range(int(numbers[0])):
        marbles.append(int(input()))
    print(f"CASE# {loop}:")
    marbles.sort()
    loop += 1
    for _ in range(int(numbers[1])):
        query = int(input())
        pos   = bisect.bisect_left(marbles, query)
        if pos < len(marbles) and marbles[pos] == query:
            print(f"{query} found at {pos+1}")
        else:
            print(f"{query} not found")