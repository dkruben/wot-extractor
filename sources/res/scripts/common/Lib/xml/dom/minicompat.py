# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/xml/dom/minicompat.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/xml/dom/minicompat.py
__all__ = [
 'NodeList', 'EmptyNodeList', 'StringTypes', 'defproperty']
import xml.dom
try:
    unicode
except NameError:
    StringTypes = (
     type(''),)
else:
    StringTypes = (
     type(''), type(unicode('')))

class NodeList(list):
    __slots__ = ()

    def item(self, index):
        if 0 <= index < len(self):
            return self[index]

    def _get_length(self):
        return len(self)

    def _set_length(self, value):
        raise xml.dom.NoModificationAllowedErr("attempt to modify read-only attribute 'length'")

    length = property(_get_length, _set_length, doc='The number of nodes in the NodeList.')

    def __setstate__(self, state):
        if state is None:
            state = []
        self[:] = state
        return


class EmptyNodeList(tuple):
    __slots__ = ()

    def __add__(self, other):
        NL = NodeList()
        NL.extend(other)
        return NL

    def __radd__(self, other):
        NL = NodeList()
        NL.extend(other)
        return NL

    def item(self, index):
        return

    def _get_length(self):
        return 0

    def _set_length(self, value):
        raise xml.dom.NoModificationAllowedErr("attempt to modify read-only attribute 'length'")

    length = property(_get_length, _set_length, doc='The number of nodes in the NodeList.')


def defproperty(klass, name, doc):
    get = getattr(klass, '_get_' + name).im_func

    def set(self, value, name=name):
        raise xml.dom.NoModificationAllowedErr('attempt to modify read-only attribute ' + repr(name))

    prop = property(get, set, doc=doc)
    setattr(klass, name, prop)
