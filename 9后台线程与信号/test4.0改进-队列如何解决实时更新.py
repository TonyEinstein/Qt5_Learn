#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/5/17 上午3:03
# file: test4.0改进-队列如何解决实时更新.py
# author: chenruhai
# email: ruhai.chen@qq.com
import queue
import threading
import time

queue = queue.Queue()


class ThreadNum(threading.Thread):
    """没打印一个数字等待1秒，并发打印10个数字需要多少秒？"""

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        done = False
        while not done:
            # 消费者端，从队列中获取num
            num = self.queue.get()
            if num is None:
                done = True
            else:
                print("Retrieved", num)
            time.sleep(1)
            # 在完成这项工作之后，使用 queue.task_done() 函数向任务已经完成的队列发送一个信号
            self.queue.task_done()

        print("Consumer Finished")


def main():
    # 产生一个 threads pool, 并把消息传递给thread函数进行处理，这里开启10个并发
    for i in range(5):
        t = ThreadNum(queue)
        t.setDaemon(True)
        t.start()

    # 往队列中填错数据
    for num in range(10):
        queue.put(num)

    queue.join()
    time.sleep(10)
    for i in range(10):
        queue.put(None)
        print('None')
    time.sleep(200)


if __name__ == '__main__':
    start = time.time()
    main()
    print("Elapsed Time: %s" % (time.time() - start))