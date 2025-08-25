from services.api_client import get_exchange_rate
from core.converter import converter
from core.validator import validador_valor

def main():
    print("💱 Conversor de Moedas")

    base = input("Moeda de origem (ex: USD): ").strip().upper()
    target = input("Moeda de destino (ex: BRL): ").strip().upper()
    valor_str = input(f"Valor em {base}: ").strip()

    try:
        valor = validador_valor(valor_str)
        taxa = get_exchange_rate(base, target)

        if taxa is None:
            print(f"❌ Não foi possível obter a taxa de câmbio de {base} para {target}. Verifique os códigos das moedas.")
            return

        convertido = converter(valor, taxa)
        print(f"\n💰 {valor:.2f} {base} = {convertido:.2f} {target} (taxa: {taxa:.4f})")

    except ValueError as ve:
        print(f"❌ Erro de valor: {ve}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    main()
