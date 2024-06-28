if [ $# -ne 1 ];then
        echo "Usage:drop_user user"
        exit 1
fi
user=$1
mysql_client=/usr/local/mysql/bin/mysql
client="$mysql_client -u admin -padmin -P6032 -h127.0.0.1 -e"
$client "delete from mysql_users where username='$user';LOAD MYSQL USERS FROM MEMORY;SAVE MYSQL USERS FROM MEMORY; "