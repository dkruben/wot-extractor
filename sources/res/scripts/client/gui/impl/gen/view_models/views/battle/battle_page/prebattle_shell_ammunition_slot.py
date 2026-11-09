# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/battle/battle_page/prebattle_shell_ammunition_slot.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle/battle_page/prebattle_shell_ammunition_slot.py
from enum import IntEnum
from gui.impl.gen.view_models.views.lobby.tank_setup.common.shell_ammunition_slot import ShellAmmunitionSlot

class ShellBattleState(IntEnum):
    NORMAL = 0
    CURRENT = 1
    NEXT = 2


class PrebattleShellAmmunitionSlot(ShellAmmunitionSlot):
    __slots__ = ()

    def __init__(self, properties=17, commands=0):
        super(PrebattleShellAmmunitionSlot, self).__init__(properties=properties, commands=commands)

    def getShellState(self):
        return ShellBattleState(self._getNumber(16))

    def setShellState(self, value):
        self._setNumber(16, value.value)

    def _initialize(self):
        super(PrebattleShellAmmunitionSlot, self)._initialize()
        self._addNumberProperty('shellState')
