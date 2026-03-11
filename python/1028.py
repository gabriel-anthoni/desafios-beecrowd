# beecrowd | 1028 | Figurinhas

# Entrada: 
#   - Leia um número inteiro que representa quantas vezes o programa vai ler uma linha e retornar uma resposta. 
#   - Leia uma string.
#
# Lógica: 
#   - Separe a string por espaços para obter dois números inteiros, f1 e f2.
#   - Encontre o maior divisor comum entre esses dois números.
#     Maior divisor comum: é o maior número que divide ambos sem deixar resto.
#     Exemplos:
#       - No número 12, os divisores são: [1, 2, 3, 4, 6, 12]
#       - No número 8,  os divisores são: [1, 2, 4, 8]
#       - O maior divisor que os dois números têm em comum é 4.
#
# Saída:
#   - Retorne o maior divisor comum entre os dois números.

# Código:
import math

lines = int(input())
for _ in range(lines):
    cards    = input().split()
    f1       = int(cards[0])
    f2       = int(cards[1])
    print(math.gcd(f1, f2))