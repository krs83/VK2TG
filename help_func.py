from aiogram.types import InputMediaPhoto, URLInputFile

from bot_handler import *
from config import vk, DOMAIN


# adding a vk link to post
async def link_include(post, links, text, images):
    post_url = vk + DOMAIN + '?w=wall' + \
               str(post['owner_id']) + '_' + str(post['id'])
    links.insert(0, post_url)
    text = '\n'.join([text] + links)
    await datas_checker(images=images, text=text)

# if one image to process
async def send_posts_img(text, img=None):
    url = None
    length = len(img)

    if length != 0:
        for photo in img[0]['sizes']:
            # seeking for type Z image - good quality(proportional copy with max size  1280x1080)
            if photo['type'] == 'z':
                url = photo['url']
                break
            if photo['type'] == 'base':
                url = photo['url']
        await asyncio.create_task(send_image_to_bot(image=url, text=text))


# process common datas from api reply
async def datas_checker(images, text=None):
    if (text is not None or text != '') and images is None:
        await send_text_to_bot(text)
    image_urls = []
    media = []

    # if more then 1 image to process
    if len(images) > 1:
        for image in images:
            for sizes in image['sizes']:
                if sizes['type'] == 'z':
                    image_urls.append(sizes['url'])
                    break
                if sizes['type'] == 'base':
                    image_urls.append(sizes['url'])

        for i in image_urls:
            media.append(InputMediaPhoto(media=URLInputFile(i)))
        await asyncio.create_task(send_text_to_bot(text=text))
        if media:
            await asyncio.create_task(send_group_images_to_bot(group_images=media))
    else:
        # if one image to process
        await send_posts_img(text=text, img=images)
