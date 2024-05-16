#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/5/17 上午2:59
# file: test4.0队列如何解决实时更新.py
# author: chenruhai
# email: ruhai.chen@qq.com

import queue
import threading
import time

queue = queue.Queue()


class ThreadNum(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # 消费者端，从队列中获取num
            num = self.queue.get()
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

    # 往队列中填数据
    for num in range(10):
        queue.put(num)
        # wait on the queue until everything has been processed

    queue.join()


if __name__ == '__main__':
    main()
    time.sleep(500)