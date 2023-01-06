import alpaca_trade_api as tradeapi
import config
import logging
from alpaca_trade_api.rest import REST, TimeFrame
import datetime as dt
import pandas as pd
from datetime import date
import datetime
import yfinance as yf

#call API
api = tradeapi.REST(key_id=config.LIVE_API_KEY, secret_key=config.LIVE_SECRET_KEY, api_version='v2',
                                        base_url=config.LIVE_API_BASE_URL)
target_symbols_long = []
target_symbols_short = []

i = str

quick_list = []

Symbols = input("Enter tickers separated by commas:  \n").split(', ')

#useful date formats
now = date.today()
today = now.strftime('%Y-%m-%d')
yesterday = (now - pd.Timedelta('1day')).strftime('%Y-%m-%d')
ninedaysago = (now - pd.Timedelta('9day')).strftime('%Y-%m-%d')


#main screening function, runs buy_o if buy_s parameters are met
def start_screen():
    for i in Symbols:
        stock = yf.Ticker(str(i))
        # get stock info
        #print(stock.info['longBusinessSummary'])
        # get historical market data
        hist = stock.history(period="2mo")
        histd = pd.DataFrame(hist)
        df = pd.DataFrame()
        df["Date"] = pd.to_datetime(histd.index, unit='ms')
        df["Close"] = histd["Close"].values
        df["Volume"] = hist['Volume'].values
        df["EMA9"] = df["Close"].ewm(span=9).mean().round(2)
        df["EMA20"] = df["Close"].ewm(span=20).mean().round(2)
        df["EMA50"] =df["Close"].ewm(span=50).mean().round(2)
        df["Symbol"] = stock.ticker
        bool_long = df["EMA9"].iloc[-1] < hist["Close"].iloc[-1]  ##create Boolean to filter out stocks to go long on.
        if bool_long == True:
            target_list_long = df['Symbol'][0]
            target_symbols_long.append(target_list_long)
            print("Stock ", i, "is within buying parameters. Dataframe: " , "\n")
            print(df.tail(1))
            print("\n")
            try:
                optc = stock.option_chain("2023-01-20")
                optcl = optc.calls
                optcd = pd.DataFrame(optcl)
                optcd.rename(columns = {'lastTradeDate':'lstTrade', 'lastPrice': 'last', 'openInterest': 'oInterest', 'impliedVolatility': 'iVol'}, inplace=True)
                optcd['lstTrade'] = optcd['lstTrade'].dt.strftime('%m/%d/%Y')
                print("Calls for ", i, "are: ", "\n", optcd[['lstTrade', 'strike', 'last', 'bid', 'ask', 'volume', 'oInterest', 'iVol']][3:5])
            except ValueError as err:
                print("no calls available for ", i)
                print("\n")
            print(df.tail(1))
            print("\n")
        else:
            print("Stock", i, "is not within buying parameters")

        bool_short = df["EMA9"].iloc[-1] > hist["Close"].iloc[-1]  ##create second boolean to filter out stocks to short.
        if bool_short == True:
            target_list_short = df['Symbol'][0]
            target_symbols_short.append(target_list_short)
            try:
                optp = stock.option_chain("2023-01-20")
                optpl = optp.puts
                optpd = pd.DataFrame(optpl)
                optpd.rename(columns = {'lastTradeDate':'lstTrade', 'lastPrice': 'last', 'openInterest': 'oInterest', 'impliedVolatility': 'iVol'}, inplace=True)
                optpd['lstTrade'] = optpd['lstTrade'].dt.strftime('%m/%d/%Y')
                print("Puts for ", i, "are: ", "\n", optpd[['lstTrade', 'strike', 'last', 'bid', 'ask', 'volume', 'oInterest', 'iVol']][3:5])
            except ValueError as err:
                print("No puts available for ", i)
                print("\n")
            print("Stock ", i, "is within selling parameters. Dataframe: " , "\n")
            print(df.tail(1))
            print("\n")
        else:
            print("Stock", i, "is not within selling parameters")
 
    
    


if __name__ == '__main__':
    try:
        start_screen()
    except:
        start_screen()

print("The stocks to go long on are: ", target_symbols_long, "\n")
print("The stocks to go short on are: ", target_symbols_short)

