#more work needs to be done on slicing into the optimal option chain rows. 
#Example: for stock i find options where price is <.5. How to handle multiple results?
import yfinance as yf
import pandas as pd

from .buy_s import option_long, target_symbols_long, target_symbols_short, option_short


def option_chain_generator():
    for i in target_symbols_long:
        print("The target symbols will be: ", target_symbols_long)
        chain_symbol = yf.Ticker(str(i))
        #chain_symbol = yf.Ticker(','.join(str(i)))
        chain = chain_symbol.option_chain("2023-01-20")

        try:
            optc = chain_symbol.option_chain("2023-01-20")
            optcz = optc.calls[['lastTradeDate', 'strike', 'lastPrice', 'bid', 'ask', 'volume', 'openInterest', 'impliedVolatility']][20:55]
            optczdf = pd.DataFrame(optcz)

            optczdf['lastTradeDate'] = optczdf['lastTradeDate'].dt.strftime('%m/%d/%Y')
            optczdf.rename(columns = {'lastTradeDate':'lstTrade', 'lastPrice': 'last', 'openInterest': 'OI', 'impliedVolatility': 'IV'}, inplace=True)
            print("\n", "BUY", i, ", Optimal Call Chain:", "\n\n", optczdf, "\n\n")
        except ValueError as err:
            print("no calls available for ", i, "\n\n")

    for i in target_symbols_short:           
            print("The target symbols will be: ", target_symbols_long)
            chain_symbol = yf.Ticker(str(i))
            #chain_symbol = yf.Ticker(','.join(str(i)))
            chain = chain_symbol.option_chain("2023-01-20")

            try:
                optp = chain_symbol.option_chain("2023-01-20")
                optpz = optp.puts[['lastTradeDate', 'strike', 'lastPrice', 'bid', 'ask', 'volume', 'openInterest', 'impliedVolatility']][20:50]
                optpzdf = pd.DataFrame(optpz)
                
                optpzdf['lastTradeDate'] = optpzdf['lastTradeDate'].dt.strftime('%m/%d/%Y')
                optpzdf.rename(columns = {'lastTradeDate':'lstTrade', 'lastPrice': 'last', 'openInterest': 'OI', 'impliedVolatility': 'IV'}, inplace=True)
                print("\n", "SELL", i, ", Optimal Put Chain:", "\n\n", optpzdf, "\n\n")
            except ValueError as err:
                print("no puts available for ", i, "\n\n")    

