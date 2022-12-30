#create dataframe adding EMA columns to date, stock, and volume columns.     
def dataframe_creator():
    target_symbols_long = []
    target_symbols_short = []
    quote_iter = api.get_bars(i, TimeFrame.Day, start = ninedaysago, end = yesterday, limit=80)._raw
    quotes_df0 = pd.DataFrame(quote_iter)
    quotes_df = pd.DataFrame(index=None)
    quotes_df['Date'] = pd.to_datetime(quotes_df0['t'])
    quotes_df['Date'] = quotes_df['Date'].dt.strftime('%m/%d/%Y')
    quotes_df['Symbol'] = i
    quotes_df['Close'] = quotes_df0['c']
    quotes_df["EMA9"] = quotes_df0['c'].ewm(span=9).mean().round(2)
    quotes_df["EMA20"] = quotes_df0['c'].ewm(span=20).mean().round(2)
    quotes_df["EMA50"] =quotes_df0['c'].ewm(span=50).mean().round(2)
    quotes_df['Volume'] = quotes_df0['v'].apply(lambda x : "{:,}".format(x))
    bool_long = quotes_df["EMA9"].iloc[-1] < quotes_df["Close"].iloc[-1]  ##create Boolean to filter out stocks to go long on.
    if bool_long == True:
        target_list_long = i
        target_symbols_long.append(target_list_long)
        print("Stock ", i, "is within buying parameters. Dataframe: " , "\n")
        print(quotes_df.tail(1))
    else:
        print("Stock", i, "is not within buying parameters")

    bool_short = quotes_df["EMA9"].iloc[-1] > quotes_df["Close"].iloc[-1]  ##create second boolean to filter out stocks to short.
    if bool_short == True:
        target_list_short = i
        target_symbols_short.append(target_list_short)
        print("Stock ", i, "is within selling parameters. Dataframe: " , "\n")
        print(quotes_df.tail(1))
    else:
        print("Stock", i, "is not within selling parameters")