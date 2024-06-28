if [ $# -ne 2 ];then
        echo "Usage:host_ip [online|offline_soft|offline_hard]"
	exit 1
fi
echo $2 | egrep -i "online|offline_soft|offline_hard" >/dev/null 
if [ $? -eq 0 ];then
	echo "param  check ok!"
else
	echo "Usage:host_ip [online|offline_soft|offline_hard]"
	exit 1
fi
mysql_client=/usr/local/mysql/bin/mysql
client="$mysql_client -u admin -padmin -P6032 -h127.0.0.1 -e"
host=$1
status=$2

$client "insert or ignore into  mysql_servers(hostname,max_connections) values('$host',4000);update mysql_servers set status='$status' where hostname='$host';load mysql servers from memory;save mysql servers from memory;"
