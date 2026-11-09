# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/battle_royale_event_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/battle_royale_event_model.py
from battle_royale.gui.impl.gen.view_models.views.lobby.enums import CoinType, SubMode
from frameworks.wulf import ViewModel

class BattleRoyaleEventModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BattleRoyaleEventModel, self).__init__(properties=properties, commands=commands)

    def getSubMode(self):
        return SubMode(self._getString(0))

    def setSubMode(self, value):
        self._setString(0, value.value)

    def getCoinType(self):
        return CoinType(self._getString(1))

    def setCoinType(self, value):
        self._setString(1, value.value)

    def _initialize(self):
        super(BattleRoyaleEventModel, self)._initialize()
        self._addStringProperty('subMode')
        self._addStringProperty('coinType')
