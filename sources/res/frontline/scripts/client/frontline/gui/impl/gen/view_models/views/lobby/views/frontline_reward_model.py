# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/views/frontline_reward_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/views/frontline_reward_model.py
from enum import Enum
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class ClaimState(Enum):
    STATIC = 'static'
    CLAIMABLE = 'claimable'


class FrontlineRewardModel(IconBonusModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(FrontlineRewardModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getString(9)

    def setId(self, value):
        self._setString(9, value)

    def getClaimState(self):
        return ClaimState(self._getString(10))

    def setClaimState(self, value):
        self._setString(10, value.value)

    def getType(self):
        return self._getString(11)

    def setType(self, value):
        self._setString(11, value)

    def getOverlayType(self):
        return self._getString(12)

    def setOverlayType(self, value):
        self._setString(12, value)

    def _initialize(self):
        super(FrontlineRewardModel, self)._initialize()
        self._addStringProperty('id', '')
        self._addStringProperty('claimState')
        self._addStringProperty('type', '')
        self._addStringProperty('overlayType', '')
