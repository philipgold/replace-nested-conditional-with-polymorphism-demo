from demo2.Event import Event
from demo2.handlers.gps.GPSHandler import GPSHandler


class EventHandlerImpl1(GPSHandler):
    def __init__(self):
        super(EventHandlerImpl1, self).__init__()

    def handle(self, event):
        print("EventHandlerImpl1.handled: " + event.content)

    class Factory:
        def create(self):
            return EventHandlerImpl1()
