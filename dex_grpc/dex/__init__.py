from os import getenv
from importlib import import_module

DEX_VERSION = getenv('PY_K8S_DEX_VERSION', '2.13.0')
DEX_GRPC = import_module(
    'k8s_dex.dex.v{0}.dex_api_{0}_pb2_grpc'.format(DEX_VERSION.replace('.', '_'))
)
DEX_PROTO = import_module(
    'k8s_dex.dex.v{0}.dex_api_{0}_pb2'.format(DEX_VERSION.replace('.', '_'))
)
