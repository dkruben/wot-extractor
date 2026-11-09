# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/meta/FrontlineCarouselFilterPopoverMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/Scaleform/daapi/view/meta/FrontlineCarouselFilterPopoverMeta.py
from gui.Scaleform.daapi.view.common.filter_popover import TankCarouselFilterPopover

class FrontlineCarouselFilterPopoverMeta(TankCarouselFilterPopover):

    def onPlayListsChange(self, playListId):
        self._printOverrideError('onPlayListsChange')

    def as_updatePlayListsS(self, dataProvider):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePlayLists(dataProvider)
