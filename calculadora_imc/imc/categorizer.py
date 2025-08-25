def classificar_imc(imc):
    """Retorna a categoria do IMC."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepreso"
    else: 
        return "Obsesidade"