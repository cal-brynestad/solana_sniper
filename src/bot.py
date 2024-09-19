import asyncio
import logging
from .email_parser import read_newsletter
from .solana_trader import execute_trade
from .utils import load_config

logger = logging.getLogger(__name__)

async def trading_bot():
    config = load_config()
    
    while True:
        try:
            coin_info = read_newsletter(config['email'])
            if coin_info:
                result = await execute_trade(coin_info, config['solana'])
                logger.info(f"Trade executed: {result}")
            
            await asyncio.sleep(config['trading']['check_interval'])
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            await asyncio.sleep(60)  # Wait a bit before retrying