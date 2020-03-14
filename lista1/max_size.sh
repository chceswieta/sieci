#!/bin/bash
# calculates the largest packet size that still can be sent with fragmentation off


size=1272
while ping -s $size -c1 -M do $1 >&/dev/null; do 
  ((size+=4))
done
echo $size
