# Binance Futures Trading Bot

## Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- CLI arguments
- Input validation
- Logging
- Error handling

## Setup

pip install -r requirements.txt

## Run

Market Order:

python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001

Limit Order:

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 120000

## Known Issue

The Binance Demo Futures API currently returns HTTP 403 Forbidden responses despite successful API key generation and authentication. The application includes error handling and logging for such API failures.
