# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/tabbed_full_stats.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from gui.Scaleform.daapi.view.meta.TabbedFullStatsMeta import TabbedFullStatsMeta as TabbedFullStatsMeta
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from gui.battle_control.battle_constants import TabsAliases as TabsAliases
_logger: Any

class TabbedFullStatsComponent(TabbedFullStatsMeta):
    __tabsMap: Any
    def __init__(self):
        ...
    @property
    def hasTabs(self):
        ...
    def hasTab(self, alias):
        ...
    def setActiveTab(self, tabAlias):
        ...
    def _populate(self):
        ...
    def _destroy(self):
        ...
    @staticmethod
    def _buildTabs(builder):
        ...

class _TabsBuilder(object):
    __lobbyContext: Any
    __tabs: Any
    def __init__(self):
        ...
    def addStatisticsTab(self):
        ...
    def addPersonalQuestsTab(self):
        ...
    def addBoostersTab(self):
        ...
    def getTabs(self):
        ...
    def __isBoosterProcessingAvailable(self):
        ...
