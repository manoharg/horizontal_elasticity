#!/bin/bash

echo "Enter number of Servers you wish to create: "
read numOfServers

echo "Enter the port number you wish to start at: "
read portNum

#run loop to spin up servers
for ((num = 0; num <numOfServers; num++))
do
#docker call that will name the server starting at "server1" to "server$numOfServers" and make them all mounted to the same html content
	docker run --name server$num -p $portNum:80 -v /home/manohar/Desktop/ProjectFiles/Servers/server1/html:/usr/share/nginx/html:ro -d server1
#port number will be increased by one so that the next server will be created on the next port
	portNum=$((portNum + 1))
done

echo "$numOfServers server(s) created."
