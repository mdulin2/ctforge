#!/bin/bash

# Parameter 1 is the flag. 
sudo -u root -H sh -c "echo $1 > /etc/Services/ServiceB/flag.txt"