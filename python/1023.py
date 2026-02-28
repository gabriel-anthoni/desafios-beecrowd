# beecrowd | 1023 | Estiagem

# Entrada: 
#   - Leia um número inteiro que representa quantas casas existem na cidade. 
#   - Para cada casa, leia uma linha contendo dois números inteiros: 
#       1. Quantidade de pessoas que moram na casa.
#       2. Consumo total da casa.
#
# Lógica: 
#   - Se o número de casas for 0, encerre a execução.
#   - Para cada casa, calcule o consumo por pessoa dividindo o consumo total pela quantidade de pessoas.
#   - Se houver outra casa com o mesmo consumo por pessoa, some a quantidade de pessoas dessas casas.
#   - Ao final, calcule o consumo médio da cidade dividindo o consumo total de todas as casas pelo total de pessoas da cidade.
#   - OBS: Utilize a biblioteca 'sys' para leitura de entrada a fim de evitar "Time limit exceeded".
#
# Saída:
#   - Primeira linha: "Cidade# X:", onde X é o número da cidade (1, 2, 3, ...).
#   - Segunda linha: para cada consumo por pessoa presente na cidade, imprima "quantidade_pessoas-consumo_por_pessoa" 
#     separados por espaço, em ordem crescente de consumo por pessoa.
#   - Terceira linha: "Consumo medio: {media} m3.", onde {media} é o consumo médio truncado para duas casas decimais.
#   - Ao final, insira uma linha em branco.

# Código:
import sys

city = 1

while True:
    line = sys.stdin.readline()
    if not line:
        break

    houses = int(line.strip())
    if houses == 0:
        break

    total_people      = 0
    total_consumption = 0
    consumptions      = {}

    for _ in range(houses):
        line = sys.stdin.readline().strip()
        people, consumption = map(int, line.split())

        total_people      += people
        total_consumption += consumption

        avg = consumption // people
        consumptions[avg] = consumptions.get(avg, 0) + people

    print(f"Cidade# {city}:")
    city += 1

    for key in sorted(consumptions):
        print(f"{consumptions[key]}-{key}", end=" ")
    print()

    avg_consumption = (total_consumption * 100) // total_people
    avg_consumption = avg_consumption / 100

    print(f"Consumo medio: {avg_consumption:.2f} m3.")
    print()