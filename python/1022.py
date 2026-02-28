# beecrowd | 1022 | TDA Racional
#
# Entrada:
#   - Leia um número inteiro que representa quantas vezes o problema será repetido.
#   - Para cada repetição, leia uma linha contendo uma operação com duas frações no formato: "n1/d1 op n2/d2", 
#     onde n1, d1, n2, d2 são inteiros e op é um dos operadores: +, -, * ou /.
#
# Lógica:
#   1. Separe a string por espaços e pelos caracteres "/" para obter n1, d1, n2, d2 e o operador.
#   2. Calcule a operação entre as frações dependendo do operador:
#       - "+" : numerador = n1*d2 + n2*d1 | denominador = d1*d2
#       - "-" : numerador = n1*d2 - n2*d1 | denominador = d1*d2
#       - "*" : numerador = n1*n2         | denominador = d1*d2
#       - "/" : numerador = n1*d2         | denominador = n2*d1
#   3. Simplifique a fração resultante:
#       - Pegue o valor absoluto do numerador e denominador.
#       - Use o maior divisor comum (MDC) para simplificar.
#       - Divida numerador e denominador pelo MDC.
#
# Saída:
#   - Imprima a fração original e a fração simplificada, no formato:
#         numerador/denominador = numerador_simplificado/denominador_simplificado

# Código:
def fatora(numerator:int,denominator:int):
    newNumbers = [abs(numerator),abs(denominator)]
    minNumber  = min(newNumbers)
    maxNumber  = max(newNumbers)
    divisor    = minNumber
    while divisor > 1:
        if (minNumber % divisor) == 0:
            if (maxNumber % divisor) == 0:
                return int(numerator/divisor), int(denominator/divisor)
        divisor -= 1
    return numerator, denominator


loops = int(input())
for loop in range(loops):
    command = input().split()
    n1,d1,operator,n2,d2 = int(command[0]),int(command[2]),command[3],int(command[4]),int(command[6])
    match operator:
        case "+":
            numerator   = n1 * d2 + n2 * d1
            denominator = d1 * d2
        case "-":
            numerator   = n1 * d2 - n2 * d1
            denominator = d1 * d2
        case "*":
            numerator   = n1 * n2
            denominator = d1 * d2
        case "/":
            numerator   = n1 * d2
            denominator = n2 * d1
    simplification = fatora(numerator,denominator)
    print(f"{numerator}/{denominator} = {simplification[0]}/{simplification[1]}")