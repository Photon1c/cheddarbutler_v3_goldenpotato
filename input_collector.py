#gather required inputs from user: source, date range, and price range.

import datetime as dt
import pandas as pd
from datetime import date
import datetime


quick_list = []
option_price = []

def input_collector():
    print(source_greeting)
    source = input("Enter M, L, or F: ")
    print(source)
    date_set = input("For the data range: The default is 2 weeks of historical data, or entering a customized range is possible. Enter D for default or C to customize the date range: ")
    price_set = input("For the price range, Enter D for the default price range of no more than $1 per option premium, or M to manually set a price cutoff: ")
    s_date_list = []
    e_date_list = []
    if source == "L":
        stock_list = input("Enter stock tickers separated by a comma: ")
        quick_list.append(stock_list)
        out_quick = pd.DataFrame(quick_list)
        out_quick.to_csv(r'D:\mainline\goldenpotato\outputs\quick_list.csv')
    if source == "F":
        source = pd.read_csv(r"D:\mainline\goldenpotato\datasets\sample_csv_list.csv")
        quick_list.append(source)
            
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
        s_date = get_first_friday
        e_date = two_weeks_from_nearest_friday_formatted
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

input_collector()    
    
    
    
    
    





  









excel_file = pd.read_csv(r"D:\mainline\goldenpotato\datasets\sample_csv_list.csv")

now = date.today()
today = now.strftime('%Y-%m-%d')
yesterday = (now - pd.Timedelta('1day')).strftime('%Y-%m-%d')
ninedaysago = (now - pd.Timedelta('9day')).strftime('%Y-%m-%d')
