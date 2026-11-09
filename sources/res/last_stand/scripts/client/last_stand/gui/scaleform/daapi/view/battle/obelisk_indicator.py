# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/obelisk_indicator.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/obelisk_indicator.py
from __future__ import absolute_import
from LSObeliskInfoComponent import LSObeliskInfoComponent, ObeliskInfoStates
from last_stand.gui.scaleform.daapi.view.meta.ObeliskMeta import ObeliskMeta
from helpers import dependency
from skeletons.gui.shared import IItemsCache

class LSObeliskIndicator(ObeliskMeta):
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self):
        super(LSObeliskIndicator, self).__init__()
        self.curObeliskName = ''

    def _populate(self):
        super(LSObeliskIndicator, self)._populate()
        component = LSObeliskInfoComponent.getInstance()
        if component is not None:
            component.onStateChange += self._onStateChange
            component.onObeliskObserved += self._onObeliskObserved
            if component.isPresent:
                self.as_setStateS(ObeliskInfoStates.SHOW)
        return

    def _dispose(self):
        component = LSObeliskInfoComponent.getInstance()
        if component is not None:
            component.onStateChange -= self._onStateChange
            component.onObeliskObserved -= self._onObeliskObserved
        super(LSObeliskIndicator, self)._dispose()
        return

    def _onStateChange(self, state):
        self.as_setStateS(state)

    def _onObeliskObserved(self, obeliskIntCD):
        item = self.__itemsCache.items.getItemByCD(obeliskIntCD)
        name = item.shortUserName if item else ''
        if self.curObeliskName != name:
            self.curObeliskName = name
            self.as_setNameS(self.curObeliskName)
