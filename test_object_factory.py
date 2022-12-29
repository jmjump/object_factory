#!/usr/bin/python3
import os
import time
import unittest
import sys

from unittest.mock import patch
from unittest.mock import MagicMock

import object_factory

class Type1:
    def __init__(self):
        pass

class Type2:
    def __init__(self):
        pass


class TestObjectFactory(unittest.TestCase):
    def test_GoodCreate(self):
        myFactory = object_factory.ObjectFactory()

        myFactory.register('Type1', Type1)
        myFactory.register('Type2', Type2)

        aType1 = myFactory.create('Type1')
        aType2 = myFactory.create('Type2')

        self.assertIsInstance(aType1, Type1)
        self.assertIsInstance(aType2, Type2)

    def test_GoodCreateWithFunction(self):
        myFactory = object_factory.ObjectFactory()

        myFactory.register('Type1', create_type1)
        myFactory.register('Type2', create_type2)

        aType1 = myFactory.create('Type1')
        aType2 = myFactory.create('Type2')

        self.assertIsInstance(aType1, Type1)
        self.assertIsInstance(aType2, Type2)

    def test_BadCreate(self):
        myFactory = object_factory.ObjectFactory()

        self.assertRaises(ValueError, myFactory.create, 'something')


if __name__ == '__main__':
    unittest.main()
