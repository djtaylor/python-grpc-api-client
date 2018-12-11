dex_version='2.13.0'

go:
	python3 -m grpc_tools.protoc -I. --python_out=./dex_grpc/dex --grpc_python_out=. protoc/dex_api_2-13-0.proto

build_dex:
	docker build . -t python-dex-grpc-server -f Dockerfile_Dex --no-cache

run_dex:
	-docker rm python-dex-grpc-server
	-docker kill python-dex-grpc-server
	docker run -d -p 35557:5557 --name python-dex-grpc-server python-k8s-dex-server serve /etc/dex/dex-config.yaml

install:
	sudo python3 setup.py install

test:
	python3 setup.py test
