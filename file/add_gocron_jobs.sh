#!/bin/sh

# 然后再进行添加定时任务 Auth-Token 换成登录成功得到的token即可
curl 'http://xxxxxxx:5921/api/task/store' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: zh-CN,zh;q=0.9' \
  -H 'Auth-Token: @gocron_token' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Origin: http://xxxxxxx:5921' \
  -H 'Pragma: no-cache' \
  -H 'Referer: http://xxxxxxx:5921/' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
  -d 'id=&name=@rds_id&tag=Flyme_MySQL_Backup&level=1&dependency_status=1&dependency_task_id=&spec=1%201%20@backup_hour%20%2A%20%2A%20%2A&protocol=2&http_method=1&command=/usr/bin/bash /opt/gocron/shell_script/flyme_mydumper_backup_gocron.sh "@slaveip"&host_id=@my_host_id&timeout=0&multi=2&notify_status=1&notify_type=2&notify_receiver_id=&notify_keyword=&retry_times=0&retry_interval=0&remark=mark' \
  --insecure