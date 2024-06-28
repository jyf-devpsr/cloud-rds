#!/bin/bash

wget_timeout=3
wget_server="xxxxxxx:8080"
wget_root="software/n9e"
curl --connect-timeout 2 "http://${wget_server}" &>> /dev/null
if [[ $? -ne 0 ]];then
    wget_server="xxxxxxx:8080"
fi
wget_cmd="wget --no-verbose --tries=2 --timeout=${wget_timeout} http://${wget_server}/${wget_root}/"

user='prometheus'

if [[ ! -e "/etc/redhat-release" ]];then
    echo "unsupport system."
    exit 2
fi

if [[ -e "/usr/bin/systemctl" ]];then
    osrelease=7
else
    osrelease=6
fi


echo "os release ${osrelease}"

id $user &>> /dev/null
if [[ $? -ne 0 ]];then
    useradd $user -s /bin/bash
fi

function downloadFile(){
    local filename=$1
    local basefilename=`basename ${filename}`
    if [[ -e $basefilename && -s $basefilename ]];then 
		return 0;
	fi

	which wget &>>/dev/null
	if [[ $? -ne 0 ]];then 
		yum install -y wget
		if [[ $? -ne 0 ]];then echo "yum install wget failed.";exit 2;fi
	fi
	${wget_cmd}${filename} -O ${basefilename}
    
    if [[ (! -e ${basefilename}) || (! -s ${basefilename}) ]];then
        echo "download file ${basefilename} failed."
        exit 4
    fi
}


function installNodeExporter(){

    ps -ef | grep -v grep | grep -wq node_exporter
    if [[ $? -ne 0 ]];then
        echo "node_exporter not exists, install"
    else
        echo "node_exporter already installed, skip"
        return 0
    fi
	
    binDir="/usr/local/node_exporter/bin"
    textfileDir="/usr/local/node_exporter/textfile"
	
	if [[ ! -d "$binDir" ]];then mkdir -p "$binDir";fi
    if [[ ! -d "$textfileDir" ]];then mkdir -p "$textfileDir";fi
	
    cd $binDir
	
    if [[ ! -e "node_exporter" ]];then
        downloadFile "node_exporter"
    fi
    
    chmod +x ./node_exporter
    if [[ $osrelease -ge 7 ]];then
        echo "[Unit]
Description=node exporter service
Documentation=https://prometheus.io
After=network.target

[Service]
Type=simple
User=root
Group=root
LimitNOFILE=500000
ExecStart=${binDir}/node_exporter --collector.textfile.directory=${textfileDir}
Restart=always

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/node_exporter.service
        systemctl daemon-reload
        systemctl restart node_exporter
        systemctl enable node_exporter
    else
        nohup ${binDir}/node_exporter --collector.textfile.directory=${textfileDir} &>>/dev/null &
        grep -wq "node_exporter" /etc/rc.local
        if [[ $? -ne 0 ]];then
            sed -i '$a \'"${binDir}"'/node_exporter --collector.textfile.directory='${textfileDir}' &>>/tmp/node_exporter.log &' /etc/rc.local
        fi
    fi  
    
    ps -ef | grep -v grep | grep -wq node_exporter
    if [[ $? -eq 0 ]];then
        echo "start node_exporter successfully"'!'
    else
        echo "start node_exporter failed."
        exit 4
    fi
    
}

function removeNodeExporter(){
    if [[ $osrelease -ge 7 ]];then
        systemctl stop node_exporter
        systemctl disable node_exporter
    else
        ps -ef | awk '/node_exporter/{print $2}' | xargs kill -9
        grep -wq "node_exporter" /etc/rc.local
        if [[ $? -eq 0 ]];then
            sed -i /node_exporter/d /etc/rc.local
        fi
    fi
    ps -ef | grep -v grep | grep -wq node_exporter
    if [[ $? -ne 0 ]];then
        #rm -rf /usr/local/node_exporter
        echo "finish to stop node_exporter"'!'
    else
        echo "stop node_exporter failed."
        exit 4
    fi
}



