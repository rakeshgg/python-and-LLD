"""
How to create New thread in Python and run concurent programes.

"""

import threading
from time import sleep


# define target as a functions where this thread runs
def run(content):
    print(content)


# new thread created
# thread1 = threading.Thread(target=run, args=("run",))
# thread2 = threading.Thread()
# run the thread
# activate the thread and make runing
# thread1.start()
# In python atleat one thread is runing when i run my programe
# we create new python process and gives python interpreter
# associated to this process. activate the main thread
# main thread is thread which is runing for all this codes.
# each process can run parallel not thread in a process

# multiple threads
thread1 = threading.Thread(target=run, args=("run1",))
thread2 = threading.Thread(target=run, args=("run2",))
thread1.start()
thread2.start()
# when run the code main thread got activated and created two threads
# making thread active make it start


# adding delay
def run2(content, delay=1):
    # sleep for some time 1 sec
    sleep(delay)
    # thread 1 sleep here so main thread to start
    # 2nd Thread delay which excutes fastest keep exceuting that threads
    print(content)


thread1 = threading.Thread(target=run2, args=("run1", 2))
thread2 = threading.Thread(target=run2, args=("run2", 1))
thread1.start()
thread2.start()
"""
run2
run1
"""

"""
Run something on Thread one don't start thread
two until thread1 is done.
thread.join() - wait for thread 1 to finish

"""

thread1 = threading.Thread(target=run2, args=("run1", 1))
thread2 = threading.Thread(target=run2, args=("run2", 1))
thread1.start()
print("main thread")
# control goes to thread1 as its still sleeping
thread1.join()
print(threading.active_count())
thread2.start()
print(threading.active_count())

"""
How many thread are active, executed
threading.active_count()

"""


def print_values(values, delay):
    for item in values:
        print(item)
        sleep(delay)


thread1 = threading.Thread(target=print_values, args=([1, 3, 5], 0.2))
thread2 = threading.Thread(target=print_values, args=([2, 4], 0.3))
thread1.start()
thread2.start()

"""
Locks

"""
