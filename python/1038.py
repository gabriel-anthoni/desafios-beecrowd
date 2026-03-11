# beecrowd | 1038 | Lanche
#
# Entrada:
#   - Leia uma string contendo dois números inteiros: o código do item e a quantidade.
#
# Lógica:
#   - Separe a string em 2 valores inteiros para obter o produto escolhido e a quantidade deles.
#   - Pelo produto escolhido veja o preço dele na tabela e multiplique pela quantidade para obter o valor total.
#
# Saída:
#   - Imprima o valor total formatado como moeda (duas casas decimais) com o prefixo "Total: R$ ".

# Código:
snacks = [4.00,4.50,5.00,2.00,1.50]
order  = input().split()
print(f"Total: R$ {((snacks[(int(order[0])-1)])*int(order[1])):.2f}")