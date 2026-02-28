# beecrowd | 1021 | Notas e Moedas
#
# Entrada:
#   - Leia um número de ponto flutuante representando um valor monetário.
#
# Lógica:
#   - Determine quantas notas e moedas de cada valor são necessárias para formar esse valor.
#   - Comece pelas notas de maior valor até as menores.
#   - Depois, faça o mesmo para as moedas.
#   - OBS: Cuidado com erros de precisão ao lidar com moedas de R$ 0,01 devido ao ponto flutuante.
#
# Saída:
#   - Imprima o valor lido no formato: "R$ {valor:.2f}".
#   - Em seguida, para cada nota, imprima:
#         "{quantidade} nota(s) de R$ {valor:.2f}"
#   - E para cada moeda, imprima:
#         "{quantidade} moeda(s) de R$ {valor:.2f}"
#   - A saída deve listar todas as notas e moedas necessárias para compor o valor.

# Código:
money  = float(input())
bills  = [100.0,50.0,20.0,10.0,5.0,2.0]
coins = [1.0,0.50,0.25,0.10,0.05]
print("NOTAS:")
for bill in bills:
    print(f"{int(money/bill)} nota(s) de R$ {bill:.2f}")
    money %= bill
print("MOEDAS:")
for coin in coins:
    print(f"{int(money/coin)} moeda(s) de R$ {coin:.2f}")
    money %= coin
print(f"{int((money/0.01)+0.001)} moeda(s) de R$ 0.01")