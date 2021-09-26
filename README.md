# Assignment 1 - Asset Kanatov

Python code which pulls the data from coingecko.com and filters out top N cryptocurrencies by market capitalization

## Installation
Basically you have to download pycoingecko library, which is really easy, all you need to do is paste this code into the terminal

```bash
pip install pycoingecko
```

Once you have completed this step, you are ready to run the code, you need to download crypto_output.py file, that is situated in the folder src/

## Usage
If you are using VSCode for programming in Python as me, then you should follow the steps below 
```bash
File -> Open File -> crypto_output.py
```
I hope you found the exact place, where your file was downloaded. After this you are ready to run the code.
## Examples
## Output from crypto_output.py
When you run the code, you have to enter in terminal the number of cryptocurrencies you want to output
```bash
Input the number of cryptocurrencies you would like to see (from 1 to 50)
```

### Example with 1 and 5 cryptocurrencies

```bash
Input the number of cryptocurrencies you would like to see (from 1 to 50)
1
[{'id': 'bitcoin', 'symbol': 'btc', 'name': 'Bitcoin', 'image': 'https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579', 'current_price': 43371, 'market_cap': 815533629829, 'market_cap_rank': 1, 'fully_diluted_valuation': 909665948851, 'total_volume': 31094117276, 'high_24h': 44229, 'low_24h': 40890, 'price_change_24h': 806.4, 'price_change_percentage_24h': 1.89453, 'market_cap_change_24h': 10384500714, 'market_cap_change_percentage_24h': 1.28976, 'circulating_supply': 18826918.0, 'total_supply': 21000000.0, 'max_supply': 21000000.0, 'ath': 64805, 'ath_change_percentage': -33.17172, 'ath_date': '2021-04-14T11:54:46.763Z', 'atl': 67.81, 'atl_change_percentage': 63767.45712, 'atl_date': '2013-07-06T00:00:00.000Z', 'roi': None, 'last_updated': '2021-09-26T18:32:33.221Z'}]
PS C:\Users\asset\Рабочий стол\Python> 

```

```bash
Input the number of cryptocurrencies you would like to see (from 1 to 50)
5
[{'id': 'bitcoin', 'symbol': 'btc', 'name': 'Bitcoin', 'image': 'https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579', 'current_price': 43354, 'market_cap': 815533629829, 'market_cap_rank': 1, 'fully_diluted_valuation': 909665948851, 'total_volume': 30619939693, 'high_24h': 44229, 'low_24h': 40890, 'price_change_24h': 702.33, 'price_change_percentage_24h': 1.64667, 'market_cap_change_24h': 10384500714, 'market_cap_change_percentage_24h': 1.28976, 'circulating_supply': 18826918.0, 'total_supply': 21000000.0, 'max_supply': 21000000.0, 'ath': 64805, 'ath_change_percentage': -33.17172, 'ath_date': '2021-04-14T11:54:46.763Z', 'atl': 67.81, 'atl_change_percentage': 63767.45712, 'atl_date': '2013-07-06T00:00:00.000Z', 'roi': None, 'last_updated': '2021-09-26T18:36:01.801Z'}, <br/>
{'id': 'ethereum', 'symbol': 'eth', 'name': 'Ethereum', 'image': 'https://assets.coingecko.com/coins/images/279/large/ethereum.png?1595348880', 'current_price': 3059.84, 'market_cap': 358465280408, 'market_cap_rank': 2, 'fully_diluted_valuation': None, 'total_volume': 25031618076, 'high_24h': 3067.86, 'low_24h': 2745.41, 'price_change_24h': 153.41, 'price_change_percentage_24h': 5.27814, 'market_cap_change_24h': 15203019986, 'market_cap_change_percentage_24h': 4.42898, 'circulating_supply': 117685154.374, 'total_supply': None, 'max_supply': None, 'ath': 4356.99, 'ath_change_percentage': -29.71697, 'ath_date': '2021-05-12T14:41:48.623Z', 'atl': 0.432979, 'atl_change_percentage': 707145.84059, 'atl_date': '2015-10-20T00:00:00.000Z', 'roi': {'times': 93.39847056190682, 'currency': 'btc', 'percentage': 9339.847056190682}, 'last_updated': '2021-09-26T18:36:08.172Z'}, <br/> 
{'id': 'cardano', 'symbol': 'ada', 'name': 'Cardano', 'image': 'https://assets.coingecko.com/coins/images/975/large/cardano.png?1547034860', 'current_price': 2.26, 'market_cap': 72426099276, 'market_cap_rank': 3, 'fully_diluted_valuation': 101638332206, 'total_volume': 3776222450, 'high_24h': 2.4, 'low_24h': 2.15, 'price_change_24h': -0.122427095937, 'price_change_percentage_24h': -5.135, 'market_cap_change_24h': -4875628926.036575, 'market_cap_change_percentage_24h': -6.30727, 'circulating_supply': 32066390668.4135, 'total_supply': 45000000000.0, 'max_supply': 45000000000.0, 'ath': 3.09, 'ath_change_percentage': -26.75491, 'ath_date': '2021-09-02T06:00:10.474Z', 'atl': 0.01925275, 'atl_change_percentage': 11643.83516, 'atl_date': '2020-03-13T02:22:55.044Z', 'roi': None, 'last_updated': '2021-09-26T18:36:32.139Z'}, <br/> 
{'id': 'tether', 'symbol': 'usdt', 'name': 'Tether', 'image': 'https://assets.coingecko.com/coins/images/325/large/Tether-logo.png?1598003707', 'current_price': 1.0, 'market_cap': 69562102430, 'market_cap_rank': 4, 'fully_diluted_valuation': None, 'total_volume': 70790165190, 'high_24h': 1.03, 'low_24h': 0.994102, 'price_change_24h': 0.0036194, 'price_change_percentage_24h': 0.36195, 'market_cap_change_24h': 63995829, 'market_cap_change_percentage_24h': 0.09208, 'circulating_supply': 69414996725.2484, 'total_supply': 69414996725.2484, 'max_supply': None, 'ath': 1.32, 'ath_change_percentage': -24.19897, 'ath_date': '2018-07-24T00:00:00.000Z', 'atl': 0.572521, 'atl_change_percentage': 75.17609, 'atl_date': '2015-03-02T00:00:00.000Z', 'roi': None, 'last_updated': '2021-09-26T18:35:37.919Z'}, <br/> 
{'id': 'binancecoin', 'symbol': 'bnb', 'name': 'Binance Coin', 'image': 'https://assets.coingecko.com/coins/images/825/large/binance-coin-logo.png?1547034615', 'current_price': 349.18, 'market_cap': 53704848335, 'market_cap_rank': 5, 'fully_diluted_valuation': 59265304345, 'total_volume': 1755272208, 'high_24h': 352.46, 'low_24h': 321.11, 'price_change_24h': -0.31033812378, 'price_change_percentage_24h': -0.0888, 'market_cap_change_24h': -488234264.0824585, 'market_cap_change_percentage_24h': -0.90092, 'circulating_supply': 154533651.9, 'total_supply': 170533651.9, 'max_supply': 170533651.9, 'ath': 686.31, 'ath_change_percentage': -49.19308, 'ath_date': '2021-05-10T07:24:17.097Z', 'atl': 0.0398177, 'atl_change_percentage': 875619.33362, 'atl_date': '2017-10-19T00:00:00.000Z', 'roi': None, 'last_updated': '2021-09-26T18:36:15.409Z'}]
```
