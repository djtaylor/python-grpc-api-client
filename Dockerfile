FROM python:3.7-stretch

WORKDIR /docker_files
RUN mkdir -p /etc/grpc/tls

COPY ./docker_files/grpc_tls/ /etc/grpc/tls/.

WORKDIR /server

COPY ./requirements.txt /server
RUN pip3 install -r requirements.txt

COPY . /server

RUN python3 setup.py install

CMD python3 /server/docker_files/grpc_server.py
