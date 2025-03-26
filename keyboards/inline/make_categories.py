from data.app import db
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def make_categories():
    categories = db.get_categories()
    
    kb = []
    for category in categories:
        category_id, name = category
        kb.append(
            InlineKeyboardButton(text=name, callback_data=f"{name}.{category_id}")
        )
    menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [*kb]
        ]
    )
    return menu
