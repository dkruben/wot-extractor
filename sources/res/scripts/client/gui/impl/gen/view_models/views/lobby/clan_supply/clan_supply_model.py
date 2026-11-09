# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/clan_supply/clan_supply_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/clan_supply/clan_supply_model.py
from enum import IntEnum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.clan_supply.pages.progression_model import ProgressionModel
from gui.impl.gen.view_models.views.lobby.clan_supply.pages.quests_model import QuestsModel
from gui.impl.gen.view_models.views.lobby.clan_supply.sidebar_model import SidebarModel

class ClanSupplyViews(IntEnum):
    PROGRESSION = 0
    QUESTS = 1


class ClanSupplyModel(ViewModel):
    __slots__ = ('onClose', 'onInfoPageOpen')

    def __init__(self, properties=5, commands=2):
        super(ClanSupplyModel, self).__init__(properties=properties, commands=commands)

    @property
    def sidebar(self):
        return self._getViewModel(0)

    @staticmethod
    def getSidebarType():
        return SidebarModel

    @property
    def progressionModel(self):
        return self._getViewModel(1)

    @staticmethod
    def getProgressionModelType():
        return ProgressionModel

    @property
    def questsModel(self):
        return self._getViewModel(2)

    @staticmethod
    def getQuestsModelType():
        return QuestsModel

    def getPageViewId(self):
        return ClanSupplyViews(self._getNumber(3))

    def setPageViewId(self, value):
        self._setNumber(3, value.value)

    def getCurrencyValue(self):
        return self._getNumber(4)

    def setCurrencyValue(self, value):
        self._setNumber(4, value)

    def _initialize(self):
        super(ClanSupplyModel, self)._initialize()
        self._addViewModelProperty('sidebar', SidebarModel())
        self._addViewModelProperty('progressionModel', ProgressionModel())
        self._addViewModelProperty('questsModel', QuestsModel())
        self._addNumberProperty('pageViewId')
        self._addNumberProperty('currencyValue', 0)
        self.onClose = self._addCommand('onClose')
        self.onInfoPageOpen = self._addCommand('onInfoPageOpen')
