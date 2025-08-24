from aiogram.types import InputMediaPhoto, URLInputFile

from bot_handler import *
from config import vk, DOMAIN, PRIORITY


# adding a vk link to post
async def link_include(post, links, text, images):
    post_url = vk + DOMAIN + '?w=wall' + \
               str(post['owner_id']) + '_' + str(post['id'])
    links.insert(0, post_url)
    text = '\n'.join([text] + links)
    await datas_checker(images=images, text=text)

def seeking_img_sizes(image):
    # Создаем словарь для быстрого поиска
    if len(image) > 1:
        size_map = {img['type']: img['url'] for img in image['sizes'] if 'type' in img and 'url' in img}
    else:
        size_map = {img['type']: img['url'] for img in image[0]['sizes'] if 'type' in img and 'url' in img}

    # Ищем по приоритету
    for size_type in PRIORITY:
        if url := size_map.get(size_type):
            return url

    return None


# if one image to process
async def send_posts_img(text, image=None):
    length = len(image)

    if length != 0:
        url = seeking_img_sizes(image)
        await asyncio.create_task(send_image_to_bot(image=url, text=text))


# process common datas from api reply
async def datas_checker(images, text=None):
    if (text is not None or text != '') and images is None:
        await send_text_to_bot(text)
    image_urls = []
    media = []

    # if more then 1 image to process
    if len(images) > 1:
        for img in images:
            url = seeking_img_sizes(img)
            image_urls.append(url)

        for i in image_urls:
            media.append(InputMediaPhoto(media=URLInputFile(i)))
        await asyncio.create_task(send_text_to_bot(text=text))
        if media:
            await asyncio.create_task(send_group_images_to_bot(group_images=media))
    else:
        # if one image to process
        await send_posts_img(text=text, image=images)
