#!/usr/bin/env python
# -*- coding: utf-8 -*-
import worker
from  keepalived_install import *


def keepalived_install_only(config,username,password,port):
    for info in config:
        masterip = info[0]
        slaveip = info[1]
        vip = info[2]

    try:  
        print("keepalived install began...")
        worker1 = worker.my_thread(keepalived_install,(masterip,slaveip,port,vip,username,password));
        worker2 = worker.my_thread(keepalived_install,(slaveip,masterip,port,vip,username,password));
        worker1.start()
        worker2.start()
    
        while worker1.is_alive() or worker2.is_alive():
            sleep(5)
            print("wait to finish 5s...")

        keepalived_start(masterip, port, username, password)
        sleep(3)
        keepalived_start(slaveip, port, username, password)
        print("keepalived install fininshed...")
        
    except Exception as e:
        print(e)
        print("Error: install keepalived encountered error")

