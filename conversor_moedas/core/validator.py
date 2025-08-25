def validador_valor(valor_str: str)  -> float:
    try: 
        valor = float(valor_str)
        if valor <= 0:
            raise ValueError("O valor deve ser positivo")
        return valor
    except ValueError:
        raise ValueError("Entrada inválida. Digite um número válido.")