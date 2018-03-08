import threading
import time
import datetime


num = 0
# mutex = threading.Lock()


# class MyThread(threading.Thread):
#     def run(self):
#         global num
#         time.sleep(1)
#
#         if mutex.acquire(1):
#             num = num+1
#             msg = self.name+' set num to '+str(num)
#             print(msg)
#             mutex.release()


def output_a(event, next_event):
    for i in range(5):
        event.wait()
        print('a')
        event.clear()
        next_event.set()


def output_b(event, next_event):
    for i in range(5):
        event.wait()
        print('b')
        event.clear()
        next_event.set()


def output_c(event, next_event):
    for i in range(5):
        event.wait()
        print('c')
        event.clear()
        next_event.set()


if __name__ == '__main__':
    # for x in range(3):
    a_event = threading.Event()
    b_event = threading.Event()
    c_event = threading.Event()

    a_thread = threading.Thread(target=output_a, args=(a_event, b_event))
    b_thread = threading.Thread(target=output_b, args=(b_event, c_event))
    c_thread = threading.Thread(target=output_c, args=(c_event, a_event))

    a_thread.start()
    b_thread.start()
    c_thread.start()

    a_event.set()
