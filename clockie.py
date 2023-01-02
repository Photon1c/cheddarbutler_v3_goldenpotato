import alpaca_trade_api as tradeapi
import config

#checks if market is open and displays user friendly message.

api = tradeapi.REST(key_id=config.LIVE_API_KEY, secret_key=config.LIVE_SECRET_KEY, api_version='v2',
                                        base_url=config.LIVE_API_BASE_URL)


def is_market_open():
    clock = api.get_clock()
    check_hours = clock.is_open
    if check_hours is False: 
        print("The market is not open at the moment, Cheddar Butler will run once the market opens.")
    if check_hours is True:
        print("The market is open, Cheddar Butler will now start...")
is_market_open()
