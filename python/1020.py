# beecrowd | 1020 | Idade em Dias
#
# Entrada:
#   - Leia um número inteiro representando a quantidade total de dias.
#
# Lógica:
#   - Calcule a quantidade de anos, meses e dias correspondentes, considerando:
#       - 1 ano = 365 dias
#       - 1 mês = 30 dias
#   - Fórmulas:
#       - Anos:  anos  = DiasTotais // 365
#       - Meses: meses = (DiasTotais % 365) // 30
#       - Dias:  dias  = (DiasTotais % 365) % 30
#
# Saída:
#   - Imprima cada resultado em uma linha, na ordem: anos, meses e dias.
#   - Acrescente os textos correspondentes: "ano(s)", "mes(es)" e "dia(s)".

# Código:
totalDays = int(input())
years     = totalDays//365
months    = (totalDays%365)//30
days      = (totalDays%365)%30
print(f"{years} ano(s)\n{months} mes(es)\n{days} dia(s)")