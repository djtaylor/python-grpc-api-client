from k8s_dex.dex import DEX_GRPC
from k8s_dex.dex.channel import K8S_Dex_gRPC_Channel

class K8S_Dex_gRPC_Interface(object):
    """
    Interface for constructing bindings based on the Dex API version being used.
    """
    def __init__(self, channel):
        self.channel = channel
        self.stub = DEX_GRPC.DexStub(self.channel)

    @classmethod
    def construct(cls, grpc_host, grpc_port, grpc_options, ca_cert=None, client_cert=None, client_key=None):
        """
        Constructor method for building a gRPC API interface.
        """

        # Open a new gRPC channel
        channel = K8S_Dex_gRPC_Channel(grpc_host, grpc_port,
            ca_cert = ca_cert,
            client_cert = client_cert,
            client_key = client_key
        ).connect()

        # Create a new Dex gRPC API interface
        return cls(channel)
