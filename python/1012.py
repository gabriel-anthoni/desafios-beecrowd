# beecrowd | 1012 | Área

# Entrada: Leia 1 string.
# Lógica:  Separe a string por espaço para formar 3 números (A, B e C) de ponto flutuante para
#          realizar os cálculos pedidos.
#          Triângulo: (base(A) × altura(C)) / 2
#          Círculo:   pi (3.14159) × raio(C)²
#          Trapézio:  ((Base1(A) + Base2(B)) × altura(C)) / 2
#          Quadrado:  lado(B)²
#          Retângulo: lado1(A) × lado2(B)
# Saída:   Imprima o valor de todos os cálculos com 3 casas decimais, precedido do texto
#          que indica de qual é a área calculada (em maiúsculo e sem caracteres especiais).
#          Exemplo: Triângulo vira "TRIANGULO = ".

# Código:
string = input().split()
a,b,c  = float(string[0]),float(string[1]),float(string[2])
pi     = 3.14159
print(f"TRIANGULO: {((a*c)/2):.3f}\nCIRCULO: {(pi*(c**2)):.3f}\nTRAPEZIO: {(((a+b)*c)/2):.3f}\nQUADRADO: {(b**2):.3f}\nRETANGULO: {(a*b):.3f}")