function installRedisExporter(){
    basedir="/usr/local/redis_exporter"
    binDir="$basedir/bin"
    etcDir="$basedir/etc"
    
    ps -ef | grep -v grep | grep -wq redis_exporter
    if [[ $? -eq 0 ]];then
        echo "redis_exporter started.skipping..."
    fi
    
    if [[ ! -d "$binDir" ]];then mkdir -p "$binDir";fi
    if [[ ! -d "$etcDir" ]];then mkdir -p "$etcDir";fi
    cd $binDir
    if [[ ! -e "redis_exporter" || ! -s "redis_exporter" ]];then
        downloadFile "redis_exporter"
    fi
    chmod +x ./redis_exporter
    if [[ $osrelease -ge 7 ]];then
        echo "[Unit]
Description=redis exporter service
Documentation=https://prometheus.io
After=network.target

[Service]
Type=simple
User=$user
Group=$user
LimitNOFILE=500000
ExecStart=${binDir}/redis_exporter -web.listen-address 0.0.0.0:9378
Restart=always

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/redis_exporter.service
        systemctl daemon-reload
        systemctl restart redis_exporter
        systemctl enable redis_exporter
        
    else
        su - $user -c "${binDir}/redis_exporter -web.listen-address 0.0.0.0:9378 &>>/tmp/redis_exporter.log &"
        grep -wq "redis_exporter" /etc/rc.local
        if [[ $? -ne 0 ]];then
            sed -i '$a \/bin/su - '"$user"' -c "'"${binDir}/"'redis_exporter -web.listen-address 0.0.0.0:9378 &>>/tmp/redis_exporter.log &"' /etc/rc.local
        fi
    fi
    
    ps -ef | grep -v grep | grep -wq redis_exporter
    if [[ $? -eq 0 ]];then
        echo "start redis_exporter successfully"'!'
    else
        echo "start redis_exporter failed."
        exit 4
    fi
    
}


function removeRedisExporter(){
    if [[ $osrelease -ge 7 ]];then
        systemctl stop redis_exporter
        systemctl disable redis_exporter
    else
        ps -ef | awk '/redis_exporter/{print $2}' | xargs kill -9 &>/dev/null
        grep -wq "redis_exporter" /etc/rc.local
        if [[ $? -eq 0 ]];then
            sed -i /redis_exporter/d /etc/rc.local
        fi
    fi
    
    ps -ef | grep -v grep | grep -wq redis_exporter
    if [[ $? -ne 0 ]];then
        #rm -rf /usr/local/redis_exporter
        echo "finish to stop redis_exporter"'!'
    else
        echo "stop redis_exporter failed."
        exit 4
    fi
}





