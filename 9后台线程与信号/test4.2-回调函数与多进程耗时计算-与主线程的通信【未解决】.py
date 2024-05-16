#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/5/16 上午10:03
# file: test4.2-回调函数与多进程耗时计算-与主线程的通信【未解决】.py.py
# author: chenruhai
# email: ruhai.chen@qq.com
import multiprocessing as mp
import time

def worker(callback):
    for i in range(10):
        callback(f'Processing item {i}')
        time.sleep(1)

def callback_function(message):
    print(message)

if __name__ == '__main__':
    processes = []
    for _ in range(3):
        process = mp.Process(target=worker, args=(callback_function,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()
