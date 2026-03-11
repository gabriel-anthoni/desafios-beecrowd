# beecrowd | 1036 | Fórmula de Bhaskara
#
# Entrada:
#   - Leia uma string contendo três números de ponto flutuante: A, B e C.
#
# Lógica:
#   - Separe a string de entrada pelos espaços para obter os valores de A, B e C.
#   - Calcule o valor de delta: Δ = B² - 4AC.
#   - Se delta for menor que 0 ou A for igual a 0, imprima: "Impossivel calcular".
#   - Caso contrário, calcule as raízes R1 e R2:
#       R1 = (-B + √Δ) / (2 * A)
#       R2 = (-B - √Δ) / (2 * A)
#
# Saída:
#   - Imprima os resultados formatados com 5 casas decimais: "R1 = <valor>" e "R2 = <valor>".
#   - Caso as condições de erro sejam atingidas, imprima apenas: "Impossivel calcular".

# Código:
numbers = input().split()
a,b,c   = float(numbers[0]),float(numbers[1]),float(numbers[2])
delta   = ((b**2) - (4*a*c))
if ( a == 0 ) or ( delta < 0 ):
    print("Impossivel calcular")
else:
    print(f"R1 = {((-b + pow(delta,0.5))/(2*a)):.5f}\nR2 = {((-b - pow(delta,0.5))/(2*a)):.5f}")