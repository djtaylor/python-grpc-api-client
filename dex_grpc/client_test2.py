import unittest
from k8s_dex.dex import DEX_GRPC
from k8s_dex import K8S_Dex_gRPC

# Create a gRPC client with the Docker container
GRPC_CLIENT = K8S_Dex_gRPC('127.0.0.1', 35557,
    ca_cert = 'docker_files/dex_tls/ca.crt',
    client_cert = 'docker_files/dex_tls/client.crt',
    client_key = 'docker_files/dex_tls/client.key'
)

class K8S_Dex_gRPC_Client_Test(unittest.TestCase):
    """Tests for `client.py`."""

    def test_create_stub(self):
        """ Test creating a stub instance of `DexStub`. """
        self.assertIsInstance(GRPC_CLIENT.grpc_interface.stub, DEX_GRPC.DexStub)

    def test_get_version(self):
        """ Test getting Dex version from gRPC endpoint. """
        client = K8S_Dex_gRPC_Client(GRPC_SERVER, **GRPC_PARAMS)
        response = GRPC_CLIENT.api.GetVersion()

        response = client.get_version()
        self.assertIsInstance(response, dex_proto.VersionResp)

    def test_list_passwords(self):
        """ Test listing passwords Dex from gRPC endpoint. """
        client = K8S_Dex_gRPC_Client(GRPC_SERVER, **GRPC_PARAMS)
        response = client.list_passwords()
        self.assertIsInstance(response, dex_proto.ListPasswordResp)

    def test_create_password(self):
        """ Test creating password from gRPC endpoint. """
        client = K8S_Dex_gRPC_Client(GRPC_SERVER, **GRPC_PARAMS)
        response = client.create_password(
            email = 'admin@domain.com',
            username = 'Administrator',
            user_id = 'admin',
            password = 'password'
        )
        self.assertIsInstance(response, dex_proto.CreatePasswordResp)

    def test_update_password(self):
        """ Test updating password from gRPC endpoint. """
        client = K8S_Dex_gRPC_Client(GRPC_SERVER, **GRPC_PARAMS)
        response = client.update_password(
            email = 'admin@domain.com',
            username = 'Administrator',
            password = 'password2'
        )
        self.assertIsInstance(response, dex_proto.UpdatePasswordResp)

    def test_delete_password(self):
        """ Test deleting password from gRPC endpoint. """
        client = K8S_Dex_gRPC_Client(GRPC_SERVER, **GRPC_PARAMS)
        response = client.delete_password(
            email = 'admin@domain.com'
        )
        self.assertIsInstance(response, dex_proto.DeletePasswordResp)

    def test_create_client(self):
        """ Test creating a client from gRPC endpoint. """
        client = K8S_Dex_gRPC_Client(GRPC_SERVER, **GRPC_PARAMS)
        response = client.create_client(
            client_id = 'test-app',
            client_name = 'Test APP',
            client_secret = 'hkjfdghkjhjkazfgdf',
            redirect_uris = ['http://127.0.0.1:5554/callback']
        )
        self.assertIsInstance(response, dex_proto.CreateClientResp)

    def test_delete_client(self):
        """ Test deleting a client from gRPC endpoint. """
        client = K8S_Dex_gRPC_Client(GRPC_SERVER, **GRPC_PARAMS)
        response = client.delete_client(
            client_id = 'test-app'
        )
        self.assertIsInstance(response, dex_proto.DeleteClientResp)

    def test_list_refresh(self):
        """ Test listing user refresh tokens from gRPC endpoint. """
        client = K8S_Dex_gRPC_Client(GRPC_SERVER, **GRPC_PARAMS)
        response = client.list_refresh(
            user_id = 'mocktest'
        )
        self.assertIsInstance(response, dex_proto.ListRefreshResp)
