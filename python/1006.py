# beecrowd | 1005 | Média 2

# Entrada: Leia 3 valores (A, B e C) de ponto flutuante que representam as notas
#          do aluno.
# Lógica:  Multiplique a nota A por 2, a nota B por 3 e a nota C por 5. Depois,
#          some os resultados e divida por 10.
# Saída:   Imprima o resultado do cálculo com 1 casa decimal, precedido do texto:
#          "MEDIA = ".

# Código:
a = float(input())*2
b = float(input())*3
c = float(input())*5
print(f"MEDIA = {((a+b+c)/10):.1f}")