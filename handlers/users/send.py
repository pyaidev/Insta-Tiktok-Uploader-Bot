from aiogram import types
from loader import dp, bot
from aiogram.dispatcher.filters import Text
from insta import instadownloader
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from tiktok import tiktok


@dp.message_handler(Text(startswith='https://www.instagram.com/'))
async def send_media(message:types.Message):
    link = message.text
    data = instadownloader(link=link)
    if data == "Error":
        await message.answer("Kanalga obuna bo'ling @the_best_python")
    else:
        if data['type'] == 'image':
            await message.answer_photo(photo=data['media'], caption="Yuklandi -> @saveinstikbot")
        elif data['type'] == 'video':
            await message.answer_video(video=data['media'], caption="Yuklandi -> @saveinstikbot")
        elif data['type'] == 'carousel':
            for i in data['media']:
                await message.answer_document(document=i, caption="Yuklandi -> @saveinstikbot")
        else:
            await message.answer("Kanalga obuna bo'ling @the_best_python")


@dp.message_handler(Text(startswith='https://vt.tiktok.com/'))
async def test(message:types.Message):
    natija = tiktok(message.text)
    music = natija['music']

    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Musiqasini yuklap olish", url ='{}'.
            format(music))]
        ]
    )
    await message.answer_audio(natija['video'], reply_markup=btn)
    await message.answer("Kanalga obuna bo'ling @the_best_python")


@dp.message_handler(Text(startswith='https://www.tiktok.com/'))
async def test(message:types.Message):
    natija = tiktok(message.text)
    music = natija['music']

    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Musiqasini yuklap olish", url ='{}'.
            format(music))]
        ]
    )
    await message.answer_audio(natija['video'], reply_markup=btn)
    await message.answer("Kanalga obuna bo'ling @the_best_python")
