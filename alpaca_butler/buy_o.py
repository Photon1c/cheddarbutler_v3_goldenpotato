#more work needs to be done on slicing into the optimal option chain rows. 
#Example: for stock i find options where price is <.5. How to handle multiple results?
import yfinance as yf

quick_list = []

def option_chain_generator():
    chain_symbol = yf.Ticker(i)
    chain = chain_symbol.option_chain("2023-01-20")
    call_chain = chain.calls
    put_chain = chain.puts 
    if bool_long == True:
        try:
            optc = chain_symbol.option_chain("2023-01-20")
            optcz = optc.calls[['strike', 'lastPrice', 'bid', 'ask', 'volume', 'openInterest', 'impliedVolatility']][2:16]
            optczdf = pd.DataFrame(optcz)
            long_df.join(optczdf) 
            optczdf['lastTradeDate'] = optczdf['lastTradeDate'].dt.strftime('%m/%d/%Y')
            print("\n", "BUY", i, ", Optimal Call Chain:", "\n\n", optczdf, "\n\n")
        except ValueError as err:
            print("no calls available for ", i, "\n\n")

    else:
        try:
            optp = chain_symbol.option_chain("2023-01-20")
            optpz = optp.puts[['lastTradeDate', 'strike', 'lastPrice', 'bid', 'ask', 'volume', 'openInterest', 'impliedVolatility']][20:50]
            optpzdf = pd.DataFrame(optpz)
            short_df.join(optpzdf)
            optpzdf['lastTradeDate'] = optpzdf['lastTradeDate'].dt.strftime('%m/%d/%Y')
            print("\n", "SELL", i, ", Optimal Put Chain:", "\n\n", optpzdf, "\n\n")
        except ValueError as err:
            print("no puts available for ", i, "\n\n")    
for i in quick_list:
    option_chain_generator()