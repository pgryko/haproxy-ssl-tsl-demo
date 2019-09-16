
Build the container
$ docker build -t my-haproxy .

Test the configuration file

$ docker run -it --rm --name haproxy-syntax-check my-haproxy haproxy -c -f /usr/local/etc/haproxy/haproxy.cfg

Run the container

$ docker run -d --name my-running-haproxy my-haproxy