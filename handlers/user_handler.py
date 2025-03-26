from aiogram import  types
from aiogram.filters import CommandStart
from data.app import dp
from data.api import filter_contries, make_text, get_calculated_text
from keyboards.inline.menu import make_inline_menu
from keyboards.inline.make_categories import make_categories
from states.user_state import UserState
from aiogram.fsm.context import FSMContext


@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    data = filter_contries()
    text = make_text(data)

    await message.reply(text, reply_markup=make_inline_menu())


@dp.message(lambda message: message.text == 'fastfood')
async def menu_handler(message: types.Message):
    return message.answer('nimadan boshlaymiz', reply_markup=make_categories())



@dp.callback_query(lambda call: call.data == 'update')
async def handle_update(call: types.CallbackQuery):
    data = filter_contries()
    text = make_text(data)
    await call.message.edit_text(text, reply_markup=make_inline_menu())
    # await call.message.answer('update')


@dp.callback_query(lambda call: call.data == 'calculator')
async def handle_calculator(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("Son kiriting")
    await state.set_state(UserState.calculate)
    await call.message.answer('calculator')


@dp.message(UserState.calculate)
async def calculator_handler(message: types.Message, state: FSMContext):
    text = message.text
    print('calkulyator ishladi')
    if text.isdigit():
        data = filter_contries()
        text = get_calculated_text(float(text), data)
        await message.reply(text, reply_markup=make_inline_menu())
        await state.clear()

    else:
        await message.answer('Faqat son kiriting')
