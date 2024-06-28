if [ $# -ne 2 ];then
	echo "Usage: $0 Variable_name Value"
        echo "example: modify_config mysql-max_allowed_packet 134217728"
	exit 1
fi
variable_name=$1
value=$2
mysql_client=/usr/local/mysql/bin/mysql
client="$mysql_client -u admin -padmin -P6032 -h127.0.0.1 -e"
$client "set $variable_name=$value; show variables like '$variable_name';LOAD MYSQL VARIABLES FROM MEMORY;SAVE MYSQL VARIABLES FROM MEMORY;"
