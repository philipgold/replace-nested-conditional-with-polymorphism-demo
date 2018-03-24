from demo.message.Message import Message


class FacebookMessage(Message):
    def __init__(self, type = 'facebook'):
        self.type = type

    def create(self):
        print("Facebook.create")

    def send(self):
        print("Facebook.send")

    class Factory:
        def create(self): return FacebookMessage()
