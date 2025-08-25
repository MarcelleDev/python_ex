# imc/calculator.py
def calcular_imc(peso: float, altura: float) -> float:
    if altura <= 0:
        raise ValueError("A altura deve ser maior que zero.")
    return peso / (altura ** 2)
