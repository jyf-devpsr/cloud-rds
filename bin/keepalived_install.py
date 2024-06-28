#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import worker
import sys
from ssh_util import *
from time import sleep

keepalived_conf='''global_defs {
   router_id Ha_keepalived
}

vrrp_instance VI_1 {
    state BACKUP
    interface %s
    virtual_router_id 66
    priority 100
    advert_int 1
    unicast_src_ip %s
    unicast_peer {
       %s 
    }
    virtual_ipaddress {
       %s
    }
    notify_master "/usr/bin/python3 /etc/keepalived/scripts/keepalived_notify.py master %s %s"
    notify_backup "/usr/bin/python3 /etc/keepalived/scripts/keepalived_notify.py backup %s %s"
}
''' 

def keepalived_install( ip_local,ip_another,port,vip,username,password):
    client = get_ssh_client(ip_local, username, password, port)
    exec_cmd(client, username, "yum install -y keepalived")
    exec_cmd(client, username, "wget -O /bin/zbxcli http://zbxservice.meizu.mz/zbxcli/upgrade && chmod +x /bin/zbxcli")
    stdin,stdout,stderr = exec_cmd(client, username, "ip addr | grep " + ip_local + " | awk '{print $NF}'")
    eth = stdout.readlines()[0]
    conf= keepalived_conf % (eth,ip_local,ip_another,vip,ip_local,vip,ip_local,vip)
    exec_cmd(client, username, "echo \'" + conf +"\' > /tmp/keepalived.conf")
    exec_cmd(client, username, "mv /etc/keepalived/keepalived.conf /etc/keepalived/keepalived.conf.old")
    exec_cmd(client, username, "mv /tmp/keepalived.conf /etc/keepalived/keepalived.conf")
    exec_cmd(client, username, "mkdir -p /etc/keepalived/scripts")
    exec_cmd(client, username, "mv /root/keepalived_notify.py /etc/keepalived/scripts/keepalived_notify.py")
    exec_cmd(client, username, "chmod +x  /etc/keepalived/scripts/keepalived_notify.py")
    exec_cmd(client, username, "systemctl enable keepalived.service")
    return
    
def keepalived_start(ip,port,username,password):
    client = get_ssh_client(ip, username, password, port)
    exec_cmd(client, username, "service keepalived start")
    exec_cmd(client, username, "sed -i 's/#//g' /etc/keepalived/keepalived.conf")
    exec_cmd(client, username, "service keepalived reload")
    
def main(vip,username,password,port,masterip,slaveip):
    try:  
        print("keepalived install began...")
        worker1 = worker.my_thread(keepalived_install,(masterip,slaveip,port,vip,username,password));
        worker2 = worker.my_thread(keepalived_install,(slaveip,masterip,port,vip,username,password));
        worker1.start()
        sleep(5)
        worker2.start()
    
        while worker1.is_alive() or worker2.is_alive():
            sleep(10)
            print("wait to finish 10s...")
        keepalived_start(masterip, port, username, password)
        sleep(3)
        keepalived_start(slaveip, port, username, password)
        print("keepalived install fininshed...")
    except Exception as e:
        print("error:" % (e))
        print("error: install keepalived encountered error")
    else:
        return "keep_install_ok"
 


