def obter_palpite():
    while True:
        try:
            return int(input("Digite seu palpite (1 a 5)"))
        except ValueError:
            print("❌ Entrada inválida. Digite um número inteiro.")


#Funções auxiliares, como validação de entrada.

