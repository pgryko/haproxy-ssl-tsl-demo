FROM haproxy:1.5.18
RUN apt update -y
RUN apt install -y openssl


# Generate cetificates
RUN cd /etc/ssl/certs/ && openssl genrsa -out server.key 2048 && \
  openssl rsa -in server.key -out server.key && \
  openssl req -sha256 -new -key server.key -out server.csr -subj '/CN=httpd' && \
  openssl x509 -req -sha256 -days 365 -in server.csr -signkey server.key -out server.crt

# Create pem file, this is the certificate, the key and optionally certificate authorities concatenated into one file
RUN cat /etc/ssl/certs/server.crt /etc/ssl/certs/server.key | tee /etc/ssl/certs/server.pem

RUN ls /etc/ssl/certs/

RUN ls /usr/local/etc/haproxy/

COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg
