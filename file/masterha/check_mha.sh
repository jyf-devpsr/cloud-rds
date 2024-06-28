echo "####################### check status #############"
masterha_check_status --conf=/etc/masterha/proxy_app_default.cnf
echo "####################### check ssh    #############"
masterha_check_ssh --conf=/etc/masterha/proxy_app_default.cnf
echo "####################### check repl #############"
masterha_check_repl --conf=/etc/masterha/proxy_app_default.cnf
