#!/bin/sh

curl 'http://xxxxxxxxxxxx:5921/api/user/login' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: zh-CN,zh;q=0.9' \
  -H 'Auth-Token;' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Origin: http://xxxxxxx:5921' \
  -H 'Pragma: no-cache' \
  -H 'Referer: http://xxxxxxx:5921/' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
  -d 'username=gocron&password=Zh715D_F9vUl7HpX' \
  --insecure