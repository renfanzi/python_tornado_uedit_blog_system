#!/usr/bin/env python
# -*- coding:utf-8 -*-
from  multiprocessing import Process, Pool
import multiprocessing
import time, sys
# -----<计时器>----- #
def timer(arg):
    '''
    use method：
        timer(14)

    :param arg: 倒计时时间
    :return: True
    '''
    # 倒计时时间
    back_time = arg
    while back_time != 0:
        sys.stdout.write('\r')  ##意思是打印在清空
        back_time -= 1
        sys.stdout.write("%s" % (int(back_time)))
        sys.stdout.flush()
        time.sleep(1)
    return True


# -----<任务函数>----- #
def slow_worker():
    '''
    你的自定义任务， 需要执行的代码
    :return:
    '''
    print('Starting worker')
    time.sleep(4)
    print('Finished worker')

def abc(countdown=2):
    p = multiprocessing.Process(target=slow_worker)
    p.start()
    if countdown:
        status = timer(countdown)
        if status:
            p.terminate()


def Foo(fi):

    abc()



if __name__ == '__main__':
    from gevent import monkey;monkey.patch_all()
    import gevent


    gevent.joinall([
        gevent.spawn(Foo),
        gevent.spawn(Foo),
        gevent.spawn(Foo),
    ])