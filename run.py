import asyncio

import requests

from config import *
from own_post import own_post_processing
from repost import repost_processing

# get data from vk.com
vk_answer = requests.get(url=url, params=params)


# Check datas before posting to Bot
def check_posts_vk():
    response = reversed(vk_answer.json()['response']['items'])

    for post in response:
        # Read last post id from vk wall
        id = config.get('Settings', 'LAST_ID')

        # Compare published posts and continue
        if int(post['id']) <= int(id):
            print('Нет свежих новостей')
            continue

        own_post_processing(post)
        repost_processing(post)

        # write id to settings.ini
        config.set('Settings', 'LAST_ID', str(post['id']))
        with open(config_path, "w") as config_file:
            config.write(config_file)


if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    check_posts_vk()


