from ladon.compat import PORTABLE_STRING
from ladon.ladonizer import ladonize

class Service(object):

        @ladonize(PORTABLE_STRING, rtype=PORTABLE_STRING)
        def hello(self, name):
                return "Hello " + name

