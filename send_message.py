# -*- coding: UTF-8 -*-
import requests
from constrains import Constrains
import random
class SendMessage(object):
    def __init__(self):
        self.session = requests.session()
        self.session.headers = Constrains.HEADER

    def send_messge(self):
        message =random.choice(Constrains.MESSAGES)
        print(message)
        DATA = {
            "color": 16777215,
            "fontsize": "25",
            "mode": "2",
            "msg": message,
            "roomid": "22412265",
            "bubble": 0,
            "rnd": "粘贴内容",
            "csrf_token": "粘贴内容",
            "csrf": "粘贴内容"
        }
        result = self.session.post(Constrains.URL,DATA).json()
        print(result)
