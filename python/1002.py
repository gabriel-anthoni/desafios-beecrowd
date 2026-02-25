# beecrowd | 1002 | Área do Círculo

# Entrada: Leia 1 valor de ponto flutuante que representa o raio.
# Lógica:  Calcule a área do círculo usando pi (valor: 3.14159),
#          multiplicado pelo valor do raio (fornecido na entrada) ao quadrado.
# Saída:   Imprima o resultado do cálculo da área do círculo com 4 casas decimais,
#          precedido do texto: "A=".

# Código:
raio = float(input())
pi   = 3.14159
area = pi*(raio**2)
print(f"A={area:.4f}")