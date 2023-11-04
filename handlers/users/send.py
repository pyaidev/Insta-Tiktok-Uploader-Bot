import asyncio

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

    if data == "error":
        await message.answer("Nothing was found through this link")
    else:
        if data['type'] =='image':
            await message.answer_photo(photo=data['media'])
        elif data['type'] =='video':
            wait = await message.answer("Please wait... ⏳")
            await message.answer_video(video=data['media'], caption="Saved @saveinstikbot")
            await wait.delete()
        elif data['type'] =='carousel':
            for i in data['media']:
                wait = await message.answer("Please wait... ⏳")
                await message.answer_document(document=i)
                await wait.delete()
                
        else:
            await message.answer("Nothing was found through this link")




@dp.message_handler(Text(startswith='https://vt.tiktok.com/'))
async def test(message:types.Message):
    natija = tiktok(message.text)
    music = natija['music']

    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Download music", url ='{}'.
            format(music))]
        ]
    )
    await message.answer_video(natija['video'], reply_markup=btn, caption="Saved -> @saveinstikbot")


@dp.message_handler(Text(startswith='https://www.tiktok.com/'))
async def test(message:types.Message):
    natija = tiktok(message.text)
    music = natija['music']

    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Download music", url ='{}'.
            format(music))]
        ]
    )
    wait = await message.answer("Please wait... ⏳")
    await message.answer_audio(natija['video'], reply_markup=btn)
    await wait.delete()


@dp.message_handler()
async def handle_non_url_messages(message: types.Message):
    # This handler will handle all messages that don't match the previous handlers

    # You can respond with a message to inform the user that the message format is not supported
    await message.answer("Sorry, this type of message is not supported. Please provide a valid Instagram or TikTok URL.")