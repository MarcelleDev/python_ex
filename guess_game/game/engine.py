import random
from .utils import obter_palpite

def jogar():
    numero_secreto = random.randint(1, 5)
    tentativas = 0
    print("🎯 Bem-vindo ao jogo de adivinhação!")

    while True:
        palpite = obter_palpite()
        tentativas += 1

        if palpite == numero_secreto:
            print(f"✅ Parabéns! Você acertou em {tentativas} tentativas.")
            break
        elif palpite < numero_secreto:
            print("🔼 Tente um número maior.")
        else:
            print("🔽 Tente um número menor.")

#Contém a lógica do jogo.