# Cheddar Butler v3 Golden Potato Edition

Cheddar Butler v3 builds upon the first closed version that used the Ameritrade API,
as well as the second version Bacon Saver which used the yfinance module. It is 
simplified into three steps. The first takes the inputs as indicated by
the user. The second is a hidden layer which screens for the data requested. Finally
the result is generated into both a file and the terminal output. 

```mermaid
stateDiagram-v2
state "User provides parameters" as [*]
state "Input Layer" as Input
state "Hidden Layer" as Hidden
state "Output Layer" as Output
[*] --> Input
Input --> Hidden
Hidden --> Output
Output --> Input: Review

```
  


***Check back for updates to this project***
<br>
Pending tasks:
<br>
Deadline: Jan 10, 2022
<br>
- [ ] Create iterable list of stock tickers to pass through functions
- [ ] Create trade execution function
- [ ] Generate additional sample outputs


### Useful Resources

[yfinance](https://pypi.org/project/yfinance/)<br><br>
[Alpaca Trade API](https://github.com/alpacahq/alpaca-trade-api-python)<br><br>
[Ally API](https://www.ally.com/api/invest/documentation/getting-started/)<br><br>
