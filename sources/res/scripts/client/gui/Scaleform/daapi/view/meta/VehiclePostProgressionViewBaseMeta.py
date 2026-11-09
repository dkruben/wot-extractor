# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/VehiclePostProgressionViewBaseMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehiclePostProgressionViewBaseMeta.py
from gui.Scaleform.framework.entities.View import View

class VehiclePostProgressionViewBaseMeta(View):

    def demountAllPairs(self):
        self._printOverrideError('demountAllPairs')

    def onClose(self):
        self._printOverrideError('onClose')

    def as_setVehicleTitleS(self, vo):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleTitle(vo)

    def as_setDataS(self, vo):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(vo)

    def as_showS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_show()
