from demo2.Event import Event
from demo2.handlers.gps.GPSHandler import GPSHandler

class EventHandlerImpl2(GPSHandler):
    def __init__(self):
        super(EventHandlerImpl2, self).__init__()

    def handle(self, Event):
        print("EventHandlerImpl2.handled: " + Event.content)



    class Factory:
        def create(self):
            return EventHandlerImpl2()