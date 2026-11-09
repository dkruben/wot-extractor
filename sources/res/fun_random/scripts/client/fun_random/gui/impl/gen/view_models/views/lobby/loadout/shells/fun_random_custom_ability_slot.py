# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/loadout/shells/fun_random_custom_ability_slot.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/loadout/shells/fun_random_custom_ability_slot.py
from gui.impl.gen.view_models.views.lobby.tank_setup.common.base_ammunition_slot import BaseAmmunitionSlot

class FunRandomCustomAbilitySlot(BaseAmmunitionSlot):
    __slots__ = ()

    def __init__(self, properties=14, commands=0):
        super(FunRandomCustomAbilitySlot, self).__init__(properties=properties, commands=commands)

    def getTooltipAlias(self):
        return self._getString(13)

    def setTooltipAlias(self, value):
        self._setString(13, value)

    def _initialize(self):
        super(FunRandomCustomAbilitySlot, self)._initialize()
        self._addStringProperty('tooltipAlias', '')
