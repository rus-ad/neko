import vk_api, vk
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import re

from nda_config import group_token, vk_args
from events.info import EventInfo


vk_session = vk_api.VkApi(token=group_token)
longpoll = VkBotLongPoll(vk_session, 160640329)
vk = vk_session.get_api()


def send_message(text):
    vk_args['random_id'] = get_random_id()
    vk_args['message'] = text
    vk_args['chat_id'] = event.chat_id
    vk.messages.send(**vk_args)

neko = re.compile('^нэко')
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        raw_text = event.message['text']
        if neko.search(raw_text.lower().strip()) is None:
            continue

        test_event = EventInfo()
        response = test_event.get_response(raw_text)
        if response is not None:
            send_message(response)
            continue

        send_message("""Знаешь, я давно хотела тебе это сказать.
        Я давно об этом думала, но не знала, как подвести к этому.
        И мне кажется, что ты долбаеб. ❤""")



