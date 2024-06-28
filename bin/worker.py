#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time

class my_thread(threading.Thread):
    def __init__(self, func, args=()):
        super(my_thread, self).__init__()
        self.func = func
        self.args = args
    def run(self):
        time.sleep(2)
        self.result = self.func(*self.args)
    def get_result(self):  # 线程返回值
        threading.Thread.join(self)  # 等待线程执行完毕
        try:
            return self.result
        except Exception:
            return None