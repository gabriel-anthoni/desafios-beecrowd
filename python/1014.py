# beecrowd | 1014 | Consumo

# Entrada: Leia 1 número inteiro que representa a distância total
#          percorrida (em km) e 1 número de ponto flutuante que representa
#          o total de combustível gasto (em litros).
# Lógica:  Divida a distância total pelo total de combustível gasto.
# Saída:   Imprima o resultado da divisão com o texto à frente: " km/l".

# Código:
totalDistance = int(input())
fuelConsumed  = float(input())
print(f"{(totalDistance/fuelConsumed):.3f} km/l")