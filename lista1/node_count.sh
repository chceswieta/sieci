#!/bin/bash
# calculates the node count to and from a chosen server
# usage: node_count.sh <SERVER> <START_VALUE> <MAX_TIMEOUT>


to=$2
while :
do
    if ping -W $3 -Mdo -c1 -t $to $1 >res
    then
        break
    else
        ((to++))
    fi
done

echo "nodes to server: $to"
cat res
rm res
