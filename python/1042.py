# beecrowd | 1042 | Sort Simples
#
# Entrada:
#   - Leia uma string contendo três números inteiros.
#
# Lógica:
#   - Converta a string de entrada para uma lista de números inteiros.
#   - Crie uma cópia ordenada desses números para exibição crescente.
#   - Imprima os números em ordem crescente.
#   - Imprima uma linha em branco.
#   - Imprima a sequência original, conforme lida inicialmente.
#
# Saída:
#   - Os números ordenados seguidos pela sequência original na ordem de entrada.

# Código:
numbers = input().split()
numbers = [ int(number) for number in numbers ]
newNumbers = []
newNumbers.append(sorted(numbers))
for _ in range(len(newNumbers[0])):
    print(newNumbers[0][_])
print()
for _ in numbers:
    print(_)