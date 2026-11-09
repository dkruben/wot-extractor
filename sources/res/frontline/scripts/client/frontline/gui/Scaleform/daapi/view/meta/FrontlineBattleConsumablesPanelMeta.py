# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/meta/FrontlineBattleConsumablesPanelMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/Scaleform/daapi/view/meta/FrontlineBattleConsumablesPanelMeta.py
from gui.Scaleform.daapi.view.meta.ConsumablesPanelMeta import ConsumablesPanelMeta

class FrontlineBattleConsumablesPanelMeta(ConsumablesPanelMeta):

    def as_addEpicBattleEquipmentSlotS(self, idx, keyCode, sfKeyCode, quantity, timeRemaining, reloadingTime, iconPath, isTooltipSpecial, tooltipText, animation):
        if self._isDAAPIInited():
            return self.flashObject.as_addEpicBattleEquipmentSlot(idx, keyCode, sfKeyCode, quantity, timeRemaining, reloadingTime, iconPath, isTooltipSpecial, tooltipText, animation)

    def as_updateLockedInformationS(self, idx, lockedID, tooltipStr, isSlotEmpty):
        if self._isDAAPIInited():
            return self.flashObject.as_updateLockedInformation(idx, lockedID, tooltipStr, isSlotEmpty)

    def as_updateLevelInformationS(self, idx, level):
        if self._isDAAPIInited():
            return self.flashObject.as_updateLevelInformation(idx, level)

    def as_showPossibleStacksS(self, idx, stack):
        if self._isDAAPIInited():
            return self.flashObject.as_showPossibleStacks(idx, stack)

    def as_updateStacksS(self, idx, stack):
        if self._isDAAPIInited():
            return self.flashObject.as_updateStacks(idx, stack)
