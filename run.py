import asyncio
import logging

import aiohttp

from bot_handler import bot
from config import *
from own_post import own_post_processing
from repost import repost_processing

from aiogram.exceptions import TelegramForbiddenError

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

logger = logging.getLogger(__name__)

# Check datas before posting to Bot
async def check_posts_vk():
    # get data from vk.com
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url=url, params=params) as response:
            data = await response.json()

            posts = reversed(data['response']['items'])

            for post in posts:
                # Read last post id from vk wall
                id = config.get('Settings', 'LAST_ID')

                # Compare published posts and continue
                if int(post['id']) <= int(id):
                    print('Нет свежих новостей')
                    continue

                await own_post_processing(post)
                await repost_processing(post)

                # write id to settings.ini
                # config.set('Settings', 'LAST_ID', str(post['id']))
                # with open(config_path, "w") as config_file:
                #     config.write(config_file)

async def shutdown():
    # Закрываем соединение с ботом
    await bot.session.close()

async def main():
    """Основная асинхронная функция"""
    try:
        await check_posts_vk()  # Запускаем первоначальную проверку
    except TelegramForbiddenError:
        logger.error('The bot is not administrator of this channel. Please add it as admin')
    finally:
        await shutdown()

if __name__ == '__main__':
    asyncio.run(main())


