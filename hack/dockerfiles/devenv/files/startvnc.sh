#!/bin/bash

prog=/usr/bin/vncpasswd
mypass="zzZ2Zzz"

/usr/bin/expect <<EOF
spawn "$prog"
expect "Password:"
send "$mypass\r"
expect "Verify:"
send "$mypass\r"
expect "Would you like to enter a view-only password (y/n)? "
send "n\r"
expect eof
exit
EOF

USER=root vncserver -geometry 1280x720 -depth 24
USER=root vncserver -geometry 1920x1080 -depth 24

while :
do
    sleep 3
done
