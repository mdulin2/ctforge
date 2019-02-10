sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 5000
uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app
