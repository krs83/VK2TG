import asyncio
import logging

import aiohttp

from bot_handler import bot
from config import *
from own_post import own_post_processing
from repost import repost_processing

from aiogram.exceptions import TelegramForbiddenError, TelegramRetryAfter, TelegramBadRequest
from configparser import NoSectionError

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
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
                post_id = config.get('Settings', 'LAST_ID')

                # Compare published posts and continue
                if int(post['id']) <= int(post_id):
                    logger.info('Проверяем последние неопубликованные новости...')
                    continue

                await own_post_processing(post)
                await repost_processing(post)

                # write id to settings.ini
                config.set('Settings', 'LAST_ID', str(post['id']))
                with open(config_path, "w") as config_file:
                    logger.info(f'Last posted news is {post_id}')
                    logger.info('_'*25)
                    config.write(config_file)

async def shutdown():
    # Закрываем соединение с ботом
    logger.info('session is closed')
    await bot.session.close()

async def main():
    """Основная асинхронная функция"""
    logger.info('start main function')
    try:
        await check_posts_vk()  # Запускаем первоначальную проверку
    except TelegramForbiddenError:
        logger.error('The bot is not administrator of this channel. Please add it as admin')
    except TelegramRetryAfter:
        logger.error('Too many requests. Please increase SLEEP variable')
    except KeyError as msg:
        logger.error(f'Key error. This key is not found: {msg}')
    except TelegramBadRequest as msg:
        logger.error(f'The error from Telegram: {msg}')
    except NoSectionError:
        logger.error('Configure file is absent. Please add it to root folder')
    finally:
        await shutdown()

if __name__ == '__main__':
    asyncio.run(main())


