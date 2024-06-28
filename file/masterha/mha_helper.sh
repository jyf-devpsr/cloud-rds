#!/bin/bash
#function: mha process & status monitor
source /etc/profile
hostname=`hostname -f`
#send message
f_send_mobile_msg()
{
    /bin/zbxxxxx sms -n xxxxx,xxxxxx -m "$1"

}
masterha_home=/etc/masterha
masterha_conf=$masterha_home/proxy_app_default.cnf
ip_inner=`ifconfig -a | grep -w inet | grep -v 127.0.0.1 | egrep  "192|172|10" | awk '{print $2}'`
masterha_manager --conf=$masterha_conf --ignore_last_failover > $masterha_home/app1/stdout.log 2>&1
#mha process monitor
if [ $? -ne 0 ];then
    msginfo="$(date +'%F %H:%M:%S')  ERROR:MHA Manager process 进程异常，请尽快检查!!!  [${ip_inner}] ++++++ ${hostname}  ++++++ 返回代码:${$?} !!!"
    f_send_mobile_msg "${msginfo}"
else
    msginfo="$(date +'%F %H:%M:%S')  ${hostname}'s mha manager finished.  [${ip_inner}] ++++++ ${hostname}  ++++++ 返回代码:${$?} !!!"
    f_send_mobile_msg "${msginfo}"
fi