function createExporterUser(){
    export MYSQL_PWD='sql1064PLMASD.!@#'
    
    local port_="$1"
    local MySQLAddress="$2"
    local host_="127.0.0.1"
    
    if [[ "x$MySQLAddress" == "x" ]];then
        MySQLAddress="$host_"
    fi
    #socketName="sock"
    #if [[ -e "/tmp/mysql-3306.socket" ]];then
    #    socketName="socket"
    #fi
    
    local mysqlBin="mysql"
    local preSql="set sql_log_bin=off;"
    local afterSql=""
    #local mysqlBin="/usr/local/mysql5.7/bin/mysql"
    #local mysqlCMDS="$mysqlBin -S /tmp/mysql-${port_}.${socketName} -N -s -e"
    #local mysqlCMD="$mysqlBin -S /tmp/mysql-${port_}.${socketName}"
    
    
    if [[ ! -d "/data/mysql/mysql_3306" ]];then
        host_="localhost"
    fi
    local mysqlCMDS="$mysqlBin -h${host_} -P${port_} -N -s -e"
    local mysqlCMD="$mysqlBin -h${host_} -P${port_} -vvv"
    
    tabRows=$($mysqlCMDS "select count(1) from mysql.user where user='p8s_exporter' and host='$MySQLAddress';" 2>&1)
    if [[ ! "x$(echo $tabRows |sed 's#[0-9]##g')" == "x" ]];then
        echo "connect to MySQL server ${port_} failed. $tabRows"
        return 1
    fi
    
    validateInfo=$($mysqlCMDS "show variables like 'validate_password_policy';" 2>&1)
    if [[ "x$(echo $validateInfo | awk '{print $1}')" == "xvalidate_password_policy" ]];then
        preSql="$preSql;set global validate_password_policy='LOW';"
        afterSql="set global validate_password_policy='$(echo $validateInfo | awk '{print $2}')';"
    fi
    
    
    if [[ $tabRows -eq 0 ]];then
        ${mysqlCMD}<<EOF
$preSql
create user 'p8s_exporter'@'$MySQLAddress' identified by 'meizu.com';
GRANT PROCESS, REPLICATION CLIENT, SELECT ON *.* TO 'p8s_exporter'@'$MySQLAddress';
$afterSql
EOF
    else
        echo "MySQL server ${port_} user 'p8s_exporter'@'$MySQLAddress' have been created."
        return 0
    fi
    
    tabRows=$($mysqlCMDS "select count(1) from mysql.user where user='p8s_exporter' and host='$MySQLAddress';" 2>&1)
    if [[ $tabRows -eq 0 ]];then
        echo "MySQL server ${port_} user 'p8s_exporter'@'$MySQLAddress' create fail"'!'
    else
        echo "MySQL server ${port_} user 'p8s_exporter'@'$MySQLAddress' created."
        return 0
    fi
    
}



function installMysqlExporter(){
    local MySQLAddress=""
    
    if [[ -d "/data/mysql/mysql_3306" ]];then
        MySQLAddress="127.0.0.1"
    else
        MySQLAddress="`hostname -I |awk '{print $1}'`"
    fi
    
	ps -ef | grep -v grep | grep -wq mysqld_exporter
    if [[ $? -ne 0 ]];then
        echo "mysqld_exporter not exists, install"
    else
        echo "mysqld_exporter already installed, skip"
        
		return 0
    fi
    
    binDir="/usr/local/mysqld_exporter/bin"
	if [[ ! -d "$binDir" ]];then mkdir -p "$binDir";fi
	
    if [[ ! -d "/usr/local/mysqld_exporter/etc" ]];then mkdir -p /usr/local/mysqld_exporter/etc;fi
    echo "[client]
host=${MySQLAddress}
user=p8s_exporter
password=meizu.com" > /usr/local/mysqld_exporter/etc/mysqld_exporter.cnf
   
    cd $binDir
	
    if [[ ! -e "mysqld_exporter" ]];then
        downloadFile "mysqld_exporter"
    fi
    chmod +x ./mysqld_exporter
    
    if [[ $osrelease -ge 7 ]];then
        echo "[Unit]
Description=mysql exporter service
Documentation=https://prometheus.io
After=network.target

[Service]
Type=simple
User=$user
Group=$user
LimitNOFILE=500000
ExecStart=${binDir}/mysqld_exporter --config.my-cnf=/usr/local/mysqld_exporter/etc/mysqld_exporter.cnf \
--web.listen-address=0.0.0.0:9306 \
--collect.slave_status \
--collect.binlog_size \
--collect.info_schema.processlist \
--collect.info_schema.innodb_metrics \
--collect.engine_innodb_status \
--collect.perf_schema.file_events \
--collect.perf_schema.replication_group_member_stats
Restart=always

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/mysqld_exporter.service
        systemctl daemon-reload
        systemctl restart mysqld_exporter.service
        systemctl enable mysqld_exporter.service
    else
        su - $user -c "${binDir}/mysqld_exporter --config.my-cnf=/usr/local/mysqld_exporter/etc/mysqld_exporter.cnf \
--web.listen-address=0.0.0.0:9306 \
--collect.slave_status \
--collect.binlog_size \
--collect.info_schema.processlist \
--collect.info_schema.innodb_metrics \
--collect.engine_innodb_status \
--collect.perf_schema.file_events \
--collect.perf_schema.replication_group_member_stats &>>/tmp/mysqld_exporter.log &"
        grep -wq "mysqld_exporter" /etc/rc.local
        if [[ $? -ne 0 ]];then
            sed -i '$a \/bin/su - '"$user"' -c "'"${binDir}/"'mysqld_exporter --config.my-cnf=/usr/local/mysqld_exporter/etc/mysqld_exporter.cnf --web.listen-address=0.0.0.0:9306 --collect.slave_status --collect.binlog_size --collect.info_schema.processlist --collect.info_schema.innodb_metrics --collect.engine_innodb_status --collect.perf_schema.file_events --collect.perf_schema.replication_group_member_stats &>>/tmp/mysqld_exporter.log &"' /etc/rc.local
        fi
    
    fi
    
    
    ps -ef | grep -v grep | grep -wq mysqld_exporter
    if [[ $? -eq 0 ]];then
        echo "start mysqld_exporter successfully"'!'
    else
        echo "start mysqld_exporter failed."
        exit 4
    fi
}

