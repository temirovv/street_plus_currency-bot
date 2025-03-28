


import asyncio
import logging
import sys

from data.app import dp, bot, db
from handlers import user_handler
from handlers import admin_handler

logging.basicConfig(level=logging.INFO)


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    db.create_category_table()
    db.create_products_table()
    db.create_table_users()
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
