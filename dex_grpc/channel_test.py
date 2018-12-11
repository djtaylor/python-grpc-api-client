import unittest
from k8s_dex.channel import K8S_Dex_gRPC_Channel
from grpc._channel import Channel

GRPC_TARGET = '127.0.0.1:35557'
GRPC_CA_CERT = 'docker_files/dex_tls/ca.crt'
GRPC_CLIENT_CERT = 'docker_files/dex_tls/client.crt'
GRPC_CLIENT_KEY = 'docker_files/dex_tls/client.key'

class K8S_Dex_gRPC_Channel_Test(unittest.TestCase):
    """Tests for `channel.py`."""

    def test_create_secure_channel(self):
        """ Test creating a secure gRPC channel. """
        channel = K8S_Dex_gRPC_Channel(GRPC_TARGET)
        channel_secure = channel.connect_secure(GRPC_CA_CERT, GRPC_CLIENT_CERT, GRPC_CLIENT_KEY)
        self.assertIsInstance(channel_secure, Channel)

    def test_create_insecure_channel(self):
        """ Test creating an insecure gRPC channel. """
        channel = K8S_Dex_gRPC_Channel(GRPC_TARGET)
        channel_insecure = channel.connect_insecure()
        self.assertIsInstance(channel_insecure, Channel)