function removeMysqlExporter(){
    if [[ $osrelease -ge 7 ]];then
        systemctl stop mysqld_exporter
        systemctl disable mysqld_exporter
    else
        ps -ef | awk '/mysqld_exporter/{print $2}' | xargs kill -9 &>/dev/null
        grep -wq "mysqld_exporter" /etc/rc.local
        if [[ $? -eq 0 ]];then
            sed -i /mysqld_exporter/d /etc/rc.local
        fi
    fi
}




function installMongodbExporterReplica(){
    basedir="/usr/local/mongodb_exporter"
    binDir="$basedir/bin"
    etcDir="$basedir/etc"
    localIp=$(hostname -I | awk '{print $1}')
    

    
    if [[ ! -d "$binDir" ]];then mkdir -p "$binDir";fi
    if [[ ! -d "$etcDir" ]];then mkdir -p "$etcDir";fi
    cd $binDir
    if [[ ! -e "mongodb_exporter" || ! -s "mongodb_exporter" ]];then
        downloadFile "mongodb_exporter"
    fi
    chmod +x ./mongodb_exporter

    if [[ $osrelease -ge 7 ]];then
        echo "[Unit]
Description=mongodb exporter service
Documentation=https://github.com/percona/mongodb_exporter
After=network.target

[Service]
Type=simple
User=$user
Group=$user
LimitNOFILE=500000
ExecStart=${binDir}/mongodb_exporter --web.listen-address=:9216 --collect-all --compatible-mode --mongodb.uri=mongodb://p8s_exporter:meizu.com@${localIp}:27017/admin
Restart=always

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/mongodb_exporter.service
        systemctl daemon-reload
        systemctl restart mongodb_exporter.service
        systemctl enable mongodb_exporter.service
        
    else
        su - $user -c "${binDir}/mongodb_exporter --web.listen-address=:9216 --collect-all --compatible-mode --mongodb.uri=mongodb://p8s_exporter:meizu.com@${localIp}:27017/admin &>>/tmp/mongodb_exporter.log &"
        grep -wq "mongodb_exporter" /etc/rc.local
        if [[ $? -ne 0 ]];then
            sed -i '$a \/bin/su - '"$user"' -c "'"${basedir}/bin/"'mongodb_exporter --web.listen-address=:9216 --collect-all --compatible-mode --mongodb.uri=mongodb://p8s_exporter:meizu.com@'${localIp}':27017/admin &>>/tmp/mongodb_exporter.log &"' /etc/rc.local
        fi
    fi

    ps -ef | grep [m]ongodb_exporter 
    if [[ $? -eq 0 ]];then
        echo "start mongodb_exporter successfully"'!'
    else
        echo "start mongodb_exporter failed."
        exit 4
    fi
    
}


