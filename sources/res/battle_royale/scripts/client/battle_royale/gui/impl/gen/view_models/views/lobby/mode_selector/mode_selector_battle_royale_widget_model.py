# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/mode_selector/mode_selector_battle_royale_widget_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/mode_selector/mode_selector_battle_royale_widget_model.py
from enum import Enum
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_base_widget_model import ModeSelectorBaseWidgetModel

class BattleRoyaleProgressionStatus(Enum):
    DISABLED = 'disabled'
    ACTIVE = 'active'


class ModeSelectorBattleRoyaleWidgetModel(ModeSelectorBaseWidgetModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(ModeSelectorBattleRoyaleWidgetModel, self).__init__(properties=properties, commands=commands)

    def getStatus(self):
        return BattleRoyaleProgressionStatus(self._getString(1))

    def setStatus(self, value):
        self._setString(1, value.value)

    def getCurrentStage(self):
        return self._getNumber(2)

    def setCurrentStage(self, value):
        self._setNumber(2, value)

    def getStageCurrentPoints(self):
        return self._getNumber(3)

    def setStageCurrentPoints(self, value):
        self._setNumber(3, value)

    def getStageMaximumPoints(self):
        return self._getNumber(4)

    def setStageMaximumPoints(self, value):
        self._setNumber(4, value)

    def _initialize(self):
        super(ModeSelectorBattleRoyaleWidgetModel, self)._initialize()
        self._addStringProperty('status')
        self._addNumberProperty('currentStage', -1)
        self._addNumberProperty('stageCurrentPoints', -1)
        self._addNumberProperty('stageMaximumPoints', -1)
