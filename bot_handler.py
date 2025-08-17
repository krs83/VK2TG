import asyncio
import logging

from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest

from config import SLEEP, CHANNEL, BOT_TOKEN

# bot initialization
bot = Bot(token=BOT_TOKEN)

logger = logging.getLogger(__name__)


async def send_text_to_bot(text=None):
    await asyncio.sleep(int(SLEEP))

    if text and text != '':
        logger.info('sending text')
        await bot.send_message(CHANNEL, text)


async def send_image_to_bot(caption, image=None):
    await asyncio.sleep(int(SLEEP))

    if image is not None:
        logger.info('sending image')
        await bot.send_photo(CHANNEL, photo=image, caption=caption)


async def send_group_images_to_bot(group_images=None):
    await asyncio.sleep(int(SLEEP))

    try:
        if group_images is not None:
            logger.info('sending group images')
            await bot.send_media_group(CHANNEL, media=group_images)
    except TelegramBadRequest as msg:
        logger.error(msg)
