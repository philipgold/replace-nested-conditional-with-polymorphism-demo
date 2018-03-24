from demo.message.Message import Message


class SMSMessage(Message):
    def __init__(self, type = 'sms'):
        self.type = type

    def create(self):
        print("SMS.create")

    def send(self):
        print("SMS.send")

    class Factory:
        def __init__(self):
            pass

        def create(self):
            return SMSMessage()