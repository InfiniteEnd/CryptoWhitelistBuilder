<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>

  <h1>CryptoWhitelistBuilder</h1>

  <h2>Introduction</h2>
  <p>CryptoWhitelistBuilder is a Python script designed to streamline the process of creating a whitelist file for Freqtrade, a cryptocurrency trading bot. The script fetches cryptocurrency symbols from two prominent sources Binance and CoinMarketCap, compares them and generates a Freqtrade-compatible whitelist file containing symbols common to both sources.</p>
  <p>How is this useful? Using endpoints from CoinMarketCap you can automatically pull lists of caterogised symbols from established Capital portfolios like Fenbushi, Huobi or our friends at Kenetic. You could pull full lists of symbols relating to specific Cryptocurrency Ecosystems like Ethereum or Bitcoin. Heck you could use this script to create a whitelist of Meme or NFT symbols if thats your thing LOL!<p>
  <p>In any event this tool aims to simplify the creation of a whitelist by automating the retrieval of symbols quoted in USDT from Binance and CoinMarketCap and identifying the overlapping symbols between the two datasets. By doing so, it facilitates the configuration process for Freqtrade users, enabling them to focus on optimizing their trading strategies.</p>

  <h2>Installation</h2>
  <h3>Prerequisites</h3>
  <p>Ensure you have Python 3 installed on your system. This script also requires 'requests' However the script will check if its installed automatically and should install it for you if its missing. All other Prerequisites are part of Python 3 so thats all you should need to use this script.</p>

  <h3>Steps</h3>
  <ol>
    <li><strong>Clone the Repository:</strong></li>
    <pre>
      <code>git clone https://github.com/InfiniteEnd/CryptoWhitelistBuilder.git</code>
    </pre>
    <li><strong>Update API Keys:</strong></li>
    <p>Open the script file (CryptoWhitelistBuilder.py) in a text editor. Replace api_key with your CoinMarketCap API key.</p>
    <p>A CoinMarketCap API key is mandatory to use this script. Thankfully its completely free and you just need to create a CoinMarketCap developer account to get one.</p>
    <p>Follow the link below for a quickstart guide on how to do that</p>
    <pre>
      <code>https://coinmarketcap.com/api/documentation/v1/</code>
    </pre>
    <li><strong>Run the Script:</strong></li>
    <pre>
      <code>python3 CryptoWhitelistBuilder.py</code>
    </pre>
    <li><strong>Check Output:</strong></li>
    <p>The script will attempt to fetch symbols from Binance and CoinMarketCap, find common symbols, and generate a new whitelist file named whitelist-binance.json in the script's directory.</p>
    <li><strong>Usage Notes:</strong></li>
    <ul>
      <li>Ensure a stable internet connection during execution for proper API interactions.</li>
      <li>Customize the script as needed for your specific Freqtrade setup or requirements.</li>
    </ul>
  </ol>

  <h2>License</h2>
  <p>"Software is like sex, it's better when it's free!" -Linus Torvalds</p>

</body>
</html>
