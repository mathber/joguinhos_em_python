import adivinhacao
import forca

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Selecione um número referente a um jogo: "))

if(jogo == 1):
    print("iniciando Forca...")
    forca.jogar()
elif (jogo == 2):
    print("iniciando Adivinhação...")
    adivinhacao.jogar()