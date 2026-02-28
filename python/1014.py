# beecrowd | 1014 | Consumo
#
# Entrada:
#   - Leia dois valores:
#       1. Um número inteiro representando a distância total percorrida em quilômetros.
#       2. Um número de ponto flutuante representando o total de combustível gasto em litros.
#
# Lógica:
#   - Calcule o consumo médio de combustível dividindo a distância total pelo total de litros gastos:
#         consumo = distância / combustível
#
# Saída:
#   - Imprima o resultado da divisão seguido do texto " km/l".
#   - Formate o resultado com 3 casas decimais, conforme exigido pelo problema.

# Código:
totalDistance = int(input())
fuelConsumed  = float(input())
print(f"{(totalDistance/fuelConsumed):.3f} km/l")