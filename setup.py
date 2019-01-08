#!/usr/bin/python
from setuptools import setup, find_packages

# Import the module version
from grpc_api_client import __version__

# Run the setup
setup(
    name             = 'grpc_api_client',
    version          = __version__,
    description      = 'Python bindings for interacting with a gRPC API server.',
    long_description = open('DESCRIPTION.rst').read(),
    author           = 'David Taylor',
    author_email     = 'djtaylor13@gmail.com',
    url              = 'http://github.com/djtaylor/python-grpc-api-client',
    license          = 'GPLv3',
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
    packages         = find_packages(),
    keywords         = 'grpc rpc api',
    classifiers      = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Terminals',
    ]
)
