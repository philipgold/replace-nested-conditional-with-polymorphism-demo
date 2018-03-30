from demo2.handlers.EventHandler import EventHandler


class NavHandler(EventHandler):
    def __init__(self, handler_type='nav'):
        self.type = handler_type
