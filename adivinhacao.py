import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************\n")

    numero_secreto = int(random.randrange(1, 101))

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    pontos = 1000
    rodada = 1

    # o "for" possui um terceiro parâmetro que seria de quanto em quanto pula
    for rodada in range(1, total_de_tentativas+1):

        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        # a função de input retorna uma string, logo, há a necessidade de passá-la para inteiro
        chute = int(input("Digite um número entre 1 e 100: "))

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Parabéns, você acertou!")
            print("Total de pontos: {}".format(pontos))
            break
        else:
            if(rodada == total_de_tentativas):
                print("Você errou, o número era {}.".format(numero_secreto))
            else:
                if(maior):
                    print("Você errou, o seu chute é maior do que o número.")
                elif(menor):
                    print("Você errou, o seu chute é menor do que o número.")
                pontos -= abs(numero_secreto-chute)


    print("Fim de jogo!")

if (__name__ == "__main__"):
    jogar()