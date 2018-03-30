from demo2.handlers.EventHandler import EventHandler


class GPSHandler(EventHandler):
    def __init__(self, handler_type='gps'):
        self.type = handler_type