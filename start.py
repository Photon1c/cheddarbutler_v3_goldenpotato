from alpaca_butler.input_collector import collect_inputs
from alpaca_butler.buy_s import dataframe_creator
from alpaca_butler.buy_o import option_chain_generator
from alpaca_butler.input_collector import Symbols


if __name__ == "__main__":
    collect_inputs()
    for i in Symbols:
        dataframe_creator(i)
        option_chain_generator(i)