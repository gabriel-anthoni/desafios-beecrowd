# beecrowd | 1026 | Carrega ou não Carrega?

# Entrada:
#   - Leia uma string.
#
# Lógica:
#   - Separe a string por espaços para obter dois números inteiros.
#   - Transforme os números em binário e faça a soma deles em binário.
#     Soma em binário:
#         (2) 010
#         (7) 111
#         ---------
#         (5) 101
#   - No final, transforme a soma binária em um número inteiro.
#
# Saída:
#   - Retorne o número inteiro da soma dos binários.

# Código:
while True:
    try:
        numbers = input().split()
        numbers = [ int(str(bin(int(number)))[2:]) for number in numbers ]
        bitsum  = map(int,list(str(numbers[0]+numbers[1])))
        bits    = ""
        for bit in bitsum:
            if bit == 1:
                bits += "1"
            else:
                bits += "0"
        print(int(bits,2))
    except EOFError:
        break