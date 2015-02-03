import os
from time import time

def timereps(reps, func):
    start = time()
    for i in range(0, reps):
        func()
    end = time()
    return (end - start) / reps

def count10():
    start = time()
    n = start
    while n - start <10:
        print "n: ", n - start
        n = time()

if __name__ == '__main__':
    count10()
    #listdir_time = timereps(10000, lambda: os.listdir('/'))
    #print "python can do %d os.listdir('/') per second" % (1 / listdir_time)