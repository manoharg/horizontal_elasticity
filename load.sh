#!/bin/bash
while :
do
    ab -n 1000 -c 500 "http://127.0.0.1:8080/"
done
