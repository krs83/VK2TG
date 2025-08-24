from help_func import link_include
import logging

logger = logging.getLogger(__name__)

# function to check for datas from group's post
async def own_post_processing(post):
    # Text
    text = post['text']

# Check for post attachments
    images = []
    links = []
    attachments = []
    if 'copy_history' not in post:
        logger.info('posting your own post')
        attach = post['attachments']
        for add in attach:
            if add['type'] == 'photo':
                img = add['photo']
                images.append(img)
            if add['type'] == 'album':
                text = add['album']['title']
                img = add['album']['thumb']
                images.append(img)
            else:
                for (key, value) in add.items():
                    if key != 'type' and 'url' in value:
                        attachments.append(value['url'])

        await link_include(post, links, text, images)
