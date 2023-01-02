from alpaca_butler.input_collector import collect_inputs
from alpaca_butler.buy_s import dataframe_creator
from alpaca_butler.buy_o import option_chain_generator

if __name__ == "__main__":
    collect_inputs()
    dataframe_creator()
    option_chain_generator()