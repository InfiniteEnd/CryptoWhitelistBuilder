import requests

# CoinMarketCap API Configuration
api_key = "7c80fd1d-dff9-46ec-91e6-651a68582b95"
headers = {"X-CMC_PRO_API_KEY": api_key}

def get_categories():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/categories"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        categories = response.json()["data"]
        return categories
    else:
        print("Failed to fetch categories from CoinMarketCap API.")
        return None

if __name__ == "__main__":
    categories = get_categories()
    if categories:
        print("Available Categories on CoinMarketCap:")
        for category in categories:
            print(f"ID: {category['id']}, Name: {category['name']}")

