#gather required inputs from user: source, date range, and price range.

import datetime as dt
import pandas as pd
from datetime import date
import datetime


#create automated default 2 week historical data window:
#create starting and ending dates, set to nearest friday and two weeks from nearest friday
get_first_friday = dt.date.today()
while get_first_friday.weekday() != 4:
    get_first_friday += dt.timedelta(1)
two_weeks = dt.timedelta(days=14)
two_weeks_from_nearest_friday = get_first_friday + two_weeks
two_weeks_from_nearest_friday_formatted = two_weeks_from_nearest_friday.strftime("%Y-%m-%d")



source_greeting = str("For the data source: Enter M if you will be running Golden Potato using a list of default \ndaily top moving stocks. Enter L if you will be manually entering a list of stock tickers. \nFinally, enter F if you want to enter the name of a CSV file containing a list of stock tickers. \nPlease refer to the documentation for the preferred format. ")



quick_list = []
option_price = []

def collect_inputs():
    print(source_greeting)
    source = input("Enter M, L, or F: ")
    print(source)
    date_set = input("For the data range: The default is 2 weeks of historical data, or entering a customized range is possible. Enter D for default or C to customize the date range: ")
    price_set = input("For the price range, Enter D for the default price range of no more than $1 per option premium, or M to manually set a price cutoff: ")

    if source == "L":
        stock_list = input("Enter stock tickers separated by a comma: ")
        quick_list.append(stock_list)
        out_quick = pd.DataFrame(quick_list)
        out_quick.to_csv(r'D:\mainline\goldenpotato\outputs\manual_list.csv')
    if source == "F":
        source = pd.read_csv(r"D:\mainline\goldenpotato\datasets\sample_csv_list.csv")
        quick_list.append(source)
    if source == "M":
        after_hours()
        quick_list.concat(after_hourdf)    
        if after_hourdf.empty:
            print("Empty dataframe, running script again", "\n\n\n")
            collect_inputs()
        else:    
            print("Tickers are: ", after_hourdf, " ...please wait.", "\n")    
        
    if date_set == "C":
        s_date = input("Enter start date in YYYY-MM-DD format: ")
        for i in s_date:
            temps = s_date
            s_date_list.append(temps)
        e_date = input("Enter end date in similar format: ")
        for i in e_date:
            tempe = e_date
            e_date_list.append(tempe)
    if date_set == "D":
        s_date = []
        s_date = []
        s_date == get_first_friday
        e_date = []
        e_date == two_weeks_from_nearest_friday_formatted
                
    if price_set == "D":
        optiond = 1
        option_price.append(optiond)
    if price_set == "M":
        optionc = input("Enter premium cutoff price, this will consider both calls and puts: ")
        option_price.append(optionc)
    print(quick_list)
    print(s_date)
    print(e_date)
    print(option_price)
    format = "%Y-%m-%d"

    
 #function to get list of stocks from yfinance. These can either be the daily top moving stocks, or the after hours list from MarketWatch.


#def daily_movers()
#find api command to retrieve daily top moving stocks. tbc

after_hourdf = pd.DataFrame()

def after_hours():
    df = pd.read_html("https://www.marketwatch.com/tools/screener/after-hours")
    dfg = df[0]
    #create new series that keeps only first string value in 'Symbol Symbol' column, 
    #discardinganything after space
    dfgainers = dfg['Symbol  Symbol'].str[:4]
    dflosers = df[1]
    dflosers2 = dflosers['Symbol  Symbol'].str[:4]
    dfgainers2 = dfgainers
    df_final = dfgainers2.append(dflosers2)
    df_final2 = pd.DataFrame()
    df_final2["Symbol"] = df_final
    df_final2["Symbol"].to_csv(r'[path to your csv file with stock tickers]')
    after_hourdf.append(df_final2)
    

    
    





  









excel_file = pd.read_csv(r"D:\mainline\goldenpotato\datasets\sample_csv_list.csv")

now = date.today()
today = now.strftime('%Y-%m-%d')
yesterday = (now - pd.Timedelta('1day')).strftime('%Y-%m-%d')
ninedaysago = (now - pd.Timedelta('9day')).strftime('%Y-%m-%d')
