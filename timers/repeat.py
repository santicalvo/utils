import threading;
i = 0
def work ():
    global i
    t = threading.Timer(0.1, work)
    t.start ();
    i +=1
    print "stackoverflow ", i;
    if (i>10):
        t.cancel()

def repeat_func(fun, time, limit=11):
    print i, time, limit
    def repeat_deco(*args):
        num = args[0]
        num -= 1
        t = threading.Timer(time, repeat_deco, [num, 100])
        if(num >0):
            t.start()
            fun(num)
        else:
            t.cancel()
    repeat_deco(limit)

def print_hw(n):
    print "hello world!", n

def count100(*args):
    for i in xrange(100):
        print i, args

if __name__ == '__main__':
    #work ();
    repeat_func(print_hw, 1)
    repeat_func(count100, 1, 5)