FROM python:3.6
RUN apt update -y
RUN apt install -y openssl
RUN apt install -y build-essential libssl-dev
RUN pip install --upgrade pip wheel setuptools
WORKDIR /code

ADD . /code
RUN pip install -r requirements.txt
EXPOSE 80
EXPOSE 443
CMD python index.py


