# -*- coding: utf-8 -*-
__version__ = '0.1.post1'

from k8s_dex.dex import DEX_PROTO
from k8s_dex.dex.interface import K8S_Dex_gRPC_Interface

class _K8S_Dex_gRPC_API_Path(object):
    """
    Class object for storing API path attributes and objects.
    """
    def __init__(self, stub_name, stub_object):
        """
        Initialize and store the stub object for later use.
        """
        self._stub_object = stub_object
        self._stub_name = stub_name

        # Request and response objects
        self._request = self._get_request_object()
        self._response = self._get_response_object()

    def _get_request_object(self):
        """
        Get the appropriate request object for this API path.
        """
        return getattr(DEX_PROTO, '{}Req'.format(self._stub_name))

    def _get_response_object(self):
        """
        Get the appropriate response object for this API path.
        """
        return getattr(DEX_PROTO, '{}Resp'.format(self._stub_name))

    def __call__(self, **kwargs):
        """
        Call the underlying stub method for this API path.
        """
        return self.stub_object(self._request(**kwargs))

class _K8S_Dex_gRPC_API_Collection(object):
    """
    Class object for storing API path objects.
    """
    pass

class K8S_Dex_gRPC(object):
    """
    Create a new gRPC client to connect to a Dex instance.
    """
    def __init__(self, grpc_host, grpc_port, grpc_options={}, ca_cert=None, client_cert=None, client_key=None):

        # Create the Dex gRPC interface
        self.grpc_interface = K8S_Dex_gRPC_Interface.construct(grpc_host, grpc_port,
            grpc_options = grpc_options,
            ca_cert = ca_cert,
            client_cert = client_cert,
            client_key = client_key
        )

        # API object for containing gRPC procedures
        self.api = _K8S_Dex_gRPC_API_Collection

        # Construct the API
        self._construct_api()

    def _construct_api(self):
        """
        Construct the API procedures object from the generated Dex gRPC code.
        """
        api_stubs = {}

        # Scan for API stub entries
        for a in dir(self.grpc_interface.stub):
            stub_attr = getattr(self.grpc_interface.stub, a)
            stub_name = type(stub_attr).__name__

            # Unary unary multicallables for API interactions
            if stub_name == '_UnaryUnaryMultiCallable':
                setattr(self.api, str(a), _K8S_Dex_gRPC_API_Path(str(a), stub_attr))
