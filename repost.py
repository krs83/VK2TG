# Check for repost

from help_func import link_include
import logging

logger = logging.getLogger(__name__)

async def repost_processing(post):
    images = []
    links = []

    if 'copy_history' in post:
        logger.info('posting from another source')
        copy_history = post['copy_history'][0]
        text = copy_history['text']
        # post text from repost

        # Check for reposts' attachment
        if 'attachments' in copy_history:
            copy_add = copy_history['attachments'][0]

            # if there is an image
            if copy_add['type'] == 'photo':
                attach = copy_history['attachments']
                for img in attach:
                    if 'photo' in img:
                        img = img['photo']
                        images.append(img)

        await link_include(post, links, text, images)