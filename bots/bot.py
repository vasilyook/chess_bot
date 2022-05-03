# from django.db import models
import requests
import time
from .data import *

vasilyook = 1107539029

class Bot():
    def __init__(self, token: str):
        self.token = token
        self.url = 'https://api.telegram.org/bot' + self.token +'/'

    class Update():
        def __init__(self, data: dict):
            self.data = data

        def get_message(self):
            return self.data['message']

        def get_type(self) -> str:
            if 'entities' in self.get_message():
                return self.get_message()['entities'][0]['type']
            return 'text'

        def get_text(self):
            return self.get_message()['text']

        def get_command(self):
            return self.get_text().replace('/','')

        def get_id(self):
            return self.get_message()['chat']['id']

    def send_message(self, text: str, chat_id: float):
        return self.call_method('sendMessage', {'chat_id':str(chat_id),'text':text}) 

    def call_method(self,method: str, params : dict={}):
        return requests.get(self.url + method, params=params).json()

    def handle(self, update):
        self.update = self.Update(update)

        if self.update.get_type() == 'bot_command':
            return getattr(self, self.update.get_command())()
        return self.answer()

    def answer(self):
        return self.send_message(help_text, self.update.get_id())


    def help(self):
        return self.send_message(help_text, self.update.get_id())

    def start(self):
        # start_text = "Hi! I'm Bot. Please, send me /help to get command list."
        return self.send_message(start_text, self.update.get_id())


    def polling(self):
        offset = -1
        while True:
            # print(self.call_method('getUpdates', {'offset': offset}))
            result = self.call_method('getUpdates', {'offset': offset})['result']
            update = result[0] if len(result) > 0 else None
            # print(update)
            if not update:
                time.sleep(3)
                continue
            offset = update['update_id'] + 1
            self.handle(update)
            time.sleep(3)


# bot = Bot(token)
# print(bot.handle({'update_id': 897082096, 'message': {'message_id': 7, 'from': {'id': 1107539029, 'is_bot': False, 'first_name': 'Олечка', 'last_name': 'Васильева', 'username': 'vasilyook', 'language_code': 'ru'}, 'chat': {'id': 1107539029, 'first_name': 'Олечка', 'last_name': 'Васильева', 'username': 'vasilyook', 'type': 'private'}, 'date': 1635879528, 'text': '/help', 'entities': [{'offset': 0, 'length': 5, 'type': 'bot_command'}]}}))
# bot.polling()