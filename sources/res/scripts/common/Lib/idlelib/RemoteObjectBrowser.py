# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/idlelib/RemoteObjectBrowser.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/idlelib/RemoteObjectBrowser.py
from idlelib import rpc

def remote_object_tree_item(item):
    wrapper = WrappedObjectTreeItem(item)
    oid = id(wrapper)
    rpc.objecttable[oid] = wrapper
    return oid


class WrappedObjectTreeItem:

    def __init__(self, item):
        self.__item = item

    def __getattr__(self, name):
        value = getattr(self.__item, name)
        return value

    def _GetSubList(self):
        list = self.__item._GetSubList()
        return map(remote_object_tree_item, list)


class StubObjectTreeItem:

    def __init__(self, sockio, oid):
        self.sockio = sockio
        self.oid = oid

    def __getattr__(self, name):
        value = rpc.MethodProxy(self.sockio, self.oid, name)
        return value

    def _GetSubList(self):
        list = self.sockio.remotecall(self.oid, '_GetSubList', (), {})
        return [StubObjectTreeItem(self.sockio, oid) for oid in list]
