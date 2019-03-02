from grpc_api_client.grpc.sample import API_TEST_PARAMS as tp
from grpc_api_client.grpc.sample import gRPC_API_Test_Fields
from grpc_api_client.client import gRPC_API_Client

client = gRPC_API_Client(
    tp['api_proto'],
    tp['api_grpc']
)
client.connect(tp['host'], tp['port'],
    ca_cert = tp['ca_cert'],
    client_cert = tp['client_cert'],
    client_key = tp['client_key']
)

print(client.api.BytesTest(value=b'test').json)

for name, method in client.api:
    print('API Method: {}: {}'.format(name, method))
    print('  InputClass: {}'.format(method.input.handler))
    print('    > Fields:')
    for field_name, field_obj in method.input_fields():
        print('      > {}: {}'.format(field_name, field_obj))
    print('  OutputClass: {}'.format(method.output.handler))

    print('  SampleFields: {}'.format(gRPC_API_Test_Fields.create(method)))
