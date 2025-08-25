def validor_entrada(valor):
    """Valida se o valor é um número positivo."""
    try:
        numero = float(valor)
        if numero > 0:
            return numero
        else:
            raise ValueError
    except ValueError:
        raise ValueError("Entrada inválida. Digite um número positivo.")