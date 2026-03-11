# beecrowd | 1035 | Teste de Seleção 1
#
# Entrada:
#   - Leia uma string contendo quatro números inteiros: A, B, C e D.
#
# Lógica:
#   - Separe a string de entrada pelos espaços para obter os valores de A, B, C e D.
#   - Verifique se as seguintes condições são atendidas:
#       1. B é maior que C.
#       2. D é maior que A.
#       3. A soma de C e D é maior que a soma de A e B.
#       4. C é um número positivo.
#       5. D é um número positivo.
#       6. A é um número par.
#   - Se todas as condições forem verdadeiras, imprima: "Valores aceitos".
#   - Caso contrário, imprima: "Valores nao aceitos".
#
# Saída:
#   - Imprima a mensagem correspondente ao resultado da verificação das condições.

# Código:
numbers = input().split()
a,b,c,d = int(numbers[0]),int(numbers[1]),int(numbers[2]),int(numbers[3])
if ( b>c ) and ( d>a ) and ( (c+d)>(a+b) ) and ( c>0 ) and ( d>0 ) and ( (a%2) == 0 ):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")