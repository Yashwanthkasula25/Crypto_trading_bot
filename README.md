# Binance Futures Trading Bot (Mock Version)

This is a simple Python program that simulates trading on Binance Futures.
It works in mock mode only, so no real API keys or real trading is involved.
All the orders are simulated and stored in a log file.

The program supports:
- Market Orders
- Limit Orders
- Leverage input
- Logging all orders into trading_bot.log

I built this as a practice project to understand how order placement works in futures trading.

## How to Run

1. Install Python (I used Python 3.x)
2. Save the script as mock_trading_bot.py
3. Open terminal in the same folder and run:
4. The bot will start and show a menu.  
5. Enter your option and details like symbol, side, quantity, price, etc.

## Files in this project

- **mock_trading_bot.py** → Main trading bot script  
- **trading_bot.log** → Contains the log of all simulated orders  

## Features

- Clean menu-based UI
- Mock Binance client (no internet or API keys needed)
- Market and Limit orders
- Separate function for leverage
- Input validation for numbers and side (BUY/SELL)
- Logs every action to a file for record-keeping

## Example Flow

After selecting an option, the bot asks for:
- Symbol
- BUY/SELL
- Quantity
- Leverage
- Price (only for limit orders)

After the order is placed, it prints the details on screen and writes them to the log file.

## Notes

- This project is only for learning and demonstration.
- It does not perform any real trading.
- No API keys are required.

Binance Futures Testnet (https://testnet.binancefuture.com) does not load in India
without VPN. Due to this network restriction, I implemented a Mock Binance
client to simulate order placement. The logic, structure, inputs, outputs, logging,
and order processing flow are fully implemented as per the assignment. 
If Binance Testnet is accessible in your environment, the same logic can be
connected to the real testnet client with minimal changes.

