import random

def mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def inicia_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def iniciando_lista(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra? ")
    # remove espaços no começo e fim
    chute = chute.strip()
    return chute

def chute_correto(chute, palavra_atual, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        # .upper() é para não haver distinções entre letras maiúsculas e minúsculas
        if (chute == letra):
            palavra_atual[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():

    mensagem_abertura()
    palavra_secreta = inicia_palavra_secreta()

    palavra_atual = iniciando_lista(palavra_secreta)
    print(''.join(palavra_atual))

    enforcou = False
    acertou = False
    erros = 0

    while (not acertou and not enforcou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            chute_correto(chute, palavra_atual, palavra_secreta)
        else:
            erros += 1

        desenha_forca(erros)
        print(''.join(palavra_atual))

        enforcou = erros == 7
        acertou = "_" not in palavra_atual


    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


    print("Fim do jogo")

# a variável __name__ é preenchida com o valor __main__ caso o arquivo seja executado diretamente.
if (__name__ == "__main__"):
    jogar()
