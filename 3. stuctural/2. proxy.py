import time


class Producer:
    """Define the resource intensive object to instantiate"""

    def produce(self):
        print("Producer is working hard")

    def meet(self):
        print("Producer has time to meet you now!")


class Proxy:
    """define the relatively less resouce intesive proxy to instantiate"""

    def __init__(self):
        self.occupied = "No"
        self.producer = None

    def produce(self):
        """check if producer is available"""
        print("Artist checking if produccer is available")
        if self.occupied == "No":
            # if producer is availble create the producer object!
            self.producer = Producer()
            time.sleep(2)
            # make the produccer meet the guest
            self.producer.meet()
        else:
            # otherwise don't instantiate the producer
            time.sleep(2)
            print("producer is busy!")


# Instantiate a Proxy
# proxy is one which was handaling all the request from our guests
p = Proxy()
# make the proxy: Artist produce until producer is available
p.produce()
# current state of prodcucer is not occupied that is not busy
# change the state to be "occupied"
p.occupied = "yes"
# make the producer produce
p.produce()
