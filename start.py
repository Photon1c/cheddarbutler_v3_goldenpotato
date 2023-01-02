from alpaca_butler.input_collector import collect_inputs
from alpaca_butler import buy_s
from alpaca_butler import buy_o

if __name__ == "__main__":
    collect_inputs()
    buy_s()
    buy_o()