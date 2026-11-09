# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/py2to3/patched_typing.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/py2to3/patched_typing.py
from __future__ import absolute_import
import abc, typing
from future.utils import PY2
if not typing.TYPE_CHECKING and PY2:

    class _RuntimeGenericMeta(abc.ABCMeta):

        def __getitem__(cls, item):
            return cls


    class Generic(object):
        __metaclass__ = _RuntimeGenericMeta
        __slots__ = ()


else:
    Generic = typing.Generic
__all__ = ('Generic', )
