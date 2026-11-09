# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/frameworks/wulf/view/command.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/frameworks/wulf/view/command.py
from __future__ import absolute_import
import typing
from Event import Event
from ..py_object_binder import PyObjectEntity
from ..py_object_wrappers import PyObjectCommand

class Command(PyObjectEntity):
    __slots__ = ('__event', )

    def __init__(self):
        super(Command, self).__init__(PyObjectCommand())
        self.__event = Event()

    def __call__(self, args=None):
        if args is not None:
            args = (
             args,)
        else:
            args = ()
        self.__event(*args)
        return

    @property
    def name(self):
        return self.proxy.name

    def execute(self, args=None):
        if args is not None:
            args = (
             args,)
        else:
            args = ()
        self.proxy.execute(*args)
        return

    def _unbind(self):
        self.__event.clear()
        super(Command, self)._unbind()

    def _cNotify(self, args=None):
        if args is not None:
            args = (
             args,)
        else:
            args = ()
        self.__event(*args)
        return

    def __iadd__(self, delegate):
        self.__event += delegate
        return self

    def __isub__(self, delegate):
        self.__event -= delegate
        return self
