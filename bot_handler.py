import asyncio

from aiogram import Bot

from config import SLEEP, CHANNEL, BOT_TOKEN

# bot initialization
bot = Bot(token=BOT_TOKEN)


async def send_text_to_bot(text=None):
    await asyncio.sleep(int(SLEEP))

    if text and text != '':
        await bot.send_message(CHANNEL, text)


async def send_image_to_bot(caption, image=None):
    await asyncio.sleep(int(SLEEP))

    if image is not None:
        await bot.send_photo(CHANNEL, photo=image, caption=caption)


async def send_group_images_to_bot(group_images=None):
    await asyncio.sleep(int(SLEEP))

    if group_images is not None:
        await bot.send_media_group(CHANNEL, media=group_images)
