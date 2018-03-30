from demo2.Event import Event
from demo2.handlers.nav.NavHandler import NavHandler


class EventHandlerImpl3(NavHandler):
    def __init__(self):
        super(EventHandlerImpl3, self).__init__()

    def handle(self, Event):
        print('EventHandlerImpl3.handled: ' + Event.content)

    class Factory:
        def create(self): return EventHandlerImpl3()