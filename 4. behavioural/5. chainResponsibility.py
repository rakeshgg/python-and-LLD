"""
"""


class Handler:
    # Abstarct handler
    def __init__(self, successor):
        # define who is the next handler
        self._successor = successor

    def handle(self, request):
        handled = self._handle(request)
        # if handle stop here
        # otherwise keep going
        if not handled:
            # using succesor
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError("Must provide implementation in subclass")


class ConcreteHandler1(Handler):
    # inherit from abstarct handler
    """Concrete Handler1"""

    def _handle(self, request):
        if 0 < request <= 10:  # provide a condition for handling
            print("Request {} handled in handler1".format(request))
            return True  # Indicates the request has been handled


class DefaultHandler(Handler):
    # inherit from abstarct handler
    """Default handler"""

    def _handle(self, request):
        """if there is no handler available"""
        # No condition checking since this is default handler
        print("End of chain, no handler for {}".format(request))
        return True  # Indicates the request has been handled


class Client:  # using handlers
    def __init__(self):
        # create a handler and use in sequence you want
        # ConcreteHandler1 need to specify who is
        # its succesor which is DefaultHandler
        # DefaultHandler has no succesor so use None
        self.handler = ConcreteHandler1(DefaultHandler(None))

    def delegate(self, requests):
        # send your request one at a time for handler
        for request in requests:
            self.handler.handle(request)


# Create a Client
c = Client()
# Create a Requests
requests = [2, 5, 30]
# send the request
c.delegate(requests)
"""
The chain of Responsibility pattern
is used not to tie with specific solution request
that is well demonestrated in example
"""
