#!/usr/bin/env python

import threading
from time import sleep, ctime


class Loop(object):
    def __init__(self, sec):
        self.sec = sec

    def __call__(self):
        print 'this is from loop class, time: %s' % ctime()
        sleep(self.sec)
        print 'end of loop clase, time: %s' % ctime()


def loop0():
    print 'this is loop 0, time: %s' % ctime()
    sleep(2)
    print 'loop 0 has slept for 2 sec: %s' % ctime()


def loop1():
    print 'this is loop 1, time: %s' % ctime()
    sleep(4)
    print 'loop 1 has slept for 4 sec, time: %s' % ctime()


if __name__ == '__main__':
    print 'this is main, time: %s' % ctime()
    t1 = threading.Thread(target=Loop(2))
    t2 = threading.Thread(target=Loop(4))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print 'end of main, time: %s' % ctime()