function installMongodbExporterShard(){
    basedir="/usr/local/mongodb_exporter"
    binDir="$basedir/bin"
    etcDir="$basedir/etc"
    localIp=$(hostname -I | awk '{print $1}')
    
    #目前仅安装mongos监控
    declare -A mongoExporter
    mongoExporter['mongos']="9216"
    #mongoExporter['config']="9217"
    #mongoExporter['shard']="9218"
    
    

    echo ${!mongoExporter[@]}
    
    if [[ ! -d "$binDir" ]];then mkdir -p "$binDir";fi
    if [[ ! -d "$etcDir" ]];then mkdir -p "$etcDir";fi
    cd $binDir
    if [[ ! -e "mongodb_exporter" || ! -s "mongodb_exporter" ]];then
        downloadFile "mongodb_exporter"
    fi
    chmod +x ./mongodb_exporter
    
    
    
    for mongoUnit in ${!mongoExporter[@]};do
        
        ps -ef | grep -v grep | grep -q ${mongoUnit}
        if [[ $? -ne 0 ]];then echo "failed to get [$mongoUnit] proceess pid.";exit 4;fi
        
        mongoPid=`ps -ef | grep -v grep | grep ${mongoUnit} | awk '{print $2}' | head -1`
        if [[ "x$mongoPid" == "x" ]];then echo "failed to get [$mongoUnit] proceess pid...";exit 5;fi
        
        
        netstat -tnlp | grep -q "${mongoPid}/"
        if [[ $? -ne 0 ]];then echo "failed to get [$mongoUnit] port.";exit 4;fi
        
        mongoPort=`netstat -tnlp | grep "${mongoPid}/" | awk '{print $4}' |cut -d ":" -f2`
        if [[ "x$mongoPort" == "x" ]];then echo "failed to get [$mongoUnit] port...";exit 5;fi
        
        if [[ $osrelease -ge 7 ]];then
            echo "[Unit]
Description=mongodb exporter service(${mongoUnit})
Documentation=https://github.com/percona/mongodb_exporter
After=network.target

[Service]
Type=simple
User=$user
Group=$user
LimitNOFILE=500000
ExecStart=${binDir}/mongodb_exporter --web.listen-address=:${mongoExporter[$mongoUnit]} --collect-all --compatible-mode --mongodb.uri=mongodb://p8s_exporter:meizu.com@${localIp}:${mongoPort}/admin
Restart=always

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/${mongoUnit}_exporter.service
            systemctl daemon-reload
            systemctl restart ${mongoUnit}_exporter.service
            systemctl enable ${mongoUnit}_exporter.service
            
        else
            su - $user -c "${binDir}/mongodb_exporter --web.listen-address=:${mongoExporter[$mongoUnit]} --collect-all --compatible-mode --mongodb.uri=mongodb://p8s_exporter:meizu.com@${localIp}:${mongoPort}/admin &>>/tmp/mongodb_exporter_${mongoPort}.log &"
            grep -wq "mongodb_exporter_${mongoPort}" /etc/rc.local
            if [[ $? -ne 0 ]];then
                sed -i '$a \/bin/su - '"$user"' -c "'"${basedir}/bin/"'mongodb_exporter  --web.listen-address=:'${mongoExporter[$mongoUnit]}' --collect-all --compatible-mode --mongodb.uri=mongodb://p8s_exporter:meizu.com@'${localIp}':'${mongoPort}'/admin &>>/tmp/mongodb_exporter_'${mongoPort}'.log &"' /etc/rc.local
            fi
        fi
    
        ps -ef | grep [m]ongodb_exporter | grep -wq ${mongoExporter[$mongoUnit]}
        if [[ $? -eq 0 ]];then
            echo "start mongodb_exporter [${mongoUnit}:${mongoPort}] successfully"'!'
        else
            echo "start mongodb_exporter [${mongoUnit}:${mongoPort}] failed."
            exit 4
        fi
    done
    
}



function installMongodbExporter(){
    ps -ef  | grep mongodb | grep -v grep| grep -q "config"
    if [[ $? -eq 0 ]];then
        installMongodbExporterShard
    else
        installMongodbExporterReplica
    fi
}


