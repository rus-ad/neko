import re


class BaseEvent:

    def __init__(self):
        self._name = 'base_event'
        self.search_pattern = None
        self.pattern = None

    def get_name(self):
        return self._name

    def get_response(self, raw_text):
        text = self.preprocessing(raw_text)
        if self.search_pattern(text.lower()) is not None:
            return self.actions(text)
        return None

    def search_pattern(self, text):
        result = re.search(self.pattern, text)
        print(result, text)
        if result is not None:
            result = result.span()[1]
        return result

    def preprocessing(self, raw_text: str):
        text = re.sub('\s+', ' ', raw_text)
        text = text.strip()
        return text

    def actions(self, text):
        """Some actions"""
