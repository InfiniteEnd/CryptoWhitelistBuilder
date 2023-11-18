import requests
import json
import time
import importlib
import subprocess

# Binance API Configuration
binance_base_url = 'https://api.binance.com/api/v3/exchangeInfo'
max_retries = 3

# CoinMarketCap API Configuration
api_key = "YOUR_COINMARKETCAP_API_KEY"
headers = {"X-CMC_PRO_API_KEY": api_key}
portfolio_endpoints = [
    "605e2e73d41eae1066535f80",
    '605e2e38d41eae1066535f7f',
    # Add other endpoints here
]

# Function to check and install Dependencies
def check_and_install_dependencies():
    required_dependencies = ['requests']

    missing_dependencies = []
    for dependency in required_dependencies:
        try:
            importlib.import_module(dependency)
        except ImportError:
            missing_dependencies.append(dependency)

    if missing_dependencies:
        print(f"Missing dependencies: {missing_dependencies}")
        print("Installing dependencies...")
        subprocess.run(['pip', 'install'] + missing_dependencies, check=True)
        print("Dependencies installed successfully.")
    else:
        print("All dependencies are already installed.")

# Function to fetch symbols quoted in USDT from Binance
def get_symbols_quoted_in_usdt():
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(binance_base_url)
            if response.status_code == 200:
                symbols = response.json()['symbols']
                usdt_symbols = [f"{symbol['baseAsset']}/{symbol['quoteAsset']}" for symbol in symbols if symbol['quoteAsset'] == 'USDT']
                return usdt_symbols
            else:
                print("Failed to fetch data from Binance API. Retrying...")
                retries += 1
                time.sleep(2)  # Adding a small delay before retrying
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            retries += 1
            time.sleep(2)  # Adding a small delay before retrying

    print("Failed after multiple retries. Exiting.")
    return None

# Function to fetch symbols from CoinMarketCap
def get_symbols_from_coinmarketcap():
    symbols = set()
    for endpoint in portfolio_endpoints:
        url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/category?id={endpoint}"
        response = requests.get(url, headers=headers)
        data = response.json()
        coins = data['data']['coins']
        for coin in coins:
            symbol = coin['symbol']
            symbols.add(symbol)

    symbol_list = list(symbols)
    symbol_usdt_list = [symbol + "/USDT" for symbol in symbol_list]
    return symbol_usdt_list

# Function to find symbols that appear in both Binance and CoinMarketCap lists
def find_common_symbols(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_symbols = list(set1.intersection(set2))
    return common_symbols

# Function to create Binance Whitelist for Freqtrade
def create_new_whitelist_file(common_symbols):
    new_whitelist = {
        "exchange": {
            "pair_whitelist": common_symbols
        }
    }
    with open("whitelist-binance.json", "w") as file:
        json.dump(new_whitelist, file, indent=4)
    print("Whitelist file 'whitelist-binance.json' updated successfully.")

if __name__ == "__main__":
    # Calls the check and install function for dependencies before running the other functions.
    check_and_install_dependencies()

    # Fetch symbols quoted in USDT from Binance
    quoted_usdt_symbols_binance = get_symbols_quoted_in_usdt()
    
    # Fetch symbols quoted in USDT from CoinMarketCap
    quoted_usdt_symbols_coinmarketcap = get_symbols_from_coinmarketcap()

    # Find symbols common to both Binance and CoinMarketCap
    common_symbols = find_common_symbols(quoted_usdt_symbols_binance, quoted_usdt_symbols_coinmarketcap)
    
    # Update the existing whitelist file with the common symbols
    if common_symbols:
        create_new_whitelist_file(common_symbols)

