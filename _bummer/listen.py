from communication import Udp
from Queue import Queue
from threading import Thread

def producer(out_q):
    while True:
        data = "test"
        out_q.put(data)


# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data

        data = in_q.get()
        print(data)
        # Process the data

# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()

'''
listener = Udp.Listener('10.0.2.15',5010)
listener.start()
print("Test")
'''