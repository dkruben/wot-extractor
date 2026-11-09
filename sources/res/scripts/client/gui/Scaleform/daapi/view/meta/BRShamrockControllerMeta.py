# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/BRShamrockControllerMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BRShamrockControllerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BRShamrockControllerMeta(BaseDAAPIComponent):

    def as_addPointsS(self, amount, newTotal, fromTeammate):
        if self._isDAAPIInited():
            return self.flashObject.as_addPoints(amount, newTotal, fromTeammate)

    def as_setCounterS(self, amount):
        if self._isDAAPIInited():
            return self.flashObject.as_setCounter(amount)
