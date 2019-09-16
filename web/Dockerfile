FROM python:3.6
RUN apt update -y
RUN apt install -y openssl apache2
RUN apt install -y build-essential libssl-dev
RUN pip install --upgrade pip wheel setuptools
RUN pip install pyOpenSSL
WORKDIR /code

# Generate cetificates
RUN openssl genrsa -out server.key 2048 && \
  openssl rsa -in server.key -out server.key && \
  openssl req -sha256 -new -key server.key -out server.csr -subj '/CN=httpd' && \
  openssl x509 -req -sha256 -days 365 -in server.csr -signkey server.key -out server.crt

ADD . /code
RUN pip install -r requirements.txt
EXPOSE 80
EXPOSE 443
CMD python index.py


