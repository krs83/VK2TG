# Check for repost
from help_func import shorten_text, link_include
import logging

logger = logging.getLogger(__name__)

async def repost_processing(post):
    images = []
    links = []

    if 'copy_history' in post:
        copy_history = post['copy_history'][0]
        # logger.info(copy_history)
        text = await shorten_text(copy_history['text'])
        # post text from repost

        # Check for reposts' attachment
        if 'attachments' in copy_history:
            copy_add = copy_history['attachments'][0]

            # if there is a link
            # if copy_add['type'] == 'link':
            #     link = copy_add['link']
            #     print(f'link is {link}')
            #     text = link['title']
            #     send_posts_text(text)
            #     img = link['photo']
            #     send_posts_img(img)
            #     url = link['url']
            #     send_posts_text(url)
            #     print(url)

            # if there is an image
            if copy_add['type'] == 'photo':
                attach = copy_history['attachments']
                for img in attach:
                    if 'photo' in img:
                        img = img['photo']
                        images.append(img)

        await link_include(post, links, text, images)