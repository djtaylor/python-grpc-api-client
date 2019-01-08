import grpc
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from grpc_api_client.grpc.test import API_TEST_PARAMS
from grpc_api_client.grpc.test import api_pb2, api_pb2_grpc
from grpc_api_client.grpc.channel import gRPC_API_Credentials

class APITestServicer(api_pb2_grpc.APITestServicer):
    """
    Subclass of the API service stub object.
    """
    def BoolTest(self, request, context):
        print(request)
        print(context)

def start_test_server():
    """
    Spin up a test Docker server for running the test suite.
    """
    server = grpc.server(ThreadPoolExecutor(max_workers=10))

    # Add the servicer
    api_pb2_grpc.add_APITestServicer_to_server(
      APITestServicer(), server)

    # Add a secure port
    server.add_secure_port('0.0.0.0:5557', gRPC_API_Credentials.create_server(
        API_TEST_PARAMS['ca_cert'],
        API_TEST_PARAMS['client_cert'],
        API_TEST_PARAMS['client_key']
    ))

    # Start the server
    server.start()

    # Keep serving requests
    while True:
        sleep(1)
