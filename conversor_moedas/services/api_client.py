import requests

def get_exchange_rate(base: str, target: str) -> float:
    url = f"https://api.frankfurter.app/latest?from={base}&to={target}"
    response = requests.get(url)
    
    # Verifica se a resposta foi bem-sucedida
    if response.status_code != 200:
        raise Exception(f"Erro na requisição: {response.status_code}")
    
    data = response.json()

    # Verifica se a chave 'rates' existe e contém a moeda de destino
    if "rates" in data and target in data["rates"]:
        return data["rates"][target]
    else:
        print("🔍 Resposta inesperada da API:", data)  # Ajuda na depuração
        return None  # Deixa o main.py lidar com isso
