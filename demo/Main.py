import random

# http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html#exercises
# https://stackoverflow.com/questions/3862310/how-to-find-all-the-subclasses-of-a-class-given-its-name
from demo.message import Message, MessageFactory

def message_generator(n):
    '''
    Generate random messages.
    n - count of messages
    '''
    types = Message.Message.__subclasses__()
    for i in range(n):
       yield random.choice(types).__name__


messages = [MessageFactory.MessageFactory.create_message(i)
            for i in message_generator(5)]

for message in messages:
    #message.create()
    message.send()