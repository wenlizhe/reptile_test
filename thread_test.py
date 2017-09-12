import threading
import time

num = 0
mutex = threading.Lock()


class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        if mutex.acquire(1):
            num = num+1
            msg = self.name+' set num to '+str(num)
            print(msg)
            mutex.release()


def test():
    for i in range(6):
        t = MyThread()
        t.start()


if __name__ == '__main__':
    test()
