# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/gen/view_models/loadout/shells/fun_random_custom_shell_slot.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/impl/gen/view_models/loadout/shells/fun_random_custom_shell_slot.py
from gui.impl.gen.view_models.views.lobby.tank_setup.common.base_ammunition_slot import BaseAmmunitionSlot

class FunRandomCustomShellSlot(BaseAmmunitionSlot):
    __slots__ = ()

    def __init__(self, properties=17, commands=0):
        super(FunRandomCustomShellSlot, self).__init__(properties=properties, commands=commands)

    def getCount(self):
        return self._getNumber(13)

    def setCount(self, value):
        self._setNumber(13, value)

    def getOriginalIdx(self):
        return self._getNumber(14)

    def setOriginalIdx(self, value):
        self._setNumber(14, value)

    def getImageNameOverride(self):
        return self._getString(15)

    def setImageNameOverride(self, value):
        self._setString(15, value)

    def getTooltipOverride(self):
        return self._getString(16)

    def setTooltipOverride(self, value):
        self._setString(16, value)

    def _initialize(self):
        super(FunRandomCustomShellSlot, self)._initialize()
        self._addNumberProperty('count', 0)
        self._addNumberProperty('originalIdx', 0)
        self._addStringProperty('imageNameOverride', '')
        self._addStringProperty('tooltipOverride', '')
