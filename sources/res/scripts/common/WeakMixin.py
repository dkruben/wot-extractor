# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/WeakMixin.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/WeakMixin.py
from __future__ import absolute_import
import weakref
from inspect import getmodule
from future.utils import viewitems

class Tapped(object):
    __slots__ = ()

    def tap(self, *appliers, **props):
        for applier in appliers:
            if callable(applier):
                applier(self)

        for p, v in viewitems(props):
            try:
                setattr(self, p, v)
            except (AttributeError, TypeError):
                pass

        return self


class WeakMixin(object):

    def __new__(cls, src, *args, **kwargs):
        kls = None
        srcKlass = src.__class__
        for k in cls.__subclasses__():
            if issubclass(k, srcKlass):
                kls = k
                break

        if not kls:
            mixinName = ('_{}_weakMixin').format(srcKlass.__name__)
            module = getmodule(cls)
            kls = type(mixinName, (cls, srcKlass), {})
            if module is not None:
                setattr(module, mixinName, kls)
        obj = object.__new__(kls)
        obj.__target__ = weakref.proxy(src)
        return obj

    def __init__(self, src, *args, **kwargs):
        pass

    def __getattribute__(self, name):
        ogetattribute = object.__getattribute__
        try:
            return ogetattribute(self, name)
        except AttributeError:
            return self.__target__.__getattribute__(name)
