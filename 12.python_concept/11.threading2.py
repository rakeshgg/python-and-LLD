from threading import Thread, Lock
from time import sleep

mutex = Lock()
# wait for lock to be availabel
# waiting operations
mutex.acquire()
mutex.release()


def t1(lock):
    print(" starting t1")
    lock.acquire()
    sleep(1)
    print("t1")
    lock.release()


def t2(lock):
    print(" starting t2")
    lock.acquire()
    sleep(1)
    print("t2")
    lock.release()


lock = Lock()
thread1 = Thread(target=t1, args=(lock,))
thread2 = Thread(target=t2, args=(lock,))
thread1.start()
thread2.start()


def print_values(values, start_lock, end_lock, name):
    for item in values:
        print(f"{name} waiting for locks")
        start_lock.acquire()
        print(item)
        end_lock.release()


lock1 = Lock()
lock2 = Lock()
lock2.acquire()

thread1 = Thread(target=print_values, args=([1, 3, 5], lock1, lock2, "t1"))
thread2 = Thread(target=print_values, args=([2, 4], lock2, lock1, "t2"))
thread1.start()
thread2.start()

# want to print 1,2,3,4,5 in order
# thrad synchronisation

"""
Join

"""


def start_game(preq=[]):
    print("waiting to start game")
    for t in preq:
        t.join()
    print("started game")


def load_assests():
    print("loaded assets")
    sleep(2)


def load_player():
    sleep(1)
    print("loaded player")


load_assests_thread = Thread(target=load_assests)
load_player_thread = Thread(target=load_player)
preq = [load_player_thread, load_assests_thread]
start_game_thread = Thread(target=start_game, args=(preq,))
# when to start this thread
# start_game_thread.start()
load_assests_thread.start()
load_player_thread.start()
start_game_thread.start()

"""
when to use Locks
when to use delay
when to use .join - wait to finsih before you continue

"""

# deadLocks - No thread able to execute


def wait_on_threads(threads):
    sleep(1)
    for thread in threads:
        thread.join()
    print("Ran")


threads = []
t1 = Thread(target=wait_on_threads, args=(threads,))
t2 = Thread(target=wait_on_threads, args=([t1],))
# putting here as t2 is not created above so using list
threads.append(t2)
t1.start()
t2.start()
