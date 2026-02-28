# beecrowd | 1017 | Gasto de Combustível
#
# Entrada:
#   - Leia dois números inteiros:
#       1. Horas gastas na viagem
#       2. Velocidade média durante a viagem (km/h)
#
# Lógica:
#   - Considere que o carro consome 1 litro de combustível a cada 12 km.
#   - Para calcular o combustível gasto:
#       - Multiplique a velocidade média pelo tempo da viagem para obter a distância percorrida.
#       - Divida a distância por 12 para obter o total de litros consumidos.
#
# Saída:
#   - Imprima a quantidade de combustível gasto com 3 casas decimais.

# Código:
travelHours  = int(input())
AverageSpeed = int(input())*travelHours
print(f"{(AverageSpeed/12):.3f}")