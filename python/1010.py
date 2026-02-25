# beecrowd | 1010 | Salário com Bônus

# Entrada: Leia 2 strings (A e B).
# Lógica:  Separar cada string por espaço para formar 2 números inteiros e 1 número
#          de ponto flutuante, sendo o primeiro o número do produto, a quantidade
#          de produtos e o valor unitário do produto. Depois, basta multiplicar a
#          quantidade de produtos pelo valor unitário (tanto em A como em B) e somar
#          o valor total dos dois.
# Saída:   Imprima o valor total do cálculo, precedido do texto: "VALOR A PAGAR: R$ ".

# Código:
a = input().split()
b = input().split()
a[0],a[1],a[2] = int(a[0]),int(a[1]),float(a[2])
b[0],b[1],b[2] = int(b[0]),int(b[1]),float(b[2])
print(f"VALOR A PAGAR: R$ {(a[1]*a[2])+(b[1]*b[2]):.2f}")