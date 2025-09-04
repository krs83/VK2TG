import configparser
import os

# settings variables
config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.ini')
config = configparser.ConfigParser()
config.read(config_path)

DOMAIN = config.get('VK', 'DOMAIN')
OFFSET = config.get('VK', 'OFFSET')
COUNT = config.get('VK', 'COUNT')
VK_TOKEN = config.get('VK', 'VK_TOKEN')
OWNER_ID = config.get('VK', 'OWNER_ID')
REPOST_ID = config.get('VK', 'REPOST_ID')
VERSION = config.get('VK', 'VERSION')
BOT_TOKEN = config.get('Telegram', 'BOT_TOKEN')
CHANNEL = config.get('Telegram', 'CHANNEL')
SLEEP = config.get('Telegram', 'SLEEP')
INCLUDE_LINK = config.getboolean('Settings', 'INCLUDE_LINK')
# PREVIEW_LINK = config.getboolean('Settings', 'PREVIEW_LINK')
LAST_ID = config.get('Settings', 'LAST_ID')

MAX_MESSAGE_LENGTH = 4096
PRIORITY = ['z', 'base', 'x', 'm', 's']

vk = 'https://vk.ru/'
url = 'https://api.vk.ru/method/wall.get'

params = {
    'owner_id': OWNER_ID,
    'v': VERSION,
    'count': COUNT,
    'offset': OFFSET,
    'access_token': VK_TOKEN
}




