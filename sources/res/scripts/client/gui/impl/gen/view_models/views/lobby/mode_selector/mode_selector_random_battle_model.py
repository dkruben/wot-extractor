# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/mode_selector/mode_selector_random_battle_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/mode_selector/mode_selector_random_battle_model.py
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_normal_card_model import ModeSelectorNormalCardModel

class ModeSelectorRandomBattleModel(ModeSelectorNormalCardModel):
    __slots__ = ()

    def __init__(self, properties=25, commands=0):
        super(ModeSelectorRandomBattleModel, self).__init__(properties=properties, commands=commands)

    def getSettingsPopoverID(self):
        return self._getNumber(22)

    def setSettingsPopoverID(self, value):
        self._setNumber(22, value)

    def getIsSettingsActive(self):
        return self._getBool(23)

    def setIsSettingsActive(self, value):
        self._setBool(23, value)

    def getWithSettingsNotification(self):
        return self._getBool(24)

    def setWithSettingsNotification(self, value):
        self._setBool(24, value)

    def _initialize(self):
        super(ModeSelectorRandomBattleModel, self)._initialize()
        self._addNumberProperty('settingsPopoverID', -1)
        self._addBoolProperty('isSettingsActive', False)
        self._addBoolProperty('withSettingsNotification', False)
