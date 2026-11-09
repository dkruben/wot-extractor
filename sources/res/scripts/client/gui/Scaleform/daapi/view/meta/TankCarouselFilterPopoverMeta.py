# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/TankCarouselFilterPopoverMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TankCarouselFilterPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class TankCarouselFilterPopoverMeta(SmartPopOverView):

    def changeFilter(self, groupId, itemId):
        self._printOverrideError('changeFilter')

    def changeSearchNameVehicle(self, inputText):
        self._printOverrideError('changeSearchNameVehicle')

    def switchCarouselType(self, selected):
        self._printOverrideError('switchCarouselType')

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_setStateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setState(data)

    def as_showCounterS(self, countText):
        if self._isDAAPIInited():
            return self.flashObject.as_showCounter(countText)
