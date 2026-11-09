# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/metaclass.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/metaclass.py


class Metaclass(type):

    def __init__(cls, name, bases, attrs):
        super(Metaclass, cls).__init__(name, bases, attrs)
        mro = list(cls.__mro__)
        mro.pop(0)
        for base in reversed(mro):
            init = base.__dict__.get('__init_subclass__', None)
            if init:
                init.__func__(cls, name, bases, attrs)

        return
