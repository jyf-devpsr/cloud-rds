#!/bin/bash
#function: mha process & status monitor
source /etc/profile
host=xxxxxxx
hostname=`hostname -f`
ip=`ifconfig | grep -E '(10.140)' | awk '{print $2}' | sed 's/\s//g'`
timeout=5
#send message
f_send_mobile_msg()
{
    /bin/zbxcli sms -n xxxxxxx,xxxxxxx -m "$1"

}

(masterha_check_status --conf=/etc/masterha/proxy_app_default.cnf > /tmp/mha_mz_ping_ok ) &
sleep $timeout
mha_check_res=`grep -E "PING_OK" /tmp/mha_mz_ping_ok |wc -l`
if  [ ${mha_check_res} -ne 1 ]; then
    msginfo="$(date +'%F %H:%M:%S') ERROR:MHA Manager status check 状态异常，请尽快检查!!! [${ip}] ++++++  ${hostname} ++++++  返回代码:${mha_check_res} !!!"
    f_send_mobile_msg "${msginfo}"
    exit 2
fi
echo "" > /tmp/mha_mz_ping_ok
