import asyncio
import logging

from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest

from config import SLEEP, CHANNEL, BOT_TOKEN, MAX_MESSAGE_LENGTH

# bot initialization
bot = Bot(token=BOT_TOKEN)

logger = logging.getLogger(__name__)

# text slicing if it is too long for TG
def if_long_text(text: str, max_length: int=MAX_MESSAGE_LENGTH) -> str:
    if len(text) <= max_length:
        yield text
    else:
        for i in range(0, len(text), max_length):
            yield text[i:i + max_length]

async def send_text_to_bot(text=None):
    await asyncio.sleep(int(SLEEP))

    if text and text != '':
        logger.info('sending text')
        for part in if_long_text(text):
            await bot.send_message(CHANNEL, part)

async def send_image_to_bot(text: str, image=None):
    await asyncio.sleep(int(SLEEP))

    if image is not None:
        logger.info('sending image')

        await bot.send_photo(CHANNEL, photo=image)

        for part in if_long_text(text):
            await bot.send_message(CHANNEL, part)

async def send_group_images_to_bot(group_images=None):
    await asyncio.sleep(int(SLEEP))

    try:
        if group_images is not None:
            logger.info('sending group images')
            await bot.send_media_group(CHANNEL, media=group_images)
    except TelegramBadRequest as msg:
        logger.error(msg)
