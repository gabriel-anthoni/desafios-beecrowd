# beecrowd | 1013 | O Maior
#
# Entrada:
#   - Leia uma linha contendo três números inteiros separados por espaços: A, B e C.
#
# Lógica:
#   - Separe a linha por espaços para obter os três números.
#   - Determine qual dos três números é o maior.
#
# Saída:
#   - Imprima o maior número seguido do texto " eh o maior".

# Código:
numbers = input().split()
numbers = [ int(number) for number in numbers ]
if   numbers[0] > numbers[1] and numbers[0] > numbers[2]:
    print(f"{numbers[0]} eh o maior")
elif numbers[1] > numbers[2]:
    print(f"{numbers[1]} eh o maior")
else:
    print(f"{numbers[2]} eh o maior")