# beecrowd | 1040 | Média 3
#
# Entrada:
#   - Leia uma string contendo quatro números de ponto flutuante (notas).
#
# Lógica:
#   - Separe a string em 4 numeros de ponto flutuante para obter a nota do aluno.
#   - Calcule a média ponderada das quatro notas (pesos: 2, 3, 4 e 1, respectivamente).
#   - Se a média for >= 7.0, o aluno está aprovado.
#   - Se a média for < 5.0, o aluno está reprovado.
#   - Se a média estiver entre 5.0 e 6.9, o aluno entra em exame:
#       - Leia a nota do exame.
#       - Recalcule a média final somando a média anterior com a nota do exame e dividindo por 2.
#       - Se a nova média for >= 5.0, o aluno é aprovado; caso contrário, reprovado.
#
# Saída:
#   - Imprima a média, a situação do aluno e, se houver exame, a nota e a média final.

# Código:
grades      = input().split()
n1,n2,n3,n4 = float(grades[0])*2,float(grades[1])*3,float(grades[2])*4,float(grades[3])
average     = (n1+n2+n3+n4)/10
print(f"Media: {(average):.1f}")
if(average >= 7):
    print("Aluno aprovado.")
elif(average < 5):
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exam = float(input())
    print(f"Nota do exame: {exam:.1f}")
    average = (average+exam)/2
    if(average >= 5):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {average:.1f}")