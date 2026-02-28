# beecrowd | 1018 | Cédulas

# Entrada: Leia um número inteiro.
# Lógica:  Divida o valor para saber com quantas e quais notas são necessárias para formar
#          esse valor.
# Saída:   Imprima o valor lido e, para cada nota, imprima quantas são necessárias
#          para compor esse valor, seguido do texto: "nota(s) de R$ {valor},00".

# Código:
money = int(input())
bills = [100,50,20,10,5,2,1] 
print(money)
for bill in bills:
    print(f"{money//bill} nota(s) de R$ {bill},00")
    money %= bill
