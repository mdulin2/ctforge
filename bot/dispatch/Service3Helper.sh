#!/bin/bash

# https://stackoverflow.com/questions/17544954/run-mysql-query-in-remote-machine-through-ssh-in-command-line
flag=$1
mysql -h localhost -u root -p*password* -e "use injection; UPDATE korean_food SET price = 24.32, description = '$1' WHERE food_id = 12121232; "
