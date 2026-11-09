# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/battle/battle_page/prebattle_ammunition_setup_selector.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle/battle_page/prebattle_ammunition_setup_selector.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_setup_selector import AmmunitionSetupSelector

class PrebattleAmmunitionSetupSelector(AmmunitionSetupSelector):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(PrebattleAmmunitionSetupSelector, self).__init__(properties=properties, commands=commands)

    def getHotKeys(self):
        return self._getArray(3)

    def setHotKeys(self, value):
        self._setArray(3, value)

    @staticmethod
    def getHotKeysType():
        return unicode

    def _initialize(self):
        super(PrebattleAmmunitionSetupSelector, self)._initialize()
        self._addArrayProperty('hotKeys', Array())
