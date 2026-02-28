# beecrowd | 1019 | Conversão de Tempo
#
# Entrada:
#   - Leia um número inteiro representando a quantidade total de segundos.
#
# Lógica:
#   - Converta os segundos totais em horas, minutos e segundos:
#       - Horas:    horas    = SegundosTotais // 3600
#       - Minutos:  minutos  = (SegundosTotais // 60) % 60
#       - Segundos: segundos = SegundosTotais % 60
#
# Saída:
#   - Imprima o resultado no formato "horas:minutos:segundos".
#   - Cada valor deve aparecer na ordem correta e separado por dois pontos ":".

# Código:
totalSeconds = int(input())
seconds      = totalSeconds%60
minutes      = (totalSeconds//60)%60
hours        = totalSeconds//3600
print(f"{hours}:{minutes}:{seconds}")