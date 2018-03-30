from demo2.Event import Event
from demo2.handlers.nav.NavHandler import NavHandler


class EventHandlerImpl4(NavHandler):
    def __init__(self):
        super(EventHandlerImpl4, self).__init__()

    def handle(self, Event):
        print('EventHandlerImpl4.handled: ' + Event.content)

    class Factory:
        def create(self): return EventHandlerImpl4()