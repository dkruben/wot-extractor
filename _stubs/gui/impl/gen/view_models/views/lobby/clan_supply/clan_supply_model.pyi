# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/clan_supply/clan_supply_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import IntEnum as IntEnum
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.clan_supply.pages.progression_model import ProgressionModel as ProgressionModel
from gui.impl.gen.view_models.views.lobby.clan_supply.pages.quests_model import QuestsModel as QuestsModel
from gui.impl.gen.view_models.views.lobby.clan_supply.sidebar_model import SidebarModel as SidebarModel

class ClanSupplyViews(IntEnum):
    PROGRESSION = 0
    QUESTS = 1

class ClanSupplyModel(ViewModel):
    __slots__: tuple
    onClose: Any
    onInfoPageOpen: Any
    def __init__(self, properties=5, commands=2):
        ...
    @property
    def sidebar(self):
        ...
    @staticmethod
    def getSidebarType():
        ...
    @property
    def progressionModel(self):
        ...
    @staticmethod
    def getProgressionModelType():
        ...
    @property
    def questsModel(self):
        ...
    @staticmethod
    def getQuestsModelType():
        ...
    def getPageViewId(self):
        ...
    def setPageViewId(self, value):
        ...
    def getCurrencyValue(self):
        ...
    def setCurrencyValue(self, value):
        ...
    def _initialize(self):
        ...
