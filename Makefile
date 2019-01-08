dex_version=2_13_0
docker_image_tag=python-grpc-api-server

build:
	docker build . -t ${docker_image_tag} -f Dockerfile
	docker run -d -p 35557:5557 --name ${docker_image_tag} ${docker_image_tag}

run:
	-docker rm ${docker_image_tag}
	-docker kill ${docker_image_tag}
	docker run -d -p 35557:5557 --name ${docker_image_tag} ${docker_image_tag}

install:
	virtualenv --python python3 venv
	chmod +x venv/bin/activate
	env bash venv/bin/activate
	pip3 install -r requirements.txt
	python3 setup.py install

clean:
	-docker rm ${docker_image_tag}
	-docker kill ${docker_image_tag}

test:
	env bash venv/bin/activate
	python3 -m grpc_tools.protoc -I./proto \
  --python_out=./ \
  --grpc_python_out=./ \
  proto/grpc_api_client/grpc/test/api.proto
	python3 setup.py test
