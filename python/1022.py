# beecrowd | 1022 | TDA Racional

# Entrada: Leia um número inteiro que represente quantas vezes o problema irá se repetir e,
#          para cada repetição, leia uma string.
# Lógica:  Separe a string por espaço e "/" para obter 4 números (n1, d1, n2, d2) e o operador
#          do cálculo. Caso o operador seja:
#          - "+" o cálculo deve ser: numerador = n1 * d2 + n2 * d1 | denominador = d1 * d2
#          - "-" o cálculo deve ser: numerador = n1 * d2 - n2 * d1 | denominador = d1 * d2
#          - "*" o cálculo deve ser: numerador = n1 * n2 | denominador = d1 * d2
#          - "/" o cálculo deve ser: numerador = n1 * d2 | denominador = n2 * d1
#          Depois, simplifique o resultado (numerador e denominador). Para isso, pegue o
#          valor absoluto dos dois números, sendo o divisor o menor entre eles. Em seguida,
#          faça um loop até que o divisor seja menor ou igual a 1. Dentro do loop, calcule
#          o módulo entre o divisor e o menor número. Se não for 0, diminua o divisor.
#          Se for 0, verifique se o divisor também é divisor do outro número. Se for de ambos,
#          retorne os dois números divididos pelo divisor. Caso o divisor chegue a 1 e o loop
#          termine, retorne os dois números originais sem modificação.
# Saída:   Imprima os valores do numerador e do denominador separados por "/" para formar
#          a fração e também imprima o numerador e o denominador simplificados da mesma
#          forma, separados por " = ".

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