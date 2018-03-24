from demo.message.SMSMessage import SMSMessage
from demo.message.FacebookMessage import FacebookMessage
from demo.message.EmailMessage import EmailMessage

class MessageFactory:
    factories = {}

    def add_factory(id, message_factory):
        MessageFactory.factories.put[id] = message_factory

    add_factory = staticmethod(add_factory)

    # A Template Method:
    def create_message(id):
        if not MessageFactory.factories.has_key(id):
            MessageFactory.factories[id] = eval(id + '.Factory()')
        return MessageFactory.factories[id].create()

    create_message = staticmethod(create_message)
