from demo2.handlers.gps import GPSHandler
from demo2.handlers.nav import NavHandler
from demo2.handlers.EventHandlerFactory import EventHandlerFactory


class MainHandler:
    def __init__(self):
        pass

    @staticmethod
    def get_handlers():
        gps_types = GPSHandler.GPSHandler.__subclasses__()
        nav_types = NavHandler.NavHandler.__subclasses__()

        types = gps_types + nav_types

        handlers = [EventHandlerFactory.create_handler(name_handler.__name__)
                    for name_handler in types]
        return handlers

    def handle(self, event):
        handlers = self.get_handlers()
        for handler in handlers:
            if event.type == handler.type:
                handler.handle(event)
