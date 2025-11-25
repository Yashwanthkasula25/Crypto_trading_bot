# Binance Futures Trading Bot (Mock Version)

This is a Python program that simulates basic trading operations on Binance
Futures. It runs completely in mock mode, so it does not require any real API
keys and does not place real trades. All the orders and actions are stored in a
log file for reference.

## Features

- Market Orders  
- Limit Orders  
- Leverage input  
- Validation for user inputs  
- Clean menu-based interface  
- Logs every order into trading_bot.log  

## How to Run

1. Install Python (I used Python 3.x)
2. Save the script as `mock_trading_bot.py`
3. Open a terminal in the same folder
4. Run the program using:
5. Choose an option from the menu and enter the required details like
   symbol, side, quantity, leverage, and price (for limit orders).

## Files Included

- **mock_trading_bot.py** — main script  
- **trading_bot.log** — log file containing all simulated orders  

## Example Flow

The bot will ask for:
- Symbol  
- BUY or SELL  
- Quantity  
- Leverage  
- Price (only for limit orders)

After placing the order, the program prints the details and also saves them
to the log file.

## Notes

- This project is created for learning and for the assignment.
- It does not interact with real Binance servers.
- No real trading or real API keys are used.

### Important

Binance Futures Testnet (https://testnet.binancefuture.com) is not opening in
India without a VPN. Because of this restriction, I implemented a mock client
to simulate the trading process. The complete logic, inputs, outputs, order
structure, and logging flow follow the assignment requirements.  
If the testnet works in another region, the same logic can be connected to the
real testnet client with small changes.
