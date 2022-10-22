from aiogram import types, Bot
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import BOT_TOKEN
from loader import dp
bot = Bot(BOT_TOKEN)

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    await bot.send_sticker(user_id, sticker='CAACAgIAAxkBAAEEeItiWG7TWqCapeRnGLmb0JhzlfO6UwACAQEAAladvQoivp8OuMLmNCME')
    await message.answer(f"Salom, {message.from_user.full_name}!\n"
                         f"Havolani yuboring!")

