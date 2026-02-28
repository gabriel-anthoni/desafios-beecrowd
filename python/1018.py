# beecrowd | 1018 | Cédulas
#
# Entrada:
#   - Leia um número inteiro representando um valor monetário em reais.
#
# Lógica:
#   - Determine quantas notas de cada valor são necessárias para formar o valor total.
#   - Comece pelas notas de maior valor (100, 50, 20, 10, 5, 2, 1) até as menores.
#
# Saída:
#   - Imprima o valor lido.
#   - Em seguida, para cada nota, imprima:
#         "{quantidade} nota(s) de R$ {valor},00"
#   - Cada linha deve indicar quantas notas de cada valor são usadas para compor o valor total.

# Código:
money = int(input())
bills = [100,50,20,10,5,2,1] 
print(money)
for bill in bills:
    print(f"{money//bill} nota(s) de R$ {bill},00")
    money %= bill
