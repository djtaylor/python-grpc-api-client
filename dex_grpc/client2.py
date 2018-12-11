import base64
from bcrypt import hashpw, gensalt
from google.protobuf.message import Message

from k8s_dex import K8S_Dex_gRPC
from k8s_dex.dex import DEX_GRPC, DEX_PROTO
from k8s_dex.channel import K8S_Dex_gRPC_Channel

class K8S_Dex_gRPC_Client(object):
    """
    gRPC client for connecting to a Dex instance.
    """
    def __init__(self, host, port=5557, ca_cert=None, client_cert=None, client_key=None):
        self.client =
        self.channel = self._connect_channel(host, port, ca_cert, client_cert, client_key)
        self.stub    = DEX_GRPC.DexStub(self.channel)

    def _connect_channel(self, host, port, ca_cert, client_cert, client_key):
        """
        Create a secure channel with the Dex gRPC server.
        """
        channel_instance = K8S_Dex_gRPC_Channel('{}:{}'.format(host, port))
        return channel_instance.connect_secure(ca_cert, client_cert, client_key)

    def get_version(self):
        """
        Make a gRPC call to VersionReq.
        """
        return self.stub.GetVersion(DEX_PROTO.VersionReq())

    def list_passwords(self):
        """
        Make a gRPC call to ListPasswordReq.
        """
        return self.stub.ListPasswords(DEX_PROTO.ListPasswordReq())

    def delete_password(self, email):
        """
        Make a gRPC call to DeletePasswordReq.
        """
        return self.stub.DeletePassword(DEX_PROTO.DeletePasswordReq(email=email))

    def update_password(self, email, username, password):
        """
        Make a gRPC call to UpdatePasswordReq.
        """
        return self.stub.UpdatePassword(DEX_PROTO.UpdatePasswordReq(
            email=email,
            new_hash=hashpw(password.encode(), gensalt()),
            new_username=username
        ))

    def create_password(self, email, username, user_id, password):
        """
        Make a gRPC call to CreatePasswordReq.
        """

        # Generate a password request message
        password_message = DEX_PROTO.Password(
            email = email,
            username = username,
            hash = hashpw(password.encode(), gensalt()),
            user_id = user_id,
        )

        return self.stub.CreatePassword(DEX_PROTO.CreatePasswordReq(
            password=password_message
        ))

    def create_client(self, client_id, client_name, client_secret, redirect_uris, **kwargs):
        """
        Make a gRPC call to CreateClientReq.
        """

        # Generate a client request message
        client_message = DEX_PROTO.Client(
            id = client_id,
            secret = client_secret,
            name = client_name,
            redirect_uris = redirect_uris,
            **kwargs
        )

        return self.stub.CreateClient(DEX_PROTO.CreateClientReq(client=client_message))

    def delete_client(self, client_id):
        """
        Make a gRPC call to DeleteClientReq.
        """
        return self.stub.DeleteClient(DEX_PROTO.DeleteClientReq(id=client_id))

    def list_refresh(self, user_id):
        """
        Make a gRPC call to ListRefreshReq.
        """
        return self.stub.ListRefresh(DEX_PROTO.ListRefreshReq(
            user_id=base64.b64encode(user_id.encode())
        ))
