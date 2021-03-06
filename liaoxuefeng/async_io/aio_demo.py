#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/17 22:11'


"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432090171191d05dae6e129940518d1d6cf6eeaaa969000

协程，又称微线程，纤程。英文名Coroutine。

协程的特点在于是一个线程执行

协程最大的优势就是协程极高的执行效率。因为子程序切换没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。

第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。

套用Donald Knuth的一句话总结协程的特点: 子程序就是协程的一种特例

因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。
"""


# 传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。

# 如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高

def consumer():  # 0.1 consumer函数是一个generator
    r = ''
    while True:
        n = yield r  # 3. consumer通过yield拿到消息，处理，又通过yield把结果传回
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):  # 0.2 把一个consumer传入produce后
    c.send(None)  # 1. 首先调用c.send(None)启动生成器   2. 一旦生产了东西，通过c.send(n)切换到consumer执行
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)  # 4. produce拿到consumer处理的结果，继续生产下一条消息
    c.close()  # 5. produce决定不生产了，通过c.close()关闭consumer，整个过程结束。


c = consumer()
produce(c)

# 整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
