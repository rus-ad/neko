from events.base_event import BaseEvent
import re
from random import randrange, choice


class EventInfo(BaseEvent):

    def __init__(self):
        self._name = 'event_info'
        self.pattern = re.compile('^нэко инфа')
        self.answers = [
            'Мяу! Мне намурчали на ушко, что это примерно: ',
        ]

    def actions(self, text):
        prob = randrange(0, 101, 2)
        response = choice(self.answers)
        response += f'{prob}%'
        return response
