# Check for repost

from help_func import link_include
import logging
from config import OWNER_ID, REPOST_ID

logger = logging.getLogger(__name__)

async def repost_processing(post):
    images = []
    links = []

    if 'copy_history' in post:
        owner_id = post['copy_history'][0]['owner_id']
        if owner_id != int(OWNER_ID) and owner_id != int(REPOST_ID):
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

                # if there is a video
                if copy_add['type'] == 'video':
                    attach = copy_history['attachments'][0]['video']
                    frame1 = attach['first_frame'][0]
                    images.append(frame1)

            await link_include(post, links, text, images)