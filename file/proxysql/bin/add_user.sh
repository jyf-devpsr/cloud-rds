if [ $# -ne 2 ];then
	echo "Usage:add_user user password"
	exit 1
fi
user=$1
password=$2
mysql_client=/usr/local/mysql/bin/mysql
client="$mysql_client -u admin -padmin -P6032 -h127.0.0.1 -e"
$client "insert into mysql_users(username,password) values('$user','$password');LOAD MYSQL USERS FROM MEMORY;SAVE MYSQL USERS FROM MEMORY; "
