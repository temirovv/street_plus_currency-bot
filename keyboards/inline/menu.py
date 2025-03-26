from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def make_inline_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='🔄 yangilash', callback_data='update'),
                InlineKeyboardButton(text='📱 Kalkulyator', callback_data='calculator')
            ]
        ]
    )
