# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/common/compare_toggle_ammunition_slot.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/common/compare_toggle_ammunition_slot.py
from gui.impl.gen.view_models.views.lobby.tank_setup.common.base_ammunition_slot import BaseAmmunitionSlot

class CompareToggleAmmunitionSlot(BaseAmmunitionSlot):
    __slots__ = ()

    def __init__(self, properties=15, commands=0):
        super(CompareToggleAmmunitionSlot, self).__init__(properties=properties, commands=commands)

    def getIsSelected(self):
        return self._getBool(13)

    def setIsSelected(self, value):
        self._setBool(13, value)

    def getIsLocked(self):
        return self._getBool(14)

    def setIsLocked(self, value):
        self._setBool(14, value)

    def _initialize(self):
        super(CompareToggleAmmunitionSlot, self)._initialize()
        self._addBoolProperty('isSelected', False)
        self._addBoolProperty('isLocked', False)
