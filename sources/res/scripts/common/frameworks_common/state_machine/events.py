# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/frameworks_common/state_machine/events.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/frameworks_common/state_machine/events.py
from __future__ import absolute_import
import typing

class StateEvent(object):
    __slots__ = ('__arguments', )

    def __init__(self, *args, **kwargs):
        super(StateEvent, self).__init__()
        self.__arguments = kwargs

    def __repr__(self):
        return ('{}({})').format(self.__class__.__name__, id(self))

    def getArgument(self, name, default=None):
        return self.__arguments.get(name, default)


class StringEvent(StateEvent):
    __slots__ = ('__token', )

    def __init__(self, token, **kwargs):
        super(StringEvent, self).__init__(**kwargs)
        self.__token = token

    def __repr__(self):
        return ('{}({})').format(self.__class__.__name__, self.__token)

    @property
    def token(self):
        return self.__token
