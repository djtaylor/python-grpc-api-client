import string
import unittest
from numpy import random
from random import getrandbits, choice, randint

class gRPC_API_Test_Field(object):
    """
    Class object containing methods for representing a dummy test field.
    """
    def __init__(self, name, descriptor):
        """
        :param name: The field name
        :type name: str
        :param descriptor: The field descriptor object
        :type descriptor: object
        """
        self._types = {
            'TYPE_BOOL': [8, self._random_bool],
            'TYPE_BYTES': [12, self._random_bytes],
            'TYPE_DOUBLE': [1, None],
            'TYPE_ENUM': [14, None],
            'TYPE_FIXED32': [7, None],
            'TYPE_FIXED64': [6, None],
            'TYPE_FLOAT': [2, self._random_float],
            'TYPE_GROUP': [10, None],
            'TYPE_INT32': [5, self._random_int32],
            'TYPE_INT64': [3, self._random_int64],
            'TYPE_MESSAGE': [11, None],
            'TYPE_SFIXED32': [15, None],
            'TYPE_SFIXED64': [16, None],
            'TYPE_SINT32': [17, None],
            'TYPE_SINT64': [18, None],
            'TYPE_STRING': [9, self._random_str],
            'TYPE_UINT32': [13, self._random_uint32],
            'TYPE_UINT64': [4, self._random_uint64]
        }

        # Field descriptor and name
        self.name = name
        self.descriptor = descriptor

        # Type integer and string label
        self._type_str = None
        self._type_int = None
        self._get_type()

    def _random_bool(self):
        """ Return a random boolean """
        return random.choice([True, False])

    def _random_bytes(self):
        """ Return a random bytes object """
        return random.bytes(128)

    def _random_float(self):
        """ Return a random floating point integer """
        return random.uniform(1, 2)

    def _random_int32(self):
        """ Return a random 32 bit integer """
        i = 2147483648
        return randint(-i, i)

    def _random_int64(self):
        """ Return a random 64 bit integer """
        i = 9223372036854775807
        return randint(-i, i)

    def _random_str(self):
        """ Return a random unicode string """
        letters = string.ascii_letters + string.digits
        return ''.join(choice(letters) for i in range(32))

    def _random_uint32(self):
        """ Generated a random unsigned 32 bit integer """
        return getrandbits(32)

    def _random_uint64(self):
        """ Generated a random unsigned 64 bit integer """
        return getrandbits(64)

    def _get_type(self):
        """
        Convenience method for getting the type of a field.
        """
        for type_str, type_attrs in self._types.items():
            if type_attrs[0] == self.descriptor.type:
                self._type_int = type_attrs[0]
                self._type_str = type_str

    def get_test_value(self):
        """
        Return a test value for the test field instance.
        """
        random_value_method = self._types[self._type_str][1]
        if random_value_method:
            return random_value_method()

        # Not implemented
        raise Exception('Generating test value for "{}" not implemented'.format(self_type_str))

class gRPC_API_Test_Fields(object):
    """
    Construct a collection of field arguments for a request object
    when running tests.
    """
    @classmethod
    def create(cls, method):
        """
        Create a new collection of test fields for the API method object.

        :param method: An instance of the API method handler
        :type api_object: gRPC_API_Path
        """
        input_fields = {}
        for name, descriptor in method.input_fields():
            field = gRPC_API_Test_Field(name, descriptor)

            # This field value is a another class
            if descriptor.message_type:
                continue
            else:
                input_fields[name] = field.get_test_value()
        return input_fields
