# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/meta/BuffsPanelMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/scaleform/daapi/view/meta/BuffsPanelMeta.py
from gui.Scaleform.daapi.view.battle.shared.situation_indicators import SituationIndicators

class BuffsPanelMeta(SituationIndicators):

    def as_addBuffSlotS(self, id, imageName, tooltipText):
        if self._isDAAPIInited():
            return self.flashObject.as_addBuffSlot(id, imageName, tooltipText)

    def as_removeBuffSlotS(self, id):
        if self._isDAAPIInited():
            return self.flashObject.as_removeBuffSlot(id)

    def as_setBuffEnabledS(self, id, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setBuffEnabled(id, value)
