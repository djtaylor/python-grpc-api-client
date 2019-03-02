docker_name=python-grpc-api-server
docker_port=35557

build:
	venv/bin/python3 -m grpc_tools.protoc -I./proto \
	--python_out=./ \
	--grpc_python_out=./ \
	proto/grpc_api_client/grpc/sample/api.proto
	docker build . -t ${docker_name} -f Dockerfile

run:
	-docker kill ${docker_name}
	-docker rm ${docker_name}
	docker run -d -p ${docker_port}:5557 --name ${docker_name} ${docker_name}

install:
	virtualenv --python python3 venv
	chmod +x venv/bin/activate
	venv/bin/pip3 install -r requirements.txt
	venv/bin/python3 setup.py install

clean:
	-docker kill ${docker_name}
	-docker rm ${docker_name}
	venv/bin/python3 setup.py clean --all

test:
	env bash venv/bin/activate
	venv/bin/python3 setup.py test

logs:
	docker logs ${docker_name}
