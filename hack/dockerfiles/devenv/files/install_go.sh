#!/bin/bash

MACHINE_TYPE=`uname -m`
if [ ${MACHINE_TYPE} == 'x86_64' ]; then
    curl https://dl.google.com/go/go1.13.8.linux-amd64.tar.gz -o go.tar.gz
elif [ ${MACHINE_TYPE} == 'aarch64' ]; then
    curl https://dl.google.com/go/go1.13.8.linux-arm64.tar.gz -o go.tar.gz
else
    echo "unknown architecture"
fi

tar -C /usr/local -xzf go.tar.gz
