from grpc import secure_channel, insecure_channel, ssl_channel_credentials

class K8S_Dex_gRPC_Channel(object):
    """
    gRPC channel for connecting to a Dex instance.
    """
    def __init__(self, grpc_host, grpc_port, grpc_options={}, ca_cert=None, client_cert=None, client_key=None):
        self.grpc_host = grpc_host
        self.grpc_port = grpc_port

        # The gRPC target (host:port)
        self.grpc_target = '{}:{}'.format(grpc_host, grpc_port)

        # Extra options to pass to the channel
        self.grpc_options = grpc_options

        # Options to make a secure (TLS) channel
        self.ca_cert = ca_cert
        self.client_key = client_key
        self.client_cert = client_cert

        # Store the channel object
        self._channel = None

    def _read_tls_bytes(self, file_name=None):
        """
        Read the contents of a TLS certificate in binary mode.
        """
        if not file_name:
            return None
        with open(file_name, 'rb') as f:
            return f.read()

    def _connect_secure(self):
        """
        Make a secure connection to the gRPC server.
        """
        credentials = ssl_channel_credentials(
            certificate_chain=self._read_tls_bytes(self.client_cert),
            private_key=self._read_tls_bytes(self.client_key),
            root_certificates=self._read_tls_bytes(self.ca_cert)
        )

        # Open and return the channel
        return secure_channel(self.grpc_target, credentials, options=self.grpc_options)

    def _connect_insecure(self):
        """
        Make an insecure connection to the gRPC server.
        """
        return insecure_channel(self._target, options=self.grpc_options)

    def connect(self):
        """
        Open a secure (or insecure if no certificates provided) gRPC channel.
        """

        # Must supply client certificate and key for secure channel
        if self.client_cert and self.client_key:
            self._channel = self._connect_secure()

        # Create an insecure channel
        else:
            self._channel = self._connect_insecure()

        # Return the channel
        return self._channel
