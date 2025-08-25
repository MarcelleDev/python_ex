def calculador_imc(peso, altura):
    # Verifica se altura está em centímetros e converte
    if altura > 10:  # altura maior que 10 provavelmente está em cm
        altura = altura / 100

    imc = peso / (altura ** 2)
    return round(imc, 2)
