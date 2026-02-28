# beecrowd | 1020 | Idade em Dias

# Entrada: Leia um número inteiro que represente os dias totais.
# Lógica:  Realize cálculos para obter os anos, meses e dias exatos
#          (considerando que cada mês dure 30 dias):
#          - Anos:  DiasTotais // 365
#          - Meses: (DiasTotais % 365) // 30
#          - Dias:  (DiasTotais % 365) % 30
# Saída:   Imprima cada cálculo na ordem: anos, meses e dias, separando cada um por uma quebra de linha.
#          Coloque os textos: "ano(s)", "mes(es)" e "dia(s)" na frente de cada resultado correspondente.

# Código:
totalDays = int(input())
years     = totalDays//365
months    = (totalDays%365)//30
days      = (totalDays%365)%30
print(f"{years} ano(s)\n{months} mes(es)\n{days} dia(s)")