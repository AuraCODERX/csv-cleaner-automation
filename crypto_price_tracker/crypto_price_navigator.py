import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("88674d79-27a4-40ba-a37f-0782c5c44a61")

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": API_KEY
}

params = {
    "start": "1",
    "limit": "10",
    "convert": "USD"
}

def fetch_crypto_prices():
    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        print("\nTop 10 Cryptocurrencies by Market Cap:\n")
        for crypto in data["data"]:
            name = crypto["name"]
            symbol = crypto["symbol"]
            price = crypto["quote"]["USD"]["price"]
            market_cap = crypto["quote"]["USD"]["market_cap"]
            print(f"{name} ({symbol}): ${price:.2f} | Market Cap: ${market_cap:,.0f}")

    except Exception as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    fetch_crypto_prices()
