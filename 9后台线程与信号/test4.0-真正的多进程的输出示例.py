#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2024/5/16 上午10:07
# file: test4.0-真正的多进程的输出示例.py
# author: chenruhai
# email: ruhai.chen@qq.com
import multiprocessing as mp
import time
import random

def expensive_calculation(x):
    result = x * x
    time.sleep(random.uniform(0.5, 1.5))  # 模拟耗时操作
    """
    可以看到这里打印的时候并不是按照0~9的顺序打印，是无序的，因为后台是在进行多进程。
    """
    print(f"Process {mp.current_process().name}: Calculated {x} * {x} = {result}")
    return result

if __name__ == '__main__':
    with mp.Pool(processes=5) as pool:
        results = pool.map(expensive_calculation, range(10))
        print("All calculations done:")
        # for result in results:
        #     print(result)
