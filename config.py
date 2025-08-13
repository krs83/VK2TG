import configparser
import os
import sys

# settings variables
config_path = os.path.join(sys.path[0], 'settings.ini')
config = configparser.ConfigParser()
config.read(config_path)

DOMAIN = config.get('VK', 'DOMAIN')
OFFSET = config.get('VK', 'OFFSET')
COUNT = config.get('VK', 'COUNT')
VK_TOKEN = config.get('VK', 'VK_TOKEN')
OWNER_ID = config.get('VK', 'OWNER_ID')
VERSION = config.get('VK', 'VERSION')
BOT_TOKEN = config.get('Telegram', 'BOT_TOKEN')
CHANNEL = config.get('Telegram', 'CHANNEL')
SLEEP = config.get('Telegram', 'SLEEP')
INCLUDE_LINK = config.getboolean('Settings', 'INCLUDE_LINK')
# PREVIEW_LINK = config.getboolean('Settings', 'PREVIEW_LINK')
LAST_ID = config.get('Settings', 'LAST_ID')

# max_message_length = 4096
max_caption_length = 900

vk = 'https://vk.com/'
url = 'https://api.vk.com/method/wall.get'

params = {
    'owner_id': OWNER_ID,
    'v': VERSION,
    'count': COUNT,
    'offset': OFFSET,
    'access_token': VK_TOKEN
}


