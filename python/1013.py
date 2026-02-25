# beecrowd | 1013 | O Maior

# Entrada: Leia 1 string.
# Lógica:  Separe a string por espaços para obter 3 números (A, B e C) e analise
#          qual dos 3 números é o maior.
# Saída:   Imprima o maior número com o texto à frente: " eh o maior".

# Código:
numbers = input().split()
numbers = [ int(number) for number in numbers ]
if   numbers[0] > numbers[1] and numbers[0] > numbers[2]:
    print(f"{numbers[0]} eh o maior")
elif numbers[1] > numbers[2]:
    print(f"{numbers[1]} eh o maior")
else:
    print(f"{numbers[2]} eh o maior")