function createExporterUserHandler(){
    if [[ -d "/data/mysql/mysql_3306" ]];then
        while read lines;do
            port=`echo $lines | awk -F'_' '{print $2}'`
            if [[ ! "x$(echo $port |sed 's#[0-9]##g')" == "x" ]];then
                echo "invalid MySQL server port: [${port}] skipping...."
                continue
            fi
            createExporterUser $port
        done < <(ls /data/mysql/)
    else
        createExporterUser "3306" "`hostname -I |awk '{print $1}'`"
    fi
}





function installMysqlProxyExporter(){
    basedir="/usr/local/mysqlproxy_exporter"
    binDir="$basedir/bin"
    etcDir="$basedir/etc"
    
    ps -ef | grep -v grep | grep -wq redis_exporter
    if [[ $? -eq 0 ]];then
        echo "mysqlproxy_exporter started.skipping..."
    fi
    
    if [[ ! -d "$binDir" ]];then mkdir -p "$binDir";fi
    if [[ ! -d "$etcDir" ]];then mkdir -p "$etcDir";fi
    cd $binDir
    if [[ ! -e "mysqlproxy_exporter" || ! -s "mysqlproxy_exporter" ]];then
        downloadFile "mysqlproxy_exporter"
    fi
    chmod +x ./mysqlproxy_exporter
    if [[ $osrelease -ge 7 ]];then
        echo "[Unit]
Description=mysql proxy exporter service
Documentation=https://prometheus.io
After=network.target

[Service]
Type=simple
User=$user
Group=$user
LimitNOFILE=500000
ExecStart=${binDir}/mysqlproxy_exporter -web.listen-address 0.0.0.0:9306
Restart=always

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/mysqlproxy_exporter.service
        systemctl daemon-reload
        systemctl enable mysqlproxy_exporter
        systemctl restart mysqlproxy_exporter
        
    else
        /bin/su - $user -c "${binDir}/mysqlproxy_exporter -web.listen-address 0.0.0.0:9306 &>>/tmp/mysqlproxy_exporter.log &"
        grep -wq "mysqlproxy_exporter" /etc/rc.local
        if [[ $? -ne 0 ]];then
            sed -i '$a \/bin/su - '"$user"' -c "'"${basedir}/bin/"'mysqlproxy_exporter -web.listen-address 0.0.0.0:9306 &>>/tmp/mysqlproxy_exporter.log &"' /etc/rc.local
        fi
    fi
    
    ps -ef | grep -v grep | grep -wq mysqlproxy_exporter
    if [[ $? -eq 0 ]];then
        echo "start mysqlproxy_exporter successfully"'!'
    else
        echo "start mysqlproxy_exporter failed."
        exit 4
    fi
    
}


function removeMysqlProxyExporter(){
    if [[ $osrelease -ge 7 ]];then
        systemctl stop mysqlproxy_exporter
        systemctl disable mysqlproxy_exporter
    else
        ps -ef | awk '/mysqlproxy_exporter/{print $2}' | xargs kill -9 &>/dev/null
        grep -wq "mysqlproxy_exporter" /etc/rc.local
        if [[ $? -eq 0 ]];then
            sed -i /mysqlproxy_exporter/d /etc/rc.local
        fi
    fi
    
    ps -ef | grep -v grep | grep -wq mysqlproxy_exporter
    if [[ $? -ne 0 ]];then
        #rm -rf /usr/local/mysqlproxy_exporter
        echo "finish to stop mysqlproxy_exporter"'!'
    else
        echo "stop mysqlproxy_exporter failed."
        exit 4
    fi
}




