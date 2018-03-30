from demo2.handlers.gps.EventHandlerImpl1 import EventHandlerImpl1
from demo2.handlers.gps.EventHandlerImpl2 import EventHandlerImpl2

from demo2.handlers.nav.EventHandlerImpl3 import EventHandlerImpl3
from demo2.handlers.nav.EventHandlerImpl4 import EventHandlerImpl4
from demo2.handlers.nav.EventHandlerImpl5 import EventHandlerImpl5
from demo2.handlers.nav.EventHandlerImpl6 import EventHandlerImpl6


class EventHandlerFactory:
    def __init__(self):
        pass

    factories = {}

    def add_factory(name, handler_factory):
        EventHandlerFactory.factories.put[name] = handler_factory

    add_factory = staticmethod(add_factory)

    # A Template Method:
    def create_handler(name):
        if not EventHandlerFactory.factories.has_key(name):
            EventHandlerFactory.factories[name] = eval(name + '.Factory()')
        return EventHandlerFactory.factories[name].create()

    create_handler = staticmethod(create_handler)