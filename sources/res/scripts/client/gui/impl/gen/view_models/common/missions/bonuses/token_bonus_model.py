# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/common/missions/bonuses/token_bonus_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/missions/bonuses/token_bonus_model.py
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class TokenBonusModel(BonusModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(TokenBonusModel, self).__init__(properties=properties, commands=commands)

    def getUserName(self):
        return self._getString(8)

    def setUserName(self, value):
        self._setString(8, value)

    def getIconSmall(self):
        return self._getString(9)

    def setIconSmall(self, value):
        self._setString(9, value)

    def getIconBig(self):
        return self._getString(10)

    def setIconBig(self, value):
        self._setString(10, value)

    def _initialize(self):
        super(TokenBonusModel, self)._initialize()
        self._addStringProperty('userName', '')
        self._addStringProperty('iconSmall', '')
        self._addStringProperty('iconBig', '')
