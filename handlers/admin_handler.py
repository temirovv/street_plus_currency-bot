from aiogram import F, types
from data.app import dp, db, bot, ADMIN, CHANNEL
from states.admin_state import Advertising
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramForbiddenError



@dp.message((F.from_user.id == ADMIN) & (F.text == 'reklama'))
async def admin_handler(message: types.Message, state: FSMContext):
    await message.answer('salom admin, reklama xabarini kiriting:')
    await state.set_state(Advertising.advertising)


@dp.message(Advertising.advertising)
async def advert_handler(message: types.Message, state: FSMContext):
    users = db.get_all_users()
    reklama_count = 0
    for user in users:
        try:
            reklama_count += 1
            await message.send_copy(chat_id=user[0])
        except TelegramForbiddenError as exception:
            print('user bloklangan')
    print(f"{reklama_count} ta reklama jo'natildi")
    await message.send_copy(chat_id=CHANNEL)
    await state.clear()