#!/bin/bash
#function the script is backup mysql 
source /etc/profile
username='xxxxxxxxxxxx'
password='xxxxxxxxxxxxxxxxxxxx'
host=@slavehost
socket=/tmp/mysql.sock
basedir=/usr/local/mysql/bin
mydmper_command=`which mydumper`
thread_num=4
hostname=`hostname`
datadir=/@data_dir/mysql/flyme_cloud_mysql/@mzbackupdir
backupdir=${datadir}/`date '+%Y%m%d'`
backuplogfile=${backupdir}/backup_`date '+%Y%m%d'`.log
lsavetime=@keep_days
ip=`ifconfig | grep -E '(10.140)' | awk '{print $2}' | sed 's/\s//g'`
#send message
f_send_mobile_msg()
{
    /bin/xxxxxxxxxxxx sms -n xxxxxxxxxxxxxx,xxxxxxxxxxxxxxxx -m "$1"

}

#make backup directory
if [ ! -d ${backupdir} ];then
   mkdir -p ${backupdir}
fi

#begin backup

###############################################################
${mydmper_command} --user=${username} --password=${password} --host=${host} --port=3306 --socket=${socket} --skip-tz-utc --threads=${thread_num}  --compress-protocol  --triggers --routines --events --compress --regex '^(?!(performance_schema|information_schema|sys))' --outputdir=${backupdir} --logfile=${backuplogfile}
rstcode=$?
if  [ ${rstcode} -ne 0 ]; then
    msginfo="$(date +'%F %H:%M:%S') ERROR:mydumper备份失败!!! [${ip}]+++ ${hostname}+++请检查备份日志：${backuplogfile} 返回代码:${rstcode},脚本退出!"
    f_send_mobile_msg "${msginfo}"
    exit 2
fi
###############################################################

#remove file
if [ -d ${datadir} ];then
   find ${datadir} -mindepth 1 -maxdepth 1 -type d -mtime +${lsavetime} -exec rm -rf {} \;
fi