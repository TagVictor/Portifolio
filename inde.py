import requests

# ==================== CONFIGURAÇÕES ====================
url = "https://exemplo.com"  # 🔧 Altere para a página que quiser
headers = {
    "User-Agent": "Mozilla/5.0"
}
# =======================================================

try:
    resposta = requests.get(url, headers=headers)
    if resposta.status_code == 200:
        with open("codigo_fonte.html", "w", encoding="utf-8") as arquivo:
            arquivo.write(resposta.text)
        print(f"Código-fonte salvo com sucesso em 'codigo_fonte.html'.")
    else:
        print(f"Erro ao acessar a página. Código de status: {resposta.status_code}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")