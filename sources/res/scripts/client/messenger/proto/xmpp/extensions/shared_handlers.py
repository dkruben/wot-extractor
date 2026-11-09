# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/messenger/proto/xmpp/extensions/shared_handlers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/proto/xmpp/extensions/shared_handlers.py
from __future__ import absolute_import
from messenger.proto.xmpp.extensions import PyHandler

class IQHandler(PyHandler):

    def getFilterString(self):
        return ('/iq/{0}').format(self._ext.getXPath())


class IQChildHandler(PyHandler):
    __slots__ = ('_index', )

    def __init__(self, ext, index=0):
        super(IQChildHandler, self).__init__(ext)
        self._index = index

    def getFilterString(self):
        return ('/iq/{0}').format(self._ext.getXPath(self._index))

    def handleTag(self, pyGlooxTag):
        child = self._ext.getChild(self._index)
        if not child:
            return
        result = pyGlooxTag.filterXPath(self.getFilterString())
        for tag in result:
            data = child.parseTag(tag)
            if data:
                yield data


class ProxyHandler(PyHandler):

    def getFilterString(self):
        return self._ext.getXPath()
