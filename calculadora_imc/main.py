from imc.calculator import calcular_imc
from imc.categorizer import classificar_imc
from imc.validator import validar_entrada

def main():
    print("🧮 Calculadora de IMC")

    while True:
        try:
            peso = validar_entrada(input("Digite seu peso (kg): "))
            altura = validar_entrada(input("Digite sua altura (m): "))
            imc = calcular_imc(peso, altura)
            categoria = classificar_imc(imc)

            print(f"\n✅ Seu IMC é {imc:.2f} — {categoria}")
            break
        except ValueError as e:
            print(f"❌ {e}")
            continue

if __name__ == "__main__":
    main()
