# beecrowd | 1019 | Conversão de Tempo

# Entrada: Leia um número inteiro que represente os segundos totais.
# Lógica:  Realize cálculos para obter as horas, minutos e segundos exatos:
#          - Segundos: SegundosTotais % 60
#          - Minutos:  (SegundosTotais // 60) % 60
#          - Horas:    SegundosTotais // 3600
# Saída:   Imprima cada cálculo na ordem: horas, minutos e segundos, separando cada um por: ":".

# Código:
totalSeconds = int(input())
seconds      = totalSeconds%60
minutes      = (totalSeconds//60)%60
hours        = totalSeconds//3600
print(f"{hours}:{minutes}:{seconds}")