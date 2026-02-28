# beecrowd | 1021 | Notas e Moedas

# Entrada: Leia um número de ponto flutuante.
# Lógica:  Divida o valor para saber com quantas e quais notas/moedas são necessárias para formar
#          esse valor (o código pode apresentar erro nos cálculos das moedas de 0.01).
# Saída:   Imprima o valor lido e, para cada nota e moeda, imprima quantas são necessárias
#          para compor esse valor, seguido do texto: "nota(s) de R$ {valor:.2f}" para notas
#          e "moeda(s) de R$ {valor:.2f}" para moedas.

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