function installRedisProxyExporter(){
    basedir="/usr/local/redisproxy_exporter"
    binDir="$basedir/bin"
    etcDir="$basedir/etc"
    
    ps -ef | grep -v grep | grep -wq redisproxy_exporter
    if [[ $? -eq 0 ]];then
        echo "redisproxy_exporter started.skipping..."
    fi
    
    if [[ ! -d "$binDir" ]];then mkdir -p "$binDir";fi
    if [[ ! -d "$etcDir" ]];then mkdir -p "$etcDir";fi
    cd $binDir
    if [[ ! -e "redisproxy_exporter" || ! -s "redisproxy_exporter" ]];then
        downloadFile "redisproxy_exporter"
    fi
    chmod +x ./redisproxy_exporter
    if [[ $osrelease -ge 7 ]];then
        echo "[Unit]
Description=redis proxy /redis watchdog exporter service
Documentation=https://prometheus.io
After=network.target

[Service]
Type=simple
User=root
Group=root
LimitNOFILE=500000
ExecStart=${binDir}/redisproxy_exporter -web.listen-address 0.0.0.0:9379
Restart=always

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/redisproxy_exporter.service
        systemctl daemon-reload
        systemctl enable redisproxy_exporter
        systemctl restart redisproxy_exporter
        
    else
        ${binDir}/redisproxy_exporter -web.listen-address 0.0.0.0:9379 &>>/tmp/redisproxy_exporter.log &
        grep -wq "redisproxy_exporter" /etc/rc.local
        if [[ $? -ne 0 ]];then
            sed -i '$a \'"${basedir}/bin/"'redisproxy_exporter -web.listen-address 0.0.0.0:9379 &>>/tmp/redisproxy_exporter.log &' /etc/rc.local
        fi
    fi
    
    ps -ef | grep -v grep | grep -wq redisproxy_exporter
    if [[ $? -eq 0 ]];then
        echo "start redisproxy_exporter successfully"'!'
    else
        echo "start redisproxy_exporter failed."
        exit 4
    fi
    
}


function removeRedisProxyExporter(){
    if [[ $osrelease -ge 7 ]];then
        systemctl stop redisproxy_exporter
        systemctl disable redisproxy_exporter
    else
        ps -ef | awk '/redisproxy_exporter/{print $2}' | xargs kill -9 &>/dev/null
        grep -wq "redisproxy_exporter" /etc/rc.local
        if [[ $? -eq 0 ]];then
            sed -i /redisproxy_exporter/d /etc/rc.local
        fi
    fi
    
    ps -ef | grep -v grep | grep -wq redisproxy_exporter
    if [[ $? -ne 0 ]];then
        #rm -rf /usr/local/redisproxy_exporter
        echo "finish to stop redisproxy_exporter"'!'
    else
        echo "stop redisproxy_exporter failed."
        exit 4
    fi
}




function showHelp(){
    echo -e "Using $0 [install|remove] [node|mysql|mysqlproxy|redis|redisproxy|mongodb] \n"
}


function main(){

    if [[ $# -lt 2 ]];then
        echo $*
        showHelp
        exit 2
    fi
    
    if [[ "$1" == "install" ]];then
        if [[ "$2" == "node" ]];then 
            installNodeExporter
        elif [[ "$2" == "mysql" ]];then 
            installMysqlExporter
            createExporterUserHandler
        elif [[ "$2" == "redis" ]];then
            installRedisExporter
        elif [[ "$2" == "mongodb" ]];then
            installMongodbExporter
        elif [[ "$2" == "mysqlproxy" ]];then
            installMysqlProxyExporter
           elif [[ "$2" == "redisproxy" ]];then
            installRedisProxyExporter
        fi

    elif [[ "$1" == "remove" ]];then
        if [[ "$2" == "node" ]];then 
            removeNodeExporter
        elif [[ "$2" == "mysql" ]];then 
            removeMysqlExporter
        elif [[ "$2" == "redis" ]];then
            removeRedisExporter
        elif [[ "$2" == "mongodb" ]];then
            echo "removeMongodbExporter not support now."
        elif [[ "$2" == "mysqlproxy" ]];then
            removeMysqlProxyExporter
        elif [[ "$2" == "redisproxy" ]];then
            removeRedisProxyExporter
        fi
    fi
}

main $*


