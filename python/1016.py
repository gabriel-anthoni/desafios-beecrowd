# beecrowd | 1016 | Distância
#
# Entrada:
#   - Leia um número inteiro representando a distância em quilômetros entre dois carros.
#
# Lógica:
#   - Cada carro se move a 60 km/h e 90 km/h, ou seja, a diferença entre eles é de 30 km/h.
#   - Para calcular o tempo que levarão para se encontrarem:
#       - Basta dobrar o número da entrada (distância / diferença de velocidade * 60) → neste caso simplificado, é só multiplicar por 2.
#
# Saída:
#   - Imprima o resultado seguido do texto " minutos".

# Código:
x = int(input())
print(f"{x*2} minutos")