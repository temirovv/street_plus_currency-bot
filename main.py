


import asyncio
import logging
import sys

from data.app import dp, bot
from handlers import user_handler

logging.basicConfig(level=logging.INFO)


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
