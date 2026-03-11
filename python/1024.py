# beecrowd | 1024 | Criptografia

# Entrada: 
#   - Leia um número inteiro que representa quantos texto o programa vai ler e criptografar. 
#   - Leia uma string.
#
# Lógica: 
#   - Para cada string lida siga a ordem para criptografala:
#     1. Avance 3 casas a direita na tebla ASCII para cada carctere que seja uma letra maisucula ou menuscula
#     2. Inverta a ordem dos carcteres do texto de tras para frente
#     3. Retroceda 1 casa a esquerda na tabela ASCII para todos os carcteres do final a metade do texto ( arredondando para cima )
#
# Saída:
#   - para cada string imprima o texto dela com a croptografia.

# Código:
def cryptography(text:list,typeOfchange:str):
    newtext = []
    count   = 0
    for character in text:
        if typeOfchange == "+":
            if character.isalpha():
                    character = chr(ord(character)+3)
                    newtext.append(character)
                    continue
            newtext.append(character)
        else:
            if count >= int(len(text)/2):
                character = chr(ord(character)-1)
                newtext.append(character)
                continue
            count += 1
            newtext.append(character)
    return newtext
            
lines = int(input())
for _ in range(lines):
    text = list(input())
    text = cryptography(text,"+")
    text = text[::-1]
    text = cryptography(text,"-")
    print("".join(text))