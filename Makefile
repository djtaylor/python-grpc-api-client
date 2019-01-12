docker_image_tag=python-grpc-api-server

build:
	docker build . -t ${docker_image_tag} -f Dockerfile

run:
	-docker kill ${docker_image_tag}
	-docker rm ${docker_image_tag}
	docker run -d -p 35557:5557 --name ${docker_image_tag} ${docker_image_tag}

install:
	virtualenv --python python3 venv
	chmod +x venv/bin/activate
	env bash venv/bin/activate
	venv/bin/pip3 install -r requirements.txt
	venv/bin/python3 setup.py install

clean:
	-docker kill ${docker_image_tag}
	-docker rm ${docker_image_tag}
	venv/bin/python3 setup.py clean --all

test:
	env bash venv/bin/activate
	venv/bin/python3 -m grpc_tools.protoc -I./proto \
  --python_out=./ \
  --grpc_python_out=./ \
  proto/grpc_api_client/grpc/test/api.proto
	venv/bin/python3 setup.py test

logs:
	docker logs ${docker_image_tag}
