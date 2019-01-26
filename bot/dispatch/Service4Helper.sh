#!/bin/bash

# https://stackoverflow.com/questions/27454717/how-to-run-a-remote-bash-script-with-arguments-from-local
# Parameter 1 is the flag. 
sudo -u root -H sh -c "echo $1 > /etc/Services/ServiceD/flag.txt"