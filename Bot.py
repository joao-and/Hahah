import telebot
import requests
import time

# Seu token do bot do Telegram
TOKEN = "COLE_SEU_TOKEN_AQUI"
bot = telebot.TeleBot(TOKEN)

# ID do chat onde serão enviados os alertas (substitua pelo seu ID)
CHAT_ID = "COLE_SEU_CHAT_ID_AQUI"

# Função para obter o preço do BTC
def get_btc_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    try:
        response = requests.get(url)
        data = response.json()
        price = float(data["bpi"]["USD"]["rate"].replace(",", ""))
        return price
    except Exception as e:
        print("Erro ao obter o preço do BTC:", Name	Last commit date
Bot.py

        return None

# Configuração da estratégia de Swing Trade
PRECO_COMPRA = 65000  # Altere para o preço desejado para comprar
PRECO_VENDA = 72000   # Altere para o preço desejado para vender

# Loop para monitorar o preço
def monitorar_btc():
    while True:
        preco_atual = get_btc_price()
        if preco_atual:
            print(f"Preço Atual do BTC: ${preco_atual}")
            if preco_atual <= PRECO_COMPRA:
                bot.send_message(CHAT_ID, f"🔥 Oportunidade de COMPRA! BTC a ${preco_atual}")
            elif preco_atual >= PRECO_VENDA:
                bot.send_message(CHAT_ID, f"🚀 Hora de VENDER! BTC a ${preco_atual}")
        time.sleep(60)  # Atualiza a cada 60 segundos

# Iniciar a verificação quando o bot for ativado
if __name__ == "__main__":
    bot.send_message(CHAT_ID, "✅ Bot de Swing Trade no BTC iniciado!")
    monitorar_btc()
