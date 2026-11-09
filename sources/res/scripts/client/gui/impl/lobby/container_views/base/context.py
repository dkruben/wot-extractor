# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/container_views/base/context.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/container_views/base/context.py
from helpers import dependency
from skeletons.gui.shared import IItemsCache

class ContextBase(object):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def update(self, *args, **kwargs):
        raise NotImplementedError


class TankmanContext(ContextBase):
    __slots__ = ('_tankmanID', '_tankman', '_tankmanCurrentVehicle', '_tankmanNativeVehicle')

    def __init__(self, tankmanID, *args, **kwargs):
        self._tankmanID = None
        self._tankman = None
        super(TankmanContext, self).__init__(tankmanID)
        return

    @property
    def tankmanID(self):
        return self._tankmanID

    @property
    def tankman(self):
        return self._tankman

    def update(self, tankmanID):
        self._tankmanID = tankmanID
        self._tankman = self.itemsCache.items.getTankman(self._tankmanID)
