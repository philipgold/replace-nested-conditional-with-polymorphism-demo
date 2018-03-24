from demo.message.Message import Message

class EmailMessage(Message):
    def __init__(self, type = 'email'):
        self.type = type

    def create(self):
        print("Email.create")

    def send(self):
        print("Email.send")

    class Factory:
        def create(self): return EmailMessage()