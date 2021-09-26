from pycoingecko import CoinGeckoAPI

cryptocurrencies = CoinGeckoAPI()
print("Input the number of cryptocurrencies you would like to see (from 1 to 50)")
def func_crypto():
     N = int(input()) 
     if 0 < N <= 50: #using if statement to define the range of possible cryptocyrrencies
             output = cryptocurrencies.get_coins_markets(vs_currency='usd', order='market_cap_desc', per_page = N, page = 1, sparkline = False
             print(output)

     elif N < 1 or N > 50: print("the input should be from 1 to 50")
                                                         
func_crypto()
