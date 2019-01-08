from os import getenv
from importlib import import_module
from grpc_api_client.client import gRPC_API_Client_Settings, gRPC_API_Bindings

API_TEST_PARAMS = {
    'host': getenv('PY_GRPC_API_TEST_HOST', '127.0.0.1'),
    'port': getenv('PY_GRPC_API_TEST_PORT', 35557),
    'ca_cert': getenv('PY_GRPC_API_TEST_CA_CERT', 'docker_files/grpc_tls/ca.crt'),
    'client_cert': getenv('PY_GRPC_API_TEST_CLIENT_CERT', 'docker_files/grpc_tls/client.crt'),
    'client_key': getenv('PY_GRPC_API_TEST_CLIENT_KEY', 'docker_files/grpc_tls/client.key'),
    'api_proto': 'grpc_api_client.grpc.test.api_pb2',
    'api_grpc': 'grpc_api_client.grpc.test.api_pb2_grpc',
    'stub_name': 'APITestStub',
    'options': {}
}

class gRPC_API_Client_Test_Settings(object):
    """
    Generate a settings object for testing this module.
    """

    @staticmethod
    def secure():
        """
        Create test settings for a secure connection.
        """
        return gRPC_API_Client_Settings(API_TEST_PARAMS['host'], API_TEST_PARAMS['port'],
            ca_cert = API_TEST_PARAMS['ca_cert'],
            client_key = API_TEST_PARAMS['client_key'],
            client_cert = API_TEST_PARAMS['client_cert'],
            bindings = gRPC_API_Bindings(
                API_TEST_PARAMS['api_proto'],
                API_TEST_PARAMS['api_grpc']
            ))

    @staticmethod
    def insecure():
        """
        Create test settings for an insecure connection.
        """
        return gRPC_API_Client_Settings(API_TEST_PARAMS['host'], API_TEST_PARAMS['port'],
            bindings = gRPC_API_Bindings(
                API_TEST_PARAMS['api_proto'],
                API_TEST_PARAMS['api_grpc']
            ))
