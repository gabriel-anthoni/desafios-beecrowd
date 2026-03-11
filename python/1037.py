# beecrowd | 1037 | Intervalo
#
# Entrada:
#   - Leia um número de ponto flutuante (float).
#
# Lógica:
#   - Verifique em qual dos intervalos a seguir o número se encontra:
#       1. [0, 25]: Se o valor estiver entre 0 e 25 (inclusive).
#       2. (25, 50]: Se o valor for maior que 25 e menor ou igual a 50.
#       3. (50, 75]: Se o valor for maior que 50 e menor ou igual a 75.
#       4. (75, 100]: Se o valor for maior que 75 e menor ou igual a 100.
#   - Caso o valor não esteja em nenhum desses intervalos, classifique como "Fora de intervalo".
#
# Saída:
#   - Imprima a mensagem correspondente ao intervalo detectado.

# Código:
Range = float(input())
if   ( ( Range >= 0 ) and ( Range <= 25 )  ):
    print("Intervalo [0,25]")
elif ( ( Range > 25 ) and ( Range <= 50 )  ):
    print("Intervalo (25,50]")
elif ( ( Range > 50 ) and ( Range <= 75 )  ):
    print("Intervalo (50,75]")
elif ( ( Range > 75 ) and ( Range <= 100 ) ):
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")