[![Build Status](https://api.travis-ci.org/djtaylor/python-dex-grpc.png)](https://api.travis-ci.org/djtaylor/python-dex-grpc)

### Local Dex Service
To build and run a local Dex server for testing:
```
$ make build_dex
$ make run_dex
```
This will spin up a Docker container with basic configuration for gRPC testing listening on port 35557.

### Tests
Testing is done with `unittest` and `nose` for discovery.
```
$ python setup.py test
```
