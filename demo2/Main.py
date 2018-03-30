from Event import Event
from MainHandler import MainHandler


nav_event = Event('nav','Nav data event')
gps_event = Event('gps', 'GPS data event')

MainHandler().handle(gps_event)
