#!/bin/sh

mysql_source_file=Percona-Server-8.0.33-25-Linux.x86_64.glibc2.17.tar.gz
source_dir=mysql_source
data_dir=@datadir

f_install_user()
{
    systemctl stop nslcd.service

    groupadd -g 1306 mysql
    useradd -u 1306 mysql -g mysql  -s /sbin/nologin -M

    systemctl start nslcd    
}

f_install_mysql()
{
    yum -y install gcc gcc-c++  cmake perl-DBD-MySQL perl-DBI bison-devel ncurses-devel openssl-devel glibc readline-devel openssl openssl-devel ncurses ncurses-devel jemalloc-devel jemalloc libcurl-devel
    mkdir $source_dir
    wget http://ftp_host:8080/software/mysql/$mysql_source_file -O $mysql_source_file
    tar xvf $mysql_source_file -C $source_dir --strip-components 1
    mv $source_dir /usr/local/mysql
    ln -s /usr/local/mysql/bin/mysql /usr/bin/mysql

}

f_init_mysql()
{
    mkdir -p $data_dir
    if [ "$data_dir" != "/usr/local/mysql/data" ];then
	[ -e "/usr/local/mysql/data" ] && mv /usr/local/mysql/data /usr/local/mysql/data_old
        ln -s $data_dir /usr/local/mysql/data
        if [ $? -ne 0 ];then
            echo "execute ln -s $data_dir /usr/local/mysql/data failed."
            exit 1
        fi
    fi
    
    chown -R mysql:mysql $data_dir
    chown -R mysql:mysql /usr/local/mysql
    /usr/local/mysql/bin/mysqld --basedir=/usr/local/mysql --datadir=/usr/local/mysql/data --user=mysql --initialize-insecure
	echo "export PATH=$PATH:/usr/local/mysql/bin" > /etc/profile.d/mysql.sh
	source /etc/profile
}

f_config_auto_start()
{
    cp /usr/local/mysql/support-files/mysql.server  /etc/init.d/mysqld 
    sed -i 's#basedir=$#basedir=/usr/local/mysql#g' /etc/init.d/mysqld
    sed -i 's#datadir=$#datadir=/usr/local/mysql/data#g' /etc/init.d/mysqld
    chmod +x /etc/init.d/mysqld

    chkconfig mysqld on
}

f_start_mysql()
{
    /etc/init.d/mysqld start
}
f_init_cfg()
{
	memory=$1
	if [ $# -ne 1 ];then
		echo "Usage:sh install.sh memory(GB)"
		echo "Example:sh install.sh 4"
		echo "默认mysql占用总内存50%"
		mem_kb=`cat /proc/meminfo | grep MemTotal | awk -F: '{print $2}' | sed 's/[^0-9]//g'`
		memory=`expr $mem_kb / 1000 / 1000 / 2`
	fi
	
	if [ -n "`echo $1 | sed 's/^[0-9]*//'`" ];then
		echo "Usage:sh install.sh memory(GB)"
                echo "Example:sh install.sh 4"
                exit 1
	fi
	inner_ip=`ip addr | grep inet | egrep -v 'inet6|127.0.0.1|10.0' | egrep '192.|10.|172.'| awk '{print $2}'|awk -F'/' '{print $1}'|head -n 1`
	server_id=`echo $inner_ip | awk -F'.' '{print $3$4}'`
	cpu_num=`cat /proc/cpuinfo | grep processor | wc -l`
	cp my_80.cnf my.cnf.tmp
	sed -i "s/@memory/${memory}GB/g" my.cnf.tmp
	sed -i "s/@server_id/$server_id/g" my.cnf.tmp
	sed -i "s/@bind_address/$inner_ip/g" my.cnf.tmp
	sed -i "s/@cpu_num/$cpu_num/g" my.cnf.tmp
	if [ -f /etc/my.cnf ];then
		mv /etc/my.cnf /etc/my.cnf.bak
	fi
	cp -f my.cnf.tmp /etc/my.cnf
}

main()
{
    f_init_cfg $@
    f_install_user
    f_install_mysql
    f_init_mysql
    f_config_auto_start
    f_start_mysql
}

main $@









