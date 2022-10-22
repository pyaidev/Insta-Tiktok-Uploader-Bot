from aiogram import Bot, Dispatcher, executor, types, executor
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await bot.send_sticker(user_id, sticker='CAACAgIAAxkBAAEEeItiWG7TWqCapeRnGLmb0JhzlfO6UwACAQEAAladvQoivp8OuMLmNCME')
    await message.answer(f"Salom, {message.from_user.full_name}!\n"
                         f"Havolani yuboring!")


