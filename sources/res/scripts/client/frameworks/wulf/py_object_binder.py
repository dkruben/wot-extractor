# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/frameworks/wulf/py_object_binder.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/frameworks/wulf/py_object_binder.py


def getProxy(object_):
    if object_ is not None:
        return object_.proxy
    else:
        return


def getObject(proxy):
    if proxy is not None:
        return proxy.object
    else:
        return


class PyObjectEntity(object):
    __slots__ = ('__cppObject', '__weakref__')

    def __init__(self, cppObject=None):
        super(PyObjectEntity, self).__init__()
        self.__cppObject = None
        if cppObject is not None:
            self.bind(cppObject)
        return

    @property
    def proxy(self):
        return self.__cppObject

    def isBound(self):
        return self.__cppObject is not None

    def unbind(self):
        if self.isBound():
            self._unbind()

    def bind(self, cppObject):
        if self.__cppObject == cppObject:
            return
        else:
            self.unbind()
            self.__cppObject = cppObject
            if cppObject is not None:
                self._bind(cppObject)
            return

    def _bind(self, cppObject):
        cppObject.bindPyObject(self)

    def _unbind(self):
        prevCppObject = self.__cppObject
        self.__cppObject = None
        prevCppObject.unbindPyObject()
        return
