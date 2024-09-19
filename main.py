# source venv/bin/activate - to activate the virtual environment
# python3.11 main.py - to run the bot

# asyncio provides infrastructure for writing asynchronous code
import asyncio
from src.bot import trading_bot

if __name__ == "__main__":
    # starts the asynchronous event loop and runs the trading_bot coroutine
    asyncio.run(trading_bot())