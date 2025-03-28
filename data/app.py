from aiogram import Bot, Dispatcher
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from utils.db.sqlite import Database


TOKEN = ''
ADMIN = ''
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()
db = Database()