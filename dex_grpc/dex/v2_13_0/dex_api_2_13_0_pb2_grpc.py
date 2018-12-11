# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from k8s_dex.dex.v2_13_0 import dex_api_2_13_0_pb2 as go_dot_dex__api__2__13__0__pb2


class DexStub(object):
  """Dex represents the dex gRPC service.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateClient = channel.unary_unary(
        '/api.Dex/CreateClient',
        request_serializer=go_dot_dex__api__2__13__0__pb2.CreateClientReq.SerializeToString,
        response_deserializer=go_dot_dex__api__2__13__0__pb2.CreateClientResp.FromString,
        )
    self.DeleteClient = channel.unary_unary(
        '/api.Dex/DeleteClient',
        request_serializer=go_dot_dex__api__2__13__0__pb2.DeleteClientReq.SerializeToString,
        response_deserializer=go_dot_dex__api__2__13__0__pb2.DeleteClientResp.FromString,
        )
    self.CreatePassword = channel.unary_unary(
        '/api.Dex/CreatePassword',
        request_serializer=go_dot_dex__api__2__13__0__pb2.CreatePasswordReq.SerializeToString,
        response_deserializer=go_dot_dex__api__2__13__0__pb2.CreatePasswordResp.FromString,
        )
    self.UpdatePassword = channel.unary_unary(
        '/api.Dex/UpdatePassword',
        request_serializer=go_dot_dex__api__2__13__0__pb2.UpdatePasswordReq.SerializeToString,
        response_deserializer=go_dot_dex__api__2__13__0__pb2.UpdatePasswordResp.FromString,
        )
    self.DeletePassword = channel.unary_unary(
        '/api.Dex/DeletePassword',
        request_serializer=go_dot_dex__api__2__13__0__pb2.DeletePasswordReq.SerializeToString,
        response_deserializer=go_dot_dex__api__2__13__0__pb2.DeletePasswordResp.FromString,
        )
    self.ListPasswords = channel.unary_unary(
        '/api.Dex/ListPasswords',
        request_serializer=go_dot_dex__api__2__13__0__pb2.ListPasswordReq.SerializeToString,
        response_deserializer=go_dot_dex__api__2__13__0__pb2.ListPasswordResp.FromString,
        )
    self.GetVersion = channel.unary_unary(
        '/api.Dex/GetVersion',
        request_serializer=go_dot_dex__api__2__13__0__pb2.VersionReq.SerializeToString,
        response_deserializer=go_dot_dex__api__2__13__0__pb2.VersionResp.FromString,
        )
    self.ListRefresh = channel.unary_unary(
        '/api.Dex/ListRefresh',
        request_serializer=go_dot_dex__api__2__13__0__pb2.ListRefreshReq.SerializeToString,
        response_deserializer=go_dot_dex__api__2__13__0__pb2.ListRefreshResp.FromString,
        )
    self.RevokeRefresh = channel.unary_unary(
        '/api.Dex/RevokeRefresh',
        request_serializer=go_dot_dex__api__2__13__0__pb2.RevokeRefreshReq.SerializeToString,
        response_deserializer=go_dot_dex__api__2__13__0__pb2.RevokeRefreshResp.FromString,
        )


class DexServicer(object):
  """Dex represents the dex gRPC service.
  """

  def CreateClient(self, request, context):
    """CreateClient creates a client.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteClient(self, request, context):
    """DeleteClient deletes the provided client.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreatePassword(self, request, context):
    """CreatePassword creates a password.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdatePassword(self, request, context):
    """UpdatePassword modifies existing password.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeletePassword(self, request, context):
    """DeletePassword deletes the password.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListPasswords(self, request, context):
    """ListPassword lists all password entries.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetVersion(self, request, context):
    """GetVersion returns version information of the server.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListRefresh(self, request, context):
    """ListRefresh lists all the refresh token entries for a particular user.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RevokeRefresh(self, request, context):
    """RevokeRefresh revokes the refresh token for the provided user-client pair.

    Note that each user-client pair can have only one refresh token at a time.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DexServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateClient': grpc.unary_unary_rpc_method_handler(
          servicer.CreateClient,
          request_deserializer=go_dot_dex__api__2__13__0__pb2.CreateClientReq.FromString,
          response_serializer=go_dot_dex__api__2__13__0__pb2.CreateClientResp.SerializeToString,
      ),
      'DeleteClient': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteClient,
          request_deserializer=go_dot_dex__api__2__13__0__pb2.DeleteClientReq.FromString,
          response_serializer=go_dot_dex__api__2__13__0__pb2.DeleteClientResp.SerializeToString,
      ),
      'CreatePassword': grpc.unary_unary_rpc_method_handler(
          servicer.CreatePassword,
          request_deserializer=go_dot_dex__api__2__13__0__pb2.CreatePasswordReq.FromString,
          response_serializer=go_dot_dex__api__2__13__0__pb2.CreatePasswordResp.SerializeToString,
      ),
      'UpdatePassword': grpc.unary_unary_rpc_method_handler(
          servicer.UpdatePassword,
          request_deserializer=go_dot_dex__api__2__13__0__pb2.UpdatePasswordReq.FromString,
          response_serializer=go_dot_dex__api__2__13__0__pb2.UpdatePasswordResp.SerializeToString,
      ),
      'DeletePassword': grpc.unary_unary_rpc_method_handler(
          servicer.DeletePassword,
          request_deserializer=go_dot_dex__api__2__13__0__pb2.DeletePasswordReq.FromString,
          response_serializer=go_dot_dex__api__2__13__0__pb2.DeletePasswordResp.SerializeToString,
      ),
      'ListPasswords': grpc.unary_unary_rpc_method_handler(
          servicer.ListPasswords,
          request_deserializer=go_dot_dex__api__2__13__0__pb2.ListPasswordReq.FromString,
          response_serializer=go_dot_dex__api__2__13__0__pb2.ListPasswordResp.SerializeToString,
      ),
      'GetVersion': grpc.unary_unary_rpc_method_handler(
          servicer.GetVersion,
          request_deserializer=go_dot_dex__api__2__13__0__pb2.VersionReq.FromString,
          response_serializer=go_dot_dex__api__2__13__0__pb2.VersionResp.SerializeToString,
      ),
      'ListRefresh': grpc.unary_unary_rpc_method_handler(
          servicer.ListRefresh,
          request_deserializer=go_dot_dex__api__2__13__0__pb2.ListRefreshReq.FromString,
          response_serializer=go_dot_dex__api__2__13__0__pb2.ListRefreshResp.SerializeToString,
      ),
      'RevokeRefresh': grpc.unary_unary_rpc_method_handler(
          servicer.RevokeRefresh,
          request_deserializer=go_dot_dex__api__2__13__0__pb2.RevokeRefreshReq.FromString,
          response_serializer=go_dot_dex__api__2__13__0__pb2.RevokeRefreshResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.Dex', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
