from aiogram import types, Bot
import json
from aiogram.dispatcher.filters.builtin import CommandStart, Command

from data.config import BOT_TOKEN
from loader import dp

bot = Bot(BOT_TOKEN)

# Dictionary to map language codes to human-readable language names
language_choices = {
    'ru': 'Русский 🇷🇺',
    'uz': 'Oʻzbekcha 🇺🇿',
    'en': 'English 🇺🇸',
}
usernames_file = 'usernames.txt'


def save_user_full_name(full_name):
    with open(usernames_file, 'a', encoding='utf-8') as file:
        file.write(f'{full_name}\n')

def is_full_name_saved(full_name):
    # Check if the full name is already in the file
    with open(usernames_file, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip() == full_name:
                return True
    return False

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    full_name = message.from_user.full_name
    if not is_full_name_saved(full_name):
        # Save the user's full name to the text file
        save_user_full_name(full_name)
    # Display language selection buttons
    keyboard = types.InlineKeyboardMarkup()
    for code, lang in language_choices.items():
        keyboard.add(types.InlineKeyboardButton(text=lang, callback_data=f'set_lang_{code}'))
    await message.answer("💬 Пожалуйста, выберите язык интерфейса для использования бота: \n💬 Iltimos, botdan foydalanish uchun interfeys tilini tanlang: \n💬 Please select the interface language to use the bot:", reply_markup=keyboard)
@dp.callback_query_handler(lambda c: c.data.startswith('set_lang_'))
async def set_language(call: types.CallbackQuery):
    # Extract the selected language code
    language_code = call.data.split('_')[-1]

    # Set the user's language preference
    user_id = call.from_user.id
    user_language = language_code  # You can store this in a database for each user
    # Replace this with your code to store the user's language preference

    # Load the corresponding localization file
    try:
        with open(f'locales/{user_language}.json', 'r', encoding='utf-8') as file:
            translation = json.load(file)
    except FileNotFoundError:
        # If the user's language is not supported, fall back to English
        with open('locales/en.json', 'r', encoding='utf-8') as file:
            translation = json.load(file)

    # Get the translated message
    start_message = translation.get('start_message', 'Hello, {full_name}!\nSend a link!')

    # Replace placeholders with user-specific data
    start_message = start_message.format(full_name=call.from_user.full_name)

    # Send the message
    await bot.send_message(user_id, start_message)

    # Remove the language selection message
    await call.message.delete()



