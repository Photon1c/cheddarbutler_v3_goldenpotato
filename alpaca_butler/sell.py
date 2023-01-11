import alpaca_trade_api as tradeapi
import datetime as dt
import pandas as pd
import config


api = tradeapi.REST(key_id=config.LIVE_API_KEY, secret_key=config.LIVE_SECRET_KEY, api_version='v2',
                                        base_url=config.LIVE_API_BASE_URL)

positions = api.list_positions()





for position in positions:
    held_symbol = position.symbol
    held_quantity = position.qty
    held_total_cost = position.cost_basis
    held_unit_cost = position.avg_entry_price
    held_pc_upl = position.unrealized_plpc
    held_dl_upl = position.unrealized_pl
    positions_df = pd.DataFrame(positions)
    print(positions_df.keys)