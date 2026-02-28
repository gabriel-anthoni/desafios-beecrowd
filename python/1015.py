# beecrowd | 1015 | Distância Entre Dois Pontos

# Entrada: Leia 2 strings (A e B).
# Lógica:  Separe cada string por espaços para obter 2 números de ponto flutuante. 
#          Na string A, obtenha os números x1 e y1. 
#          Na string B, obtenha os números x2 e y2. 
#          Em seguida, calcule a distância usando a fórmula: (x2 - x1)² + (y2 - y1)² 
#          e, por fim, tire a raiz quadrada do resultado.
# Saída:   Imprima o resultado com 4 casas decimais.

# Código:
A     = input().split()
B     = input().split()
x1,y1 = float(A[0]),float(A[1])
x2,y2 = float(B[0]),float(B[1])
print(f"{pow(((x2-x1)**2)+((y2-y1)**2),0.5):.4f}")