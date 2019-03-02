docker_name=python-grpc-api-server
docker_port=35557
python_bin=venv/bin/python3
pip_bin=venv/bin/pip3

build:
	${python_bin} -m grpc_tools.protoc -I./proto \
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
	${pip_bin} install -r requirements.txt
	${python_bin} setup.py install

clean:
	-docker kill ${docker_name}
	-docker rm ${docker_name}
	${python_bin} setup.py clean --all

test:
	${python_bin} setup.py test

logs:
	docker logs ${docker_name}
