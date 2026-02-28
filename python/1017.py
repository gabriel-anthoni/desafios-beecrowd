# beecrowd | 1017 | Gasto de Combustível

# Entrada: Leia 2 números inteiros, sendo:
#          - o primeiro: horas gastas na viagem
#          - o segundo: velocidade média durante a viagem
# Lógica:  Divida a velocidade média por 12 e multiplique pelo número
#          de horas para calcular o combustível gasto.
# Saída:   Imprima o resultado com 3 casas decimais.

# Código:
travelHours  = int(input())
AverageSpeed = int(input())/12
print(f"{(AverageSpeed*travelHours):.3f}")