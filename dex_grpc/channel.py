from grpc import secure_channel, insecure_channel, ssl_channel_credentials

class K8S_Dex_gRPC_Channel(object):
    """
    gRPC channel for connecting to a Dex instance.
    """
    def __init__(self, target=None, options=None):
        self._target   = target
        self._options  = options

    def _load_tls_bytes(self, file_path):
        """
        Load a TLS file into a bytes like object.
        """
        with open(file_path, 'rb') as f:
            return f.read()

    def connect_secure(self, ca_cert, client_cert, client_key):
        """
        Create a secure connection to a gRPC server.
        """
        credentials = ssl_channel_credentials(
            certificate_chain=self._load_tls_bytes(client_cert),
            private_key=self._load_tls_bytes(client_key),
            root_certificates=self._load_tls_bytes(ca_cert)
        )

        # Open and return the channel
        return secure_channel(self._target, credentials, options=self._options)

    def connect_insecure(self):
        """
        Create an insecure connection to a gRPC server.
        """
        return insecure_channel(self._target, options=self._options)
