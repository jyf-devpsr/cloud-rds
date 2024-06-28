#!/bin/sh
date
sed 's/\\n/&\n/g' grant_tmp.txt  > flyme_revoke.txt
sed -i 's/", u"//g' flyme_revoke.txt
sed -i 's/, u"//g' flyme_revoke.txt
sed -i 's/, u//g' flyme_revoke.txt
sed -i 's/GRANT/REVOKE/g' flyme_revoke.txt
sed -i "s/'REVOKE/REVOKE/g" flyme_revoke.txt
sed -i "s/ TO / FROM /g" flyme_revoke.txt
sed -i 's/`//g' flyme_revoke.txt
sed -i '1d' flyme_revoke.txt
sed -i '$d' flyme_revoke.txt
sed -i 's/\\n/;/g' flyme_revoke.txt
sed -i "s/FROM /FROM '/g" flyme_revoke.txt
sed -i "s/@/'@'/g" flyme_revoke.txt
sed -i "s/;/';/g" flyme_revoke.txt