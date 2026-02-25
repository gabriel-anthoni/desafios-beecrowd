# beecrowd | 1005 | Média 1

# Entrada: Leia 2 valores (A e B) de ponto flutuante que representam as notas
#          do aluno.
# Lógica:  Multiplique a nota A por 3.5 e a nota B por 7.5. Depois, some os
#          resultados e divida por 11.
# Saída:   Imprima o resultado do cálculo com 5 casas decimais, precedido do texto:
#          "MEDIA = ".

# Código:
a = float(input())*3.5
b = float(input())*7.5
print(f"MEDIA = {((a+b)/11):.